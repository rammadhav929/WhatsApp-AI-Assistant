import json
#Ram
Ram ="!"
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .send import send_whatsapp_message
# from .bot import talk
from .sending import trigger
import os

VERIFY_TOKEN = os.getenv("VERIFY_TOKEN")  # same value you put in Meta dashboard
@csrf_exempt
def whatsapp_webhook(request):

    # Meta verification (GET from Meta)
    if request.method == "GET":
        mode = request.GET.get("hub.mode")
        token = request.GET.get("hub.verify_token")
        challenge = request.GET.get("hub.challenge")

        if mode == "subscribe" and token == VERIFY_TOKEN:
            return HttpResponse(challenge)

        return HttpResponse("WhatsApp Webhook is running.")


    # Receive messages (POST from Meta)
    if request.method == "POST":

        # 🔎 LOG REQUEST SOURCE
        client_ip = request.META.get("REMOTE_ADDR")
        forwarded_ip = request.META.get("HTTP_X_FORWARDED_FOR")
        user_agent = request.META.get("HTTP_USER_AGENT")
        signature = request.META.get("HTTP_X_HUB_SIGNATURE_256")

        print("---- NEW POST RECEIVED ----", flush=True)
        print("Client IP:", client_ip, flush=True)
        print("Forwarded IP:", forwarded_ip, flush=True)
        print("User-Agent:", user_agent, flush=True)
        print("Meta Signature:", signature, flush=True)

        data = json.loads(request.body)

        try:
            msg = data["entry"][0]["changes"][0]["value"]["messages"][0]
            user_number = msg["from"]
            user_text = msg["text"]["body"]

            print("From:", user_number, flush=True)
            print("Text:", user_text, flush=True)

            text = trigger(user_text)

            send_whatsapp_message(
                user_number,
                text,
                use_template=False
            )

        except KeyError:
            print("Non-message event received", flush=True)

        return JsonResponse({"status": "ok"})
