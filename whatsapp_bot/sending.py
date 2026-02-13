import requests

def trigger(text):
    url = "http://10.6.21.30:8000/api/text/"  # adjust path if needed
    
    response = requests.post(
        url,
        json={"text": text},
        timeout=150
    )

    response.raise_for_status()
    res=response.json()
    return res['result']


