"""
Django settings for amalia project.

Generated by 'django-admin startproject' using Django 4.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""
import os
from pathlib import Path

from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from dotenv import find_dotenv
from dotenv import load_dotenv
from loguru import logger

"""
Импортируем настройки из .env
"""
if not find_dotenv():
    exit("Переменные окружения не загружены т.к отсутствует файл .env")
else:
    load_dotenv()
    logger.info("Настройки успешно импортированы")

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-89ek4b&&j31d+z)^p3-)=-m@+beimqohu_*(4prtc0fn9a3pvg"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["127.0.0.1", "localhost"]

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "import_export",
    # 'django_filters',
    # 'django_property_filter',
    "rosetta",
    "bootstrap_modal_forms",
    "widget_tweaks",
    "app_tags.apps.AppTagsConfig",
    "app_import.apps.AppImportConfig",
    "app_users.apps.AppUsersConfig",
    "app_shop.apps.AppShopConfig",
    "app_categories.apps.AppCategoriesConfig",
    "app_orders.apps.AppOrdersConfig",
    "app_settings.apps.AppSettingsConfig",
    "app_reviews.apps.AppReviewsConfig",
    "app_cart.apps.AppCartConfig",
    "app_product.apps.AppProductConfig",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "amalia.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "app_categories.context_processor.category_context",
                "app_settings.context_processor.settings_context",
                "app_users.context_processor.users_context",
                "app_cart.context_processor.cart_processor",
            ],
        },
    },
]

WSGI_APPLICATION = "amalia.wsgi.application"

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_USER_MODEL = "app_users.User"

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "app_users.validators.PasswordValidator",
    },
]

# AUTH_PASSWORD_VALIDATORS = [
#     {
#         'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
#     },
# ]

# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = "ru"

LANGUAGES = [("ru", _("Русский")), ("en", _("Английский"))]
# Сначала
# python manage.py makemessages -l ru -i venv | python manage.py makemessages -l en -i venv
# Затем
# python manage.py compilemessages -i venv

LOCALE_PATHS = [
    os.path.join(BASE_DIR, "locale"),
]

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = "/static/"

# Add these new lines
STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),)

STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

FILE_UPLOAD_HANDLERS = [
    "django.core.files.uploadhandler.TemporaryFileUploadHandler",
]

DATE_INPUT_FORMATS = ("%d/%m/%Y", "%d-%m-%Y", "%d.%m.%Y")

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

LOGIN_REDIRECT_URL = "/"
LOGIN_URL = "/login"

FIXTURE_DIRS = (os.path.join(BASE_DIR, "app_import/fixtures"),)

# ROSETTA SETTINGS
ROSETTA_MESSAGES_PER_PAGE = 500

# WORK WITH CART
CART_SESSION_ID = "cart"

# DATABASE JSON COMMAND - выпол
# python -Xutf8 manage.py dumpdata --natural-foreign --natural-primary -e contenttypes -e auth.Permission -o .\app_import\fixtures\all_data.json

# LOCALES MAKE MESSAGES COMMAND
# python manage.py makemessages -l ru -i venv | python manage.py makemessages -l en -i venv
