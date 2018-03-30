from django.test import TestCase

# Create your tests here.

from django.contrib.auth.models import User
from django.db import connection
from django.test import TestCase

from .models import Category


class TestCategory(TestCase):
    def setUp(self):
        user = User.objects.create_user('huangke', 'kwell@163.com', 'password')
        for i in range(10):
            category_name = 'cate_%s' % i
            Category.objects.create(name=category_name, owner=user)
    
    def test_filter(self):
        queryset = Category.objects.first()
        print(queryset.name)
