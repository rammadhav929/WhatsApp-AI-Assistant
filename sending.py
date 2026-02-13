import json
import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

PUBLIC_API_URL = "http://127.0.0.1:8000/api/text/"


@csrf_exempt
def proxy_text_api(request):
    if request.method != "POST":
        return JsonResponse(
            {"error": "POST method required"},
            status=405
        )

    try:
        data = json.loads(request.body)
        input_text = data.get("text")

        if not input_text:
            return JsonResponse(
                {"error": "Text field is required"},
                status=400
            )

        # Call external API
        external_response = requests.post(
            PUBLIC_API_URL,
            json={"text": input_text},
            timeout=160
        )

        external_response.raise_for_status()

        return JsonResponse(external_response.json())

    except json.JSONDecodeError:
        return JsonResponse(
            {"error": "Invalid JSON"},
            status=400
        )

    except requests.exceptions.RequestException as e:
        return JsonResponse(
            {"error": "External API call failed", "details": str(e)},
            status=502
        )
