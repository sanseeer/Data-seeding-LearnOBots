import os, django, random


os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'sls_dal_p.settings')

django.setup()

from sls_dal.models import UserProfile
from django.contrib.auth.models import User

from faker import Faker

from django.utils import timezone


def student(N):
    fake = Faker()
    for _ in range(N):
        #id = random.randint(1, 100)
        vc=fake.text()
        fakephone=random.choice([1,2,3,4,5])
        fakename=fake.name()
        fakestreet=fake.name()
        fakecity=fake.city()
        fakestate=fake.name()
        fakezip=random.choice([1,2,3,4,5])
        fakeregistrationToken=random.choice([1,2,3,4,5])
        fakecurrentcategory=fake.text()


        image = random.choice(['image1', 'image2','image3','image4','image5'])
      
        UserProfile.objects.create(
        	id = random.randint(1,2),
            gender=random.choice(['male', 'female','not_specified']),
            verification_code=vc,
            phone=fakephone,
            name=fakename,
            street=fakestreet,
            city=fakecity,
            state=fakestate,
            zip=fakezip,
            registrationToken=fakeregistrationToken,
            currentCategory=fakecurrentcategory,
            score=random.choice([1.01,2.01]),
            account_type=random.choice(["Moderator","Student","Parent","Teacher","CampusAdmin","Demo"]),
            new_badge=random.choice([1,2,3,4,5])

            )


student(10)
print('Data is populated')