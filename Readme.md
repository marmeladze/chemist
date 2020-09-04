###Create batch data

```python

from inventory.models import Drug, Company
from faker import Faker


faker = Faker()

for _ in range(20):
    Company.objects.create(name = faker.name(), country = faker.country())


companies = Company.objects.all()

for company in companies:
  for _ in range(20):
      Drug.objects.create(name = faker.user_name(), company = company)



```



### Adding support for legacy db


```sh
python manage.py inspectdb > $APP_NAME/models.py
```

Inspect changes on terminal output. Change model/field names. 

```sh
python manage.py migrate
```




