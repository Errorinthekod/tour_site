import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import requests

@csrf_exempt
def telegram_webhook(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            chat_id = data['message']['chat']['id']
            text = data['message'].get('text', '')

            # Пример ответа пользователю
            reply_text = f"Вы написали: {text}"
            send_message_url = f"https://api.telegram.org/bot{settings.TELEGRAM_BOT_TOKEN}/sendMessage"
            requests.post(send_message_url, json={
                'chat_id': chat_id,
                'text': reply_text,
            })

        except Exception as e:
            print("Error handling webhook:", e)
        return JsonResponse({"ok": True})
    return JsonResponse({"ok": False}, status=405)
