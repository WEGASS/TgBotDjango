from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'external_id')


@admin.register(UserData)
class UserDataAdmin(admin.ModelAdmin):
    list_display = ('id', 'profile', 'age', 'birthplace')


@admin.register(Questions)
class QuestionsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'question_text')


@admin.register(BotHelpMessage)
class BotHelpMessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'title','text')