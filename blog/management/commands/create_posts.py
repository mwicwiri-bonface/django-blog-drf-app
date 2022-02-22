import random
from datetime import datetime, timedelta

import pytz
from django.core.management.base import BaseCommand

from django.contrib.auth import get_user_model

from blog.models import Category, Post

User = get_user_model()


class Command(BaseCommand):
    help = 'creating blog posts.'

    def add_arguments(self, parser):
        parser.add_argument('--posts', type=int, help='The number of posts that should be created.')

    def handle(self, *args, **options):
        title = ['How to Create a Blog in 5 Minutes', 'How to Choose the Best Blogging Platform in 2019 (Compared)',
                 'Catalysts of Terror: The Prevalence and Danger of Copycat Attacks',
                 'Top 10 Hackathon Ideas 2018', 'Struggling For A Blog Post Headline? 50+ Viral Headline Examples',
                 'Microsoft Teams Vs Slack: Extended With Quick Infographic',
                 'The Proven 2019 Social Media Strategy Framework',
                 '101 Catchy Microblading Business Names for Your New Brow Studio',
                 'Are QR Codes Dead? Do People Still Use QR Codes in 2019?']
        description = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut ' \
                      'labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco ' \
                      'laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in ' \
                      'voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat' \
                      ' non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'
        authors = User.objects.all()
        categories = Category.objects.all()
        status = ['draft', 'published']
        created_posts = 0
        posts = options['posts'] if options['posts'] else 1000
        while created_posts < posts:
            dt = pytz.utc.localize(datetime.now() - timedelta(days=random.randint(0, 1825)))
            instance = Post.objects.create(
                category=random.choice(categories),
                title=random.choice(title),
                excerpt=description,
                content=description,
                author=random.choice(authors),
                status=random.choice(status),
            )
            instance.created = dt
            instance.updated = dt
            instance.save()
            created_posts = Post.objects.all().count()

        self.stdout.write(self.style.SUCCESS(f'{created_posts} posts, have been created successfully.'))
