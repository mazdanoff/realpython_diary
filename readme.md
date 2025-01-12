## Diary test project

This is a approach 
This project aims to be an exercise for a given technology stack:
- Python
- Selenium
- SQL
- Django



It was initially built thanks to RealPython's guide:\
`https://realpython.com/django-diary-project-python/`

### Setup

First, install all dependencies:\
`pip install -r requirements.txt`

Set the env variable as well to use django's admin and directly access the database used by site:\
`export DJANGO_SETTINGS_MODULE=diary.settings`

More about Django's settings [here](https://docs.djangoproject.com/en/5.1/topics/settings/#the-django-admin-utility).

The current repo's geckodriver proved to work with Firefox ver. 134.0 (64-bit). In case this is not working in the future, use Selenium Manager to gather the relevant driver.