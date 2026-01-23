import json
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .send import send_whatsapp_message
from .bot import talk
import os

VERIFY_TOKEN = os.getenv("VERIFY_TOKEN")  # same value you put in Meta dashboard

@csrf_exempt
def whatsapp_webhook(request):
    # Meta verification (GET from Meta)
    if request.method == "GET":
        mode = request.GET.get("hub.mode")
        token = request.GET.get("hub.verify_token")
        challenge = request.GET.get("hub.challenge")

        # When Meta verifies
        if mode == "subscribe" and token == VERIFY_TOKEN:
            return HttpResponse(challenge)

        # When YOU open the URL in browser
        return HttpResponse("WhatsApp Webhook is running.")

    # Receive messages (POST from Meta)
    if request.method == "POST":
        data = json.loads(request.body)

        try:
            msg = data["entry"][0]["changes"][0]["value"]["messages"][0]
            user_number = msg["from"]
            user_text = msg["text"]["body"]

            print("From:", user_number)
            print("Text:", user_text)
            #user_text=user_text+" "+user_number
            text=talk(user_text)

            '''send_whatsapp_message(
                user_number,
                text,
                use_template=False
            )'''

        except KeyError:
            pass  # non-message events

        return JsonResponse({"status": "ok"})

