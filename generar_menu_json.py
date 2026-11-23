import json
import re
import fitz

pdf = fitz.open("menu_actual.pdf")

texto = ""

for pagina in pdf:
    texto += pagina.get_text() + "\n"

pdf.close()

# Limpiar espacios
texto = re.sub(r"\r", "", texto)

lineas = [
    linea.strip()
    for linea in texto.splitlines()
    if linea.strip()
]

menus = {}

i = 0

while i < len(lineas):

    if re.fullmatch(r"\d{1,2}", lineas[i]):
        dia = lineas[i]

        bloque = []
        i += 1

        while (
            i < len(lineas)
            and not re.fullmatch(r"\d{1,2}", lineas[i])
        ):
            bloque.append(lineas[i])
            i += 1

        menus[dia] = bloque

        continue

    i += 1

with open(
    "menu_raw.json",
    "w",
    encoding="utf-8"
) as f:
    json.dump(
        menus,
        f,
        indent=2,
        ensure_ascii=False
    )

print(f"Generados {len(menus)} días")
