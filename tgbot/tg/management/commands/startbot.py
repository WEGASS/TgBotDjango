from django.core.management.base import BaseCommand
from tg.bot.bot import start_bot

class Command(BaseCommand):
    def handle(self, *args, **options):
        start_bot()
