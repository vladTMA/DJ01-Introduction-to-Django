# MyDJProdj/MyDJProdj/settings_local.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3',  # старая база
    },
    'newdb': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': r'D:\Python projects\DJ\db.sqlite3', # найденная база с книгами
    }
}

TEST_FLAG = True