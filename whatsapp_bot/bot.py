from google import genai

import os

api_key= os.getenv("/etc/secrets/api_key") 
client = genai.Client(api_key=api_key)

SYSTEM_PROMPT = (
    "You are a helpful assistant. "
    "Always reply in a maximum of 2 short lines. "
    "Be clear, polite, and concise. "
    "Do not use emojis. Do not exceed two lines."
)



name="Hello Ram How can i help you"
def talk(user_text):
    prompt = f"{SYSTEM_PROMPT}\nUser: {user_text}"
    response = client.models.generate_content(
    model="gemini-2.5-flash-lite", 
    contents=prompt
) 
    reply = response.text
    return reply
    #print(reply)
