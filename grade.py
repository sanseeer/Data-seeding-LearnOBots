import os, django, random


os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'sls_dal_p.settings')

django.setup()

from sls_dal.models import Grade
from django.contrib.auth.models import User

from faker import Faker

from django.utils import timezone


def student():
    List = ['1','2','3','4']
    i=0

    while i<4:
        Grade.objects.create(
        	id = random.randint(1,2),
            grade = List[i] 
            )
        i=i+1


student()
print('Data is populated')