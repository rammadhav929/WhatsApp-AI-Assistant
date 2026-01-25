import json
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .bot import talk
import os

VERIFY_TOKEN = os.getenv("VERIFY_TOKEN")

# store last output
LAST_OUTPUT = "No messages yet."

@csrf_exempt
def whatsapp_webhook(request):
    global LAST_OUTPUT

    if request.method == "GET":
        return HttpResponse(f"""
            <h2>WhatsApp Webhook is running</h2>
            <p><b>Last Output:</b></p>
            <pre>{LAST_OUTPUT}</pre>
        """)

    if request.method == "POST":
        try:
            data = json.loads(request.body)

            msg = data["entry"][0]["changes"][0]["value"]["messages"][0]
            user_number = msg["from"]
            user_text = msg["text"]["body"]

            text = talk(user_text)

            LAST_OUTPUT = f"From: {user_number}\nUser: {user_text}\nBot: {text}"

            return HttpResponse("ok")

        except Exception as e:
            LAST_OUTPUT = f"Error: {e}"
            return JsonResponse({"status": "ignored"})
