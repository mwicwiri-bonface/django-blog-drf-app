# A Blog Website using Django, DRF

## Step 1.1 Create a settings.ini
create a settings.ini file in core directory add the following
```ini
[settings]
DEBUG=True
SECRET_KEY=SOMEKEY
```
## Step 1.2 Django configuration
installing dependencies and migrating database
```commandline
pip install -r requirements.txt

python manage.py makemigrations --settings=core.settings.development

python manage.py migrate --settings=core.settings.development
```

## Step 1.3 Populating database
run following commands in the given order below
```commandline
python manage.py create_authors --authors=200 --settings=core.settings.development  
python manage.py create_categories --categories=20 --settings=core.settings.development  
python manage.py create_posts --posts=300 --settings=core.settings.development  
```

## Step 1.4 For running tests
```commandline
python manage.py test --settings=core.settings.development
```

## Step 1.5 For running project
```commandline
python manage.py runserver --settings=core.settings.development
```