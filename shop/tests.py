from django.test import TestCase

# Create your tests here.
from django.contrib.auth.models import User
class test(TestCase):
    u = User.objects.all()
    print(u)