from django.db import models

# Create your models here.

class Profile(models.Model):
    external_id = models.IntegerField(
        verbose_name='Telegram ID'
    )

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

    def __str__(self):
        return f'{self.external_id}'


class UserData(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.PROTECT, verbose_name='Профиль')
    age = models.PositiveIntegerField(verbose_name='Возраст',  blank=True, null=True)
    birthplace = models.TextField(verbose_name='Место рождения',  blank=True, null=True)

    class Meta:
        verbose_name = 'Ответы пользователя'
        verbose_name_plural = 'Ответы пользователей'

    def __str__(self):
        return f'{self.profile}'


class Questions(models.Model):
    title = models.CharField(max_length=50)
    question_text = models.TextField()

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'


class BotHelpMessage(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField()
