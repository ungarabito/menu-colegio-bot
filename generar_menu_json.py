import json
import fitz
import re

pdf = fitz.open("menu_actual.pdf")

texto = ""

for pagina in pdf:
    texto += pagina.get_text() + "\n"

pdf.close()

lineas = [
    l.strip()
    for l in texto.splitlines()
    if l.strip()
]

menus = {}

dias_semana = [
    "LUNES",
    "MARTES",
    "MIÉRCOLES",
    "MIERCOLES",
    "JUEVES",
    "VIERNES"
]

for i in range(len(lineas) - 2):

    linea = lineas[i]

    patron = r"^(LUNES|MARTES|MIÉRCOLES|MIERCOLES|JUEVES|VIERNES)\s+(\d+)$"

    m = re.match(patron, linea)

    if m:
        dia = m.group(2)

        primero = lineas[i + 1]
        segundo = lineas[i + 2]

        menus[dia] = {
            "primero": primero,
            "segundo": segundo
        }

with open(
    "menu.json",
    "w",
    encoding="utf-8"
) as f:
    json.dump(
        menus,
        f,
        indent=2,
        ensure_ascii=False
    )

print(json.dumps(menus, indent=2, ensure_ascii=False))
