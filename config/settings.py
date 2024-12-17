# Imports
from pathlib import Path

import environ

# Base directory of the Django project
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent

# App directory of the Django project
APPS_DIR = BASE_DIR / "apps"

# Initialize environment variables
env = environ.Env()

# Read the environment variables from the .env file
READ_DOT_ENV_FILE = env.bool(var="DJANGO_READ_DOT_ENV_FILE", default=False)
if READ_DOT_ENV_FILE:
    env.read_env(str(BASE_DIR / ".env"))

# General
# ------------------------------------------------------------------------------
DEBUG = env.bool(var="DJANGO_DEBUG", default=False)
SECRET_KEY = env.str(
    var="DJANGO_SECRET_KEY",
    default="&j5+b5hje=q_k*=(_1q+yg))f2q4=e=12b@#-0hz2nipu%zv%y74!vws_$-ohn-oga10pq)15=l!8ef9b7m3x#0mw0fq28-$om95",
)
ALLOWED_HOSTS = env.list(var="DJANGO_ALLOWED_HOSTS", default=["127.0.0.1"])
CSRF_TRUSTED_ORIGINS = env.list(
    var="DJANGO_CSRF_TRUSTED_ORIGINS",
    default=["http://127.0.0.1:8000", "https://127.0.0.1:8000"],
)

# Site settings
# ------------------------------------------------------------------------------
SITE_ID = 1
SITE_NAME = env.str(var="SITE_NAME", default="Finance Tracker")

# Internationalization
# ------------------------------------------------------------------------------
TIME_ZONE = "Asia/Kolkata"
LANGUAGE_CODE = "en-us"
USE_I18N = True
USE_TZ = True

# Django debug toolbar
# ------------------------------------------------------------------------------
INTERNAL_IPS = env.list(var="DJANGO_INTERNAL_IPS", default=["127.0.0.1"])

# Databases
# ------------------------------------------------------------------------------
DATABASES = {"default": env.db(var="DATABASE_URL", default="sqlite:///db.sqlite3")}
DATABASES["default"]["ATOMIC_REQUESTS"] = True
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Urls
# ------------------------------------------------------------------------------
ROOT_URLCONF = "config.urls"
WSGI_APPLICATION = "config.wsgi.application"

# Apps
# ------------------------------------------------------------------------------
DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
    "django.forms",
]
THIRD_PARTY_APPS = [
    "corsheaders",
    "phonenumber_field",
    "allauth",
    "allauth.account",
    "debug_toolbar",
    "django_extensions",
    "django_filters",
    "widget_tweaks",
]
LOCAL_APPS = []
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

# Authentication
# ------------------------------------------------------------------------------
AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
]

# Passwords
# ------------------------------------------------------------------------------
PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.Argon2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
    "django.contrib.auth.hashers.BCryptSHA256PasswordHasher",
]
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# Middleware
# ------------------------------------------------------------------------------
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "allauth.account.middleware.AccountMiddleware",
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

# Templates
# ------------------------------------------------------------------------------
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [str(APPS_DIR / "static")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                "django.template.context_processors.tz",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# Security
# ------------------------------------------------------------------------------
SESSION_COOKIE_HTTPONLY = True
CSRF_COOKIE_HTTPONLY = True
X_FRAME_OPTIONS = "DENY"

# Admin
# ------------------------------------------------------------------------------
ADMIN_URL = "admin/"

# Logging
# ------------------------------------------------------------------------------
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s",
        },
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        },
    },
    "root": {"level": "INFO", "handlers": ["console"]},
}

# Django CORS Headers
# -------------------------------------------------------------------------------
CORS_URLS_REGEX = r"^/api/.*$"

# Caches
# ------------------------------------------------------------------------------
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
        "LOCATION": BASE_DIR / ".cache",
    },
}

# Static files settings
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "static"
STATICFILES_DIRS = [str(APPS_DIR / "static")]

# Media files settings
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"
