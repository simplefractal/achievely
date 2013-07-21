import dj_database_url

PRODUCTION = True

DATABASES = {'default': dj_database_url.config(default='postgres://localhost')}

DEBUG = False

MEDIA_URL = 'http://s3.amazonaws.com/betterme/'
