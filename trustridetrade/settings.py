
from decouple import config,Csv
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = 'django-insecure-$*=5k5p8mlr0r3bxk7rc^8jbyiy)^vkie3ecdxocsa2sq!4x=j'

DEBUG = True

ALLOWED_HOSTS = ["*"]


INSTALLED_APPS = [
    'versatileimagefield',
    'tinymce',


    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',


    'web',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'trustridetrade.urls'



VERSATILEIMAGEFIELD_SETTINGS = {
   
    'cache_length': 2592000,
   
    'cache_name': 'versatileimagefield_cache',
    
    'jpeg_resize_quality': 70,
    
    'sized_directory_name': '__sized__',
   
    'filtered_directory_name': '__filtered__',
    
    'placeholder_directory_name': '__placeholder__',
   
    'create_images_on_demand': True,
    
    'image_key_post_processor': None,
    
    'progressive_jpeg': False
}


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'trustridetrade.wsgi.application'




DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}




AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]



LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True




MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
STATIC_URL = '/static/'
STATIC_FILE_ROOT = BASE_DIR / 'static'
STATICFILES_DIRS = ((BASE_DIR / 'static'),)

STATIC_ROOT = BASE_DIR / 'assets'



DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
