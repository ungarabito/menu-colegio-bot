import os
import re
from datetime import datetime

import fitz
import requests

token = os.environ["TELEGRAM_TOKEN"]
chat_id = os.environ["TELEGRAM_CHAT_ID"]

# Leer PDF
texto = ""

pdf = fitz.open("menu_actual.pdf")

for pagina in pdf:
    texto += pagina.get_text() + "\n"

pdf.close()

# Día actual
dia = datetime.now().day

# Buscar desde el día actual hasta el siguiente día
patron = rf"\b{dia}\b(.*?)(?=\n(?:{dia+1})\b|\Z)"

m = re.search(patron, texto, re.DOTALL)

if m:
    menu = m.group(1).strip()
else:
    menu = "No se ha encontrado el menú para hoy."

mensaje = f"🍽️ Menú del día {dia}\n\n{menu}"

requests.post(
    f"https://api.telegram.org/bot{token}/sendMessage",
    json={
        "chat_id": chat_id,
        "text": mensaje[:4000]
    }
)

print("Mensaje enviado")
