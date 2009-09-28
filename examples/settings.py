DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASE_ENGINE = 'sqlite3'
DATABASE_NAME = ':memory:'

TIME_ZONE = 'UTC'
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

SECRET_KEY = 'mjq@mq5^gqzt*a6^0m)bt4%d)xur!)6b)^890vhsag42z@s!cp'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
)

MIDDLEWARE_CLASSES = (
)

ROOT_URLCONF = 'examples.urls'

TEMPLATE_DIRS = ()

INSTALLED_APPS = (
    'django_html',
)
