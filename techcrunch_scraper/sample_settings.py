# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ''

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# CELERY RABBIT MQ URL
CELERY_BROKER_URL= 'amqp://user:pass@IP_ADDRESS'

# https://docs.celeryq.dev/en/latest/userguide/configuration.html#conf-result-backend
CELERY_RESULT_BACKEND = 'django-db'
CELERY_CACHE_BACKEND = 'django-cache'