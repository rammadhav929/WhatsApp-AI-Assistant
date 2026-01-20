import requests

VERIFY_TOKEN = "my_verify_token"
ACCESS_TOKEN = "ZA"
PHONE_NUMBER_ID = ""
BOT_URL = "http://127.0.0.1:8000/reply"  # <-- Put your bot endpoint here

def send_whatsapp_message(to, text, use_template=False):
    url = f"https://graph.facebook.com/v22.0/{PHONE_NUMBER_ID}/messages"

    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }

    if use_template:
        payload = {
            "messaging_product": "whatsapp",
            "to": to,
            "type": "template",
            "template": {
                "name": "hello_world",
                "language": {"code": "en_US"}
            }
        }
    else:
        payload = {
            "messaging_product": "whatsapp",
            "to": to,
            "text": {"body": text}
        }

    response = requests.post(url, headers=headers, json=payload)
    print(response.status_code, response.text)
