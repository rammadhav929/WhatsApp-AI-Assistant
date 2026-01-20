from google import genai


client = genai.Client(api_key="AIzaSyBhj7_xb7qW_nTAFLgpJGuEgVJ8vw55TLI")

SYSTEM_PROMPT = (
    "You are a helpful assistant. "
    "Always reply in a maximum of 2 short lines. "
    "Be clear, polite, and concise. "
    "Do not use emojis. Do not exceed two lines."
)



name="Hello Ram How can i help you"
def take(user_text):
    prompt = f"{SYSTEM_PROMPT}\nUser: {user_text}"
    response = client.models.generate_content(
    model="gemini-2.5-flash-lite", 
    contents=prompt
) 
    reply = response.text
    #print(reply)
