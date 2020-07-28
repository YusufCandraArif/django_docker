from django.test import TestCase
from apps.userprofile.models import Profile
from django.contrib.auth.models import User
from django.test.client import Client
import random

##$ python manage.py test apps/userprofile/
class RegisterTestEndpoint(TestCase):
    def setUp(self):
        self.credentials = {
            'username': 'testuser',
            'email': 'okedeh@gmail.com',  
            'password': 'secret'}
        
        self.client = Client()
        # User.objects.create_user(**self.credentials)

    def test_register_pass(self):
        response = self.client.post('/register/', self.credentials, follow=True)
        username = self.credentials.get("username").strip()
        email = self.credentials.get("email").strip()
        password = self.credentials.get("password").strip()
        status_field = False 
        if username and email and password:
            status_field = True
        self.assertEqual(response.status_code, 200)
        self.assertEqual(status_field, True)

    def test_register_fail1(self):
        fields = ["username", "password", "email"]
        field = random.choice(fields)
        self.credentials[field] = " "
        response = self.client.post('/register/', self.credentials, follow=True)
        username = self.credentials.get("username").strip()
        email = self.credentials.get("email").strip()
        password = self.credentials.get("password").strip()
        status_field = False 
        if username and email and password:
            status_field = True
        self.assertEqual(response.status_code, 200)
        self.assertEqual(status_field, False)

class RegisterTestModels(TestCase):
    def setUp(self):
        User.objects.create(
            username='Project', email='project@project.com')

    def test_experiment_email(self):
        experiment_project = User.objects.get(username='Project')
        self.assertNotEqual(
            experiment_project.username, "Project2")
        self.assertNotEqual(
            experiment_project.email, "project2@project.com")

    def test_experiment_email2(self):
        experiment_project = User.objects.get(username='Project')
        self.assertEqual(
            experiment_project.username, "Project")
        self.assertEqual(
            experiment_project.email, "project@project.com")


class UpdateProfileTests(TestCase):
    def test_fields_update_profile_positive(self):
        """testing for update profile (+)"""
        user = User(username='candra.arif21', email="cancanunyu52@gmail.com", password='pinpin123')
        user.save()
        record = Profile.objects.get(user=user)
        record.bio = "Test bio."
        record.phone_number = 123456        

        self.assertEqual(record.user.username, "candra.arif21")    
        self.assertEqual(record.bio, "Test bio.")   
        self.assertEqual(record.phone_number, 123456)   

    def test_fields_update_profile_negative(self):
        """testing for update profile (-)"""
        user = User(username='candra.arif21', email="cancanunyu52@gmail.com", password='pinpin123')
        user.save()
        record = Profile.objects.get(user=user)
        record.bio = "Test bio."
        record.phone_number = 123456   

        self.assertNotEqual(record.user.username, "candra.arif211")    
        self.assertNotEqual(record.bio, "Test bio..")   
        self.assertNotEqual(record.phone_number, 1234567)   




