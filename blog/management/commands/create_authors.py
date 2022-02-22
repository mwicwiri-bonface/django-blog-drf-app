import random

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

from blog.utils import generate_key


class Command(BaseCommand):
    help = 'Creates the various authors'
    common_password = 'blog123$'

    def add_arguments(self, parser):
        parser.add_argument('--authors', type=int, help='The number of users that should be created.')

    def handle(self, *args, **options):
        names = ['James', 'John', 'Robert', 'Michael', 'William', 'David', 'Richard', 'Joseph', 'Thomas', 'Charles',
                 'Bonface', 'Caily', 'Maureen', 'Patrick', 'Peter', 'Samuel', 'Maxwell', 'Kelvin']
        surname = ['Smith', 'Jones', 'Taylor', 'Brown', 'Williams', 'Wilson', 'Johnson', 'Davies', 'Patel', 'Wright',
                   'Mwicwiri', 'Otieno', 'Kirimi', 'Macharia', 'Kendi']
        User = get_user_model()
        authors = options['authors'] if options['authors'] else 1000
        created_authors = User.objects.all().count()
        while created_authors < authors:
            username = "-".join((random.choice(surname), generate_key(6, 6)))
            if not User.objects.filter(username=username).exists():
                User.objects.create_user(email=f'{username}@gmail.com', first_name=random.choice(names),
                                         last_name=random.choice(surname), username=username,
                                         password=self.common_password)
            created_authors = User.objects.all().count()
        self.stdout.write(self.style.SUCCESS(f'{created_authors} authors, have been created successfully create posts'))
