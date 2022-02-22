from autoslug import AutoSlugField
from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _
from blog.utils import generate_key

User = get_user_model()


class TimeStampedModel(models.Model):
    class Meta:
        abstract = True

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class Category(models.Model):
    slug = AutoSlugField(populate_from='name')
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Post(TimeStampedModel):
    class STATUS(models.TextChoices):
        DRAFT = 'draft', _('Draft')
        PUBLISHED = 'published', _('Published')

    class PublishedObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status='published').select_related('category', 'author')

    slug = AutoSlugField(populate_from='slug_name')
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    title = models.CharField(max_length=255)
    excerpt = models.TextField(null=True)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.PROTECT, related_name="blog_posts")
    status = models.CharField(choices=STATUS.choices, default=STATUS.DRAFT, max_length=20)
    objects = models.Manager()
    published_objects = PublishedObjects()

    class Meta:
        ordering = ('-created', )

    @property
    def slug_name(self):
        slug = "-".join((self.title, generate_key(5, 5)))
        return slug

    def __str__(self):
        return self.title
