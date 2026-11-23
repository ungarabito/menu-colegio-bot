import json
import os
from datetime import datetime

import requests

token = os.environ["TELEGRAM_TOKEN"]
chat_id = os.environ["TELEGRAM_CHAT_ID"]

dia = str(datetime.now().day)

with open("menu.json", encoding="utf-8") as f:
    menus = json.load(f)

if dia in menus:
    menu = menus[dia]

    mensaje = f"""🍽️ Menú del día {dia}

🥗 {menu['primero']}

🍖 {menu['segundo']}

🍎 {menu['postre']}
"""
else:
    mensaje = f"No hay menú para el día {dia}"

requests.post(
    f"https://api.telegram.org/bot{token}/sendMessage",
    json={
        "chat_id": chat_id,
        "text": mensaje
    }
)

print(mensaje)
