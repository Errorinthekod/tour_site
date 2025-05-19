from django.core.management.base import BaseCommand
import requests
from django.conf import settings


class Command(BaseCommand):
    help = 'Set Telegram webhook'

    def handle(self, *args, **options):
        bot_token = settings.TELEGRAM_BOT_TOKEN
        webhook_url = settings.TELEGRAM_WEBHOOK_URL  # полный URL, например https://example.com/telegram-webhook/

        set_url = f'https://api.telegram.org/bot{bot_token}/setWebhook'
        response = requests.post(set_url, json={'url': webhook_url})

        if response.status_code == 200 and response.json().get("ok"):
            self.stdout.write(self.style.SUCCESS(f'Successfully set webhook: {webhook_url}'))
        else:
            self.stderr.write(self.style.ERROR(f'Failed to set webhook: {response.text}'))
