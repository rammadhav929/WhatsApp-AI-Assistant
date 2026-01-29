import requests
import os
with open("/etc/secrets/ACCESS_TOKEN") as f:
    ACCESS_TOKEN = f.read().strip()

if not ACCESS_TOKEN:
    raise RuntimeError("api_key file is empty")
#ACCESS_TOKEN= os.getenv("/etc/secrets/ACCESS_TOKEN") 

with open("/etc/secrets/PHONE_NUMBER_ID") as f:
    PHONE_NUMBER_ID  = f.read().



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
    #print(response.status_code, response.text)
