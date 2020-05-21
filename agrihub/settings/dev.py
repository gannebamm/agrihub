from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '%$64b9kzz9)vfj%y9%d_=93a#8lvg5-s&y1(+^r2d0i4_vb!mb'

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['*'] 

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# DJANGO DEBUG TOOLBAR
INSTALLED_APPS = INSTALLED_APPS + [
    'debug_toolbar'
]
MIDDLEWARE = MIDDLEWARE + [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]
INTERNAL_IPS = [
    # ...
    '127.0.0.1',
    'localhost',
    # ...
]

try:
    from .local import *
except ImportError:
    pass
