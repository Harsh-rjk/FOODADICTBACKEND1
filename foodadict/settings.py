"""
Django settings for foodadict project
Production-ready (Render + PostgreSQL + Cloudinary)
"""

from pathlib import Path
import os
import environ
import cloudinary
import cloudinary.uploader
import cloudinary.api

# -------------------------------------------------------------------
# BASE DIR
# -------------------------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

# -------------------------------------------------------------------
# ENV
# -------------------------------------------------------------------
env = environ.Env(
    DEBUG=(bool, False)
)

environ.Env.read_env(os.path.join(BASE_DIR, ".env"))

# -------------------------------------------------------------------
# SECURITY
# -------------------------------------------------------------------
SECRET_KEY = env("SECRET_KEY")

DEBUG = env.bool("DEBUG", default=False)

ALLOWED_HOSTS = env.list(
    "ALLOWED_HOSTS",
    default=["localhost", "127.0.0.1"]
)

# -------------------------------------------------------------------
# APPS
# -------------------------------------------------------------------
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Third-party
    'rest_framework',
    'corsheaders',
    'cloudinary',
    'cloudinary_storage',

    # Local apps
    'Account',
    'items',
    'orders',
]

# -------------------------------------------------------------------
# MIDDLEWARE
# -------------------------------------------------------------------
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'corsheaders.middleware.CorsMiddleware',

    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_CREDENTIALS = True

# -------------------------------------------------------------------
# URLS / WSGI
# -------------------------------------------------------------------
ROOT_URLCONF = 'foodadict.urls'
WSGI_APPLICATION = 'foodadict.wsgi.application'

# -------------------------------------------------------------------
# TEMPLATES
# -------------------------------------------------------------------
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# -------------------------------------------------------------------
# DATABASE (POSTGRES)
# -------------------------------------------------------------------
DATABASES = {
    'default': env.db()
}

# -------------------------------------------------------------------
# PASSWORD VALIDATORS
# -------------------------------------------------------------------
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# -------------------------------------------------------------------
# I18N
# -------------------------------------------------------------------
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# -------------------------------------------------------------------
# STATIC FILES (WhiteNoise)
# -------------------------------------------------------------------
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

STATICFILES_STORAGE = (
    "whitenoise.storage.CompressedManifestStaticFilesStorage"
)

# -------------------------------------------------------------------
# MEDIA (Cloudinary)
# -------------------------------------------------------------------
DEFAULT_FILE_STORAGE = (
    "cloudinary_storage.storage.MediaCloudinaryStorage"
)

MEDIA_URL = "/media/"

cloudinary.config(
    cloud_name=env("CLOUDINARY_CLOUD_NAME"),
    api_key=env("CLOUDINARY_API_KEY"),
    api_secret=env("CLOUDINARY_API_SECRET"),
    secure=True,
)

# -------------------------------------------------------------------
# DJANGO REST FRAMEWORK
# -------------------------------------------------------------------
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ]
}

# -------------------------------------------------------------------
# CSRF
# -------------------------------------------------------------------
CSRF_TRUSTED_ORIGINS = [
    "https://foodadictbackend102.onrender.com",
    "http://localhost",
    "http://127.0.0.1",
]

# -------------------------------------------------------------------
# DEFAULT PK
# -------------------------------------------------------------------
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
