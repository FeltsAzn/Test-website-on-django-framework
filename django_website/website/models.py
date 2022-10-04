from django.db import models

# Create your models here.


class Cards(models.Model):
    """Карточки данных"""
    category = models.CharField("Категория", max_length=50)
    card_question = models.TextField("Вопрос")
    card_answer = models.TextField("Ответ")
    date = models.DateTimeField("Отложенное время")\

