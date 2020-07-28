from django.test import TestCase
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.test.client import Client
from apps.myblog.models import Post

class SigninTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='test',
                    password='12test12', email='test@example.com')
        self.user.save()

    def test_correct_user(self):
        user = authenticate(username='test', password='12test12')
        self.assertTrue((user is not None) and user.is_authenticated)

    def test_correct_author(self):
        self.author = User.objects.get(username='test')
        user = authenticate(username=self.author, password='12test12')
        self.assertTrue((user is not None) and user.is_authenticated)

    def test_correct_post(self):
        self.post = Post.objects.create(author=self.user, title='ini title', content='ini content')
        record = Post.objects.get(author=self.user)
        self.assertEqual(record.title, 'ini title')
        self.assertEqual(record.content, 'ini content')
   
    def test_wrong_user(self):
        user = authenticate(username='test2', password='12test12')
        self.assertFalse((user is not None) and user.is_authenticated)

    def test_wrong_author(self):
        self.author = User.objects.get(username='test')
        user = authenticate(username=self.author, password='12test122')
        self.assertFalse((user is not None) and user.is_authenticated)

    def test_wrong_post(self):
        self.post = Post.objects.create(author=self.user, title='ini title', content='ini content')
        record = Post.objects.get(author=self.user)
        self.assertNotEqual(record.title, 'ini title2')
        self.assertNotEqual(record.content, 'ini content2')