from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from django.contrib.auth import get_user_model

from blog.models import Category, Post

User = get_user_model()


class PostTests(APITestCase):
    def test_view_posts(self):
        url = reverse("blog:post-list-create")
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def create_post(self):
        self.test_category = Category.objects.create(name="postgres")
        self.test_user = User.objects.create_user(username="test_user1", password="123456789")
        data = dict(category=1, author=1, title="Full text search", excerpt="hjhj", content="hjfkh")
        url = reverse("blog:post-list-create")
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
