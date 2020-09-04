class CompanySerializer:
    def __init__(self, company):
        self.company = company


    def to_dict(self):
        # company_name, origin_country = self.company.name.split(", ")
        return {
          'uuid': str(self.company.uuid),
          'name': self.company.name,
          'list_items': f'http://localhost:8000/inventory/companies/{self.company.uuid}'
        }


    def to_xml(self):
        pass

class ItemSerializer:
    def __init__(self, item):
        self.item = item


    def to_dict(self):
        return {
          'uuid': str(self.item.uuid),
          'name': self.item.name,
          'ingredient_uuid': str(self.item.ingredient_uuid_id),
          'dosage': f'{self.item.dosage_qty} {self.item.dosage_unit}',
          'wholesale_price': self.item.wholesale_price,
          'sale_price': self.item.sale_price
        }
