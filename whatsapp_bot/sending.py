import requests

def trigger_text_api(text):
    url = "http://127.0.0.1:8000/proxy_text_api/"  # adjust path if needed
    
    response = requests.post(
        url,
        json={"text": text},
        timeout=30
    )

    response.raise_for_status()
    return response.json()
