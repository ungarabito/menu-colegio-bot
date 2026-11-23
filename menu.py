import os
import fitz
import requests

token = os.environ["TELEGRAM_TOKEN"]
chat_id = os.environ["TELEGRAM_CHAT_ID"]

pdf_file = "menu_actual.pdf"

texto = ""

pdf = fitz.open(pdf_file)

for pagina in pdf:
    texto += pagina.get_text()

pdf.close()

mensaje = texto[:3000]

requests.post(
    f"https://api.telegram.org/bot{token}/sendMessage",
    json={
        "chat_id": chat_id,
        "text": mensaje
    }
)

print("PDF procesado correctamente")
