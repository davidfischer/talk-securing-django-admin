from .base import *  # noqa

import environ


# Django will fail to start if these production settings are used
# unless values for the following settings are provided in environment variables:
#
# - SECRET_KEY
# - ALLOWED_HOSTS
env = environ.Env()


# A lot of Django's security depends on your SECRET_KEY
# including sessions and password reset tokens
SECRET_KEY = env("SECRET_KEY")

# Django reveals a lot of information that would be useful to an attacker in DEBUG=True
# This includes the most of the settings
# If a traceback can be triggered, even more information is revealed.
DEBUG = False
TEMPLATE_DEBUG = DEBUG

# Important to fully utilize Django's CSRF protection
ALLOWED_HOSTS = env.list("ALLOWED_HOSTS")

# Whether the admin should be enabled
ADMIN_ENABLED = env.bool("ADMIN_ENABLED", default=True)
# The URL where the admin should be available
ADMIN_URL = env("ADMIN_URL", default="admin")


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases
# --------------------------------------------------------------------------

DATABASES = {
    "default": env.db()  # Raises ImproperlyConfigured exception if DATABASE_URL not set
}


# Security
# https://docs.djangoproject.com/en/2.2/topics/security/
# --------------------------------------------------------------------------

SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_HSTS_SECONDS = 60 * 60 * 24 * 365  # 1 year minimum is recommended: 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

SECURE_SSL_REDIRECT = True
# This setting depends on your load balancer settings
# SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
