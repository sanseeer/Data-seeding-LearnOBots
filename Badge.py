import os, django, random


os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'sls_dal_p.settings')

django.setup()

from sls_dal.models import Badges
from django.contrib.auth.models import User

from faker import Faker

from django.utils import timezone


def student():
    fake = Faker()
    List=['Badge1', 'Badge2']
    i=0
    while i<2:      
  

        image = random.choice(['image1', 'image2','image3','image4','image5'])
        level_completion = fake.text()
        Badges.objects.create(
        	id = random.randint(1,2),
            name=List[i],            
            level=random.randint(1, 10),
            level_completion= level_completion,
            xp_required=random.randint(1, 10),
            )
        i=i+1


student()
print('Data is populated')