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
        data = json.loads(request.body)

        try:
            msg = data["entry"][0]["changes"][0]["value"]["messages"][0]
            user_number = msg["from"]
            user_text = msg["text"]["body"]

            print("From:", user_number)
            print("Text:", user_text)
            #user_text=user_text+" "+user_number
            text=talk(user_text)

            send_whatsapp_message(
                user_number,
                text,
                use_template=False
            )

        except KeyError:
            pass  # non-message events

        return JsonResponse({"status": "ok"})



            return HttpResponse("ok")

        except Exception as e:
            LAST_OUTPUT = f"Error: {e}"
            return JsonResponse({"status": "ignored"})
