# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-75v48b4yjgpnp-4_!h3&hocoo&a0i5)7p!*cr2(%wvnuod-qz+'



# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME':'product_database',
        'HOST': 'localhost',
        'USER':'root',
        'PASSWORD': 'password'
    }
}