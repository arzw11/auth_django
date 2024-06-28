# Authentication Django 5
Авторизация на Django. Восстановление пароля по E-mail. Вход в профиль по логину или E-mail.

# Технологии
- [Python 3.11](https://www.python.org/)
- [Django 5.0](https://www.djangoproject.com/)

# settings.py
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'users.authentication.EmailAuthBackend',
]

LOGIN_URL = 'users:login'
LOGIN_REDIRECT_URL = 'users:profile'
LOGOUT_REDIRECT_URL = 'users:login'

AUTH_USER_MODEL = 'users.User'

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
