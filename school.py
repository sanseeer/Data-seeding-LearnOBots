import os, django, random


os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'sls_dal_p.settings')

django.setup()

from sls_dal.models import School
from django.contrib.auth.models import User
from faker import Faker
from django.utils import timezone

def student(N):
    fake = Faker()
    for s in range(N):
    	logo = random.choice(['image1', 'image2','image3','image4','image5'])
    	faddress=fake.address()
    	School.objects.create(
    	#id = s,
    	name=random.choice(['School1', 'School2', 'School3','School4','School5']),
    	address=faddress,
        )
student(10)
print('Data is populated')