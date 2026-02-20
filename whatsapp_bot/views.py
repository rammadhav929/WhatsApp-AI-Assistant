import json
import os
import hmac
import hashlib

from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .send import send_whatsapp_message
from .sending import trigger


# --------------------------------------------------
# ENV VARIABLES
# --------------------------------------------------
VERIFY_TOKEN = os.getenv("VERIFY_TOKEN")
APP_SECRET = os.getenv("APP_SECRET")  # Meta App Secret (IMPORTANT)


# --------------------------------------------------
# SIGNATURE VERIFICATION (Security Layer)
# Ensures request really came from Meta
# --------------------------------------------------
def verify_signature(payload, received_signature):

    if not received_signature or not APP_SECRET:
        return False

    expected_signature = "sha256=" + hmac.new(
        APP_SECRET.encode(),
        payload,
        hashlib.sha256
    ).hexdigest()

    return hmac.compare_digest(expected_signature, received_signature)


# --------------------------------------------------
# WHATSAPP WEBHOOK
# --------------------------------------------------
@csrf_exempt
def whatsapp_webhook(request):

    # ==============================
    # META VERIFICATION (GET)
    # ==============================
    if request.method == "GET":

        mode = request.GET.get("hub.mode")
        token = request.GET.get("hub.verify_token")
        challenge = request.GET.get("hub.challenge")

        if mode == "subscribe" and token == VERIFY_TOKEN:
            print("Webhook verified by Meta", flush=True)
            return HttpResponse(challenge)

        return HttpResponse("WhatsApp Webhook is running.")


    # ==============================
    # RECEIVE EVENTS (POST)
    # ==============================
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

        # ==============================
        # SECURITY: VERIFY META SIGNATURE
        # ==============================
        if not verify_signature(request.body, signature):
            print("❌ Invalid signature — request rejected", flush=True)
            return JsonResponse({"error": "Invalid signature"}, status=403)

        # ==============================
        # SAFE JSON PARSING
        # ==============================
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            print("❌ Invalid JSON payload", flush=True)
            return JsonResponse({"error": "Invalid JSON"}, status=400)

        # ==============================
        # SAFE DATA EXTRACTION
        # ==============================
        try:
            value = (
                data.get("entry", [{}])[0]
                .get("changes", [{}])[0]
                .get("value", {})
            )

            # ------------------------------
            # MESSAGE EVENT
            # ------------------------------
            if "messages" in value:

                msg = value["messages"][0]

                user_number = msg.get("from")
                message_type = msg.get("type")

                # Accept only text messages
                if message_type != "text":
                    print("Non-text message ignored", flush=True)
                    return JsonResponse({"status": "ignored"})

                user_text = msg.get("text", {}).get("body", "")

                # Input validation
                if not user_number or not user_text:
                    print("Invalid message structure", flush=True)
                    return JsonResponse({"status": "invalid"})

                print("From:", user_number, flush=True)
                print("Text:", user_text, flush=True)

                # ------------------------------
                # BOT PROCESSING
                # ------------------------------
                try:
                    text = trigger(user_text)
                except Exception as e:
                    print("Bot processing error:", str(e), flush=True)
                    return JsonResponse({"status": "bot_error"})

                # ------------------------------
                # SEND REPLY
                # ------------------------------
                send_whatsapp_message(
                    user_number,
                    text,
                    use_template=False
                )

            # ------------------------------
            # STATUS EVENTS (sent/delivered/read)
            # ------------------------------
            else:
                print("Non-message event received", flush=True)

        except Exception as e:
            print("Webhook processing error:", str(e), flush=True)

        return JsonResponse({"status": "ok"})

    # ==============================
    # METHOD NOT ALLOWED
    # ==============================
    return JsonResponse({"error": "Method not allowed"}, status=405)
