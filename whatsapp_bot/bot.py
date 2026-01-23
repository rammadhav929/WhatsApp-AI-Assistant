from google import genai

import os
with open("/etc/secrets/api_key") as f:
    api_key = f.read().strip()
print(api_key)

if not api_key:
    raise RuntimeError("api_key file is empty")
'''
#api_key= os.getenv("/etc/secrets/api_key") 
client = genai.Client(api_key=api_key)

SYSTEM_PROMPT = (
    "You are a helpful assistant. "
    "Always reply in a maximum of 2 short lines. "
    "Be clear, polite, and concise. "
    "Do not use emojis. Do not exceed two lines."
)



name="Hello Ram How can i help you"
prompt = f"{SYSTEM_PROMPT}\nUser: {user_text}"
    response = client.models.generate_content(
    model="gemini-2.5-flash-lite", 
    contents=prompt
) 
    reply = response.text
    print(reply)'''
def talk(user_text):
    return api_key
    #print(reply)
