from django.db import models


class Company(models.Model):
    uuid = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'companies'


class Ingredient(models.Model):
    uuid = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ingredients'


class ItemForms(models.Model):
    item_uuid = models.OneToOneField('Item', models.DO_NOTHING, db_column='item_uuid', primary_key=True)
    form_uuid = models.ForeignKey('PharmaceuticalForm', models.DO_NOTHING, db_column='form_uuid')

    class Meta:
        managed = False
        db_table = 'item_forms'
        unique_together = (('item_uuid', 'form_uuid'),)


class ItemPackagings(models.Model):
    item_uuid = models.OneToOneField('Item', models.DO_NOTHING, db_column='item_uuid', primary_key=True)
    packaging_uuid = models.ForeignKey('Packaging', models.DO_NOTHING, db_column='packaging_uuid')

    class Meta:
        managed = False
        db_table = 'item_packagings'
        unique_together = (('item_uuid', 'packaging_uuid'),)


class Item(models.Model):
    uuid = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    ingredient_uuid = models.ForeignKey(Ingredient, models.DO_NOTHING, db_column='ingredient_uuid', blank=True, null=True)
    company_uuid = models.ForeignKey(Company, models.DO_NOTHING, db_column='company_uuid', blank=True, null=True)
    dosage_qty = models.FloatField(blank=True, null=True)
    dosage_unit = models.CharField(max_length=10, blank=True, null=True)
    wholesale_price = models.FloatField(blank=True, null=True)
    sale_price = models.FloatField(blank=True, null=True)
    submitted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'items'


class Packaging(models.Model):
    uuid = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'packagings'


class PharmaceuticalForm(models.Model):
    uuid = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pharmaceutical_forms'
