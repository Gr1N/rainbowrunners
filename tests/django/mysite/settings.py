SECRET_KEY = 'SECRET_KEY'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
    }
}

TEST_RUNNER = 'rainbowrunners.djrunner.NyanCatDiscoverRunner'
