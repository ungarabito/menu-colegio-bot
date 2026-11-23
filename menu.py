import os
import requests

token = os.environ["TELEGRAM_TOKEN"]
chat_id = os.environ["TELEGRAM_CHAT_ID"]

mensaje = """
🍽️ Bot del menú funcionando correctamente.

Prueba enviada desde GitHub Actions.
"""

response = requests.post(
    f"https://api.telegram.org/bot{token}/sendMessage",
    json={
        "chat_id": chat_id,
        "text": mensaje
    }
)

print(response.status_code)
print(response.text)