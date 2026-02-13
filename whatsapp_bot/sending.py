import requests

def trigger(text):
    url = "http://172.19.128.1:8000/api/text/"  # adjust path if needed
    
    response = requests.post(
        url,
        json={"text": text},
        timeout=150
    )

    response.raise_for_status()
    res=response.json()
    return res['result']

