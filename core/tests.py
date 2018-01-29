from django.test import TestCase
from django.contrib.auth.models import User,Group



# Create your tests here.

# Create user and save to the database
group1=Group.objects.create(name="dgen")
group2=Group.objects.create(name="c_sec")
group3=Group.objects.create(name="c_ser")

user = User.objects.create_user("testeus", "amad@gmail.com", "22live@93")
# Update fields and then save again
user.first_name = 'Sy'
user.last_name = 'Amadou'
user.save()
user1 = User.objects.create_user("section", "amad@gmail.com", "22live@93")
# Update fields and then save again
user1.first_name = 'Med'
user1.last_name = 'Ali'
user1.save()
user2 = User.objects.create_user("service", "amad@gmail.com", "22live@93")
# Update fields and then save again
user2.first_name = 'Sy'
user2.last_name = 'Amadou'
user2.save()
user.groups.add(group3)
user1.groups.add(group2)
user2.groups.add(group3)
user3=User.objects.get_by_natural_key('admin')
user3.groups.add(group1)