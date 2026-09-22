import requests
import json

def emotion_detector(text_to_analyze):
    # Endpoint de Watson NLP (ajusta con tu URL real)
    url = "https://api.us-south.natural-language-understanding.watson.cloud.ibm.com/instances/TU_INSTANCIA/v1/analyze"
    headers = {"Content-Type": "application/json"}
    payload = json.dumps({
        "text": text_to_analyze,
        "features": {
            "emotion": {}
        }
    })

    # Autenticación con tu API Key
    response = requests.post(url, headers=headers, data=payload, auth=('apikey', 'TU_API_KEY'))

    if response.status_code == 200:
        emotions = response.json()["emotion"]["document"]["emotion"]
        # ✅ Devuelve las emociones principales en formato diccionario
        return {
            "anger": emotions["anger"],
            "disgust": emotions["disgust"],
            "fear": emotions["fear"],
            "joy": emotions["joy"],
            "sadness": emotions["sadness"]
        }
    else:
        return {"error": f"Error en la solicitud: {response.status_code}"}
