import os
from pathlib import Path
from datetime import timedelta
from django.utils.translation import gettext_lazy as _
from core.settings.jazzmin import JAZZMIN_SETTINGS
from dotenv import load_dotenv

CSRF_TRUSTED_ORIGINS = ['https://d8d2-158-181-248-104.ngrok-free.app']

load_dotenv()
DEBUG = os.environ.get('DJANGO_DEBUG', '') != 'False'
BASE_DIR = Path(__file__).resolve().parent.parent.parent
#SECRET_KEY = os.environ.get("SECRET_KEY")
SECRET_KEY = 'django-insecure-6hsivhlmq8-fv4$0hy9&_^pcjsp)o*f1poic6eegmzhb@#1ht5'
ALLOWED_HOSTS = ['*']
if DEBUG:
    try:
        from .development import *
    except ImportError:
        raise ImportError("Файл development.py не найден")
else:
    try:
        from .production import *
    except ImportError:
        raise ImportError("Файл production.py не найден")

THEME_APPS = [
    "jazzmin",
]

DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

MY_APPS = [
    "app.students",
    "app.AboutAcademy",
    "app.activity",
    "app.mainpage",
    "app.gellary",
    "app.management",
    "app.ology",
    "app.education",
    "app.applicants",
    "app.search",
    # 'app.Getrequest',
]



LIBRARY_APPS = [
    'modeltranslation',
    "rest_framework",
    "corsheaders",
    'drf_yasg',
    'ckeditor',
    'django_ckeditor_5',
    'django_filters',
]

LANGUAGES = [
    ('ru', _('Russian')),
    ('ky', _('Kyrgyz')),
    ('en', _('English')),
    ('tr', _('Turkish')),
    ('ar', _('Arabic')),
]


MODELTRANSLATION_DEFAULT_LANGUAGE = 'ru'


MODELTRANSLATION_LANGUAGES = ('ru', 'ky', 'tr', 'ar', 'en')

TRANSLATABLE_MODEL_MODULES = ['app.base.models']


LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale'),
    os.path.join(BASE_DIR, 'locale'),
]

INSTALLED_APPS = [
    *THEME_APPS,
    *DJANGO_APPS,
    *MY_APPS,
    *LIBRARY_APPS,
]

CKEDITOR_UPLOAD_PATH = "uploads/"
CKEDITOR_JQUERY_URL = '//ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js'  # URL to jQuery
CKEDITOR_IMAGE_BACKEND = "pillow"  # Путь к пакету Pillow для обработки изображений
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Custom',  # Вы можете настроить свою собственную панель инструментов CKEditor
        'height': 300,
        'width': 800,
    },
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
]

REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
}


ROOT_URLCONF = "core.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]


WSGI_APPLICATION = "core.wsgi.application"

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

LANGUAGE_CODE = "ru"

TIME_ZONE = "Asia/Bishkek"

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = "static/"
STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "media/"
MEDIA_ROOT = BASE_DIR/"media"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

CORS_ALLOW_ALL_ORIGINS = True

JAZZMIN_SETTINGS=JAZZMIN_SETTINGS
AUTH_USER_MODEL = "auth.User"

CKEDITOR_5_CONFIGS = {
    'default': {
        'toolbar': 'full',
        'height': 300,
        'width': '100%',
        'config': {
            'language': 'en',
        },
    },
}
