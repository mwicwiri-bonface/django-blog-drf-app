from django.test import TestCase

from django.contrib.auth import get_user_model

from blog.models import Category, Post

User = get_user_model()


class TestCreatePost(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_category = Category.objects.create(name="postgres")
        test_user = User.objects.create_user(username="test_user1", password="123456789")
        Post.objects.create(
            category=test_category, author=test_user, title="Full text search", excerpt="hjhj", content="hjfkh",
        )

    def test_blog_content(self):
        post = Post.objects.get(id=1)
        category = Category.objects.get(id=1)
        author = post.author
        category_post = post.category
        self.assertEqual(author.username, 'test_user1')
        self.assertEqual(category_post, category)
        self.assertEqual(category_post, category)
        self.assertEqual(post.title, "Full text search")
        self.assertEqual(post.excerpt, "hjhj")
        self.assertEqual(post.content, "hjfkh")
        self.assertEqual(str(post), "Full text search")
        self.assertEqual(str(category), "postgres")
        self.assertTrue(isinstance(category_post, Category))
