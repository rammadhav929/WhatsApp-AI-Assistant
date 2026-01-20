import requests

VERIFY_TOKEN = "my_verify_token"
ACCESS_TOKEN = "EAAQHhYsOVzsBQtplGQlEA6ZAvYYGkPuCpJS8AGuE60hMHcFeWD2vkuXT7WLNopZAfPUlbe1Xz78vfOBZBb2JYAvPvWyB6e9ZAqMZAicdPy8RnKYa7FVLmheS5JsWrA6rURO81QgCSKZBLZBucsTiiQ6VaDkZAgdRksHtqRsQK711AtqmYeENKqOqlEKySTpfWd2yVRCYzjWptC46I2ILvpPpbx1GmOZCfG5zAW2cC1Omu3TFt6SZBNlf9WXhoWGZBnYjfDJMsd8niy4ZB0wM2wx1RF8c4w3G"
PHONE_NUMBER_ID = "894423013757849"
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
    #print(response.status_code, response.text)
