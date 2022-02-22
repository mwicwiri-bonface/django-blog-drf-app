import random

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

from blog.models import Category
from blog.utils import generate_key


class Command(BaseCommand):
    help = 'Creates the various categories'

    def add_arguments(self, parser):
        parser.add_argument('--categories', type=int, help='The number of categories that should be created.')

    def handle(self, *args, **options):
        categories_list = ['Economics', 'Parenting', 'Career', 'Political', 'Finance', 'Pet', 'Gaming', 'DIY',
                           'Celebrating Gossip', 'wine', 'sports', 'entertainment', 'shopping']
        categories = options['categories'] if options['categories'] else 1000
        created_categories = Category.objects.all().count()
        while created_categories < categories:
            name = "-".join((random.choice(categories_list), generate_key(6, 6)))
            if not Category.objects.filter(name=name).exists():
                Category.objects.create(name=name)
            created_categories = Category.objects.all().count()
        self.stdout.write(self.style.SUCCESS(f'{created_categories} categories, have been created successfully'))
