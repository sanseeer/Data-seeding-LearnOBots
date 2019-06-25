import os, django, random


os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'sls_dal_p.settings')

django.setup()

from sls_dal.models import Activity
from django.contrib.auth.models import User

from faker import Faker

from django.utils import timezone


def student(N):
    fake = Faker()
    for _ in range(N):

        image = random.choice(['image1', 'image2','image3','image4','image5'])
        
        blockly_url = fake.text()
        name=fake.name()
        video_url=fake.text()
        Activity.objects.create(
        	id = random.randint(1,2),
        	activity_name_en=name,
        	blockly_url=blockly_url,
        	video_id=random.randint(1, 10),
        	video_url=video_url,
            xp_on_completion=random.randint(1, 10),
            level=random.randint(1, 10),
            total_video_time=random.randint(1, 100),
            category = random.choice(['Technology', 'Science','Engineering','Arts','Mathematics','Robotics','Society']),
            )
student(10)
print('Data is populated')