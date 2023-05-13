import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','orm.settings') 
import django
django.setup()

from app.models import Employee
from random import*
from faker import Faker
faker=Faker()


def populate(n):
    for i in range(n):
        feno=randint(1,100)
        fename =faker.name()
        fesal = randint(15000,25000)
        feaddr = faker.city()
        emp_record = Employee.objects.get_or_create(eno=feno,ename=fename,esal=fesal,eaddr=feaddr)
populate(15)