from datetime import datetime

from django.db import models

# Create your models here.


class User(models.Model):
    """Пользователи"""
    user_id = models.BigAutoField('id', primary_key=True)
    email = models.EmailField("Почта", max_length=50, unique=True)
    username = models.CharField("Имя", max_length=25)
    nickname = models.CharField("Никнейм", max_length=30)
    password = models.TextField("Пароль")
    date = models.DateTimeField("Дата регистарции", default=datetime)

    def __str__(self):
        """Возвращает строковое значение"""
        return self.username


class Auth(models.Model):
    """Токены доступа"""
    token_id = models.BigAutoField('id', primary_key=True)
    token = models.CharField("Токен", max_length=50)
    username_id = models.OneToOneField(User, related_name='id', on_delete=models.CASCADE)
    date = models.DateTimeField("Дата генерации", default=datetime)
