import pywhatkit
from datetime import datetime, timedelta
from create_file import create_file
from get_pedido_content import get_pedido_content
from get_products import get_products
from create_image import create_img
from reformat_fimg import format_img


path = "C:/Users/wilye/Downloads/Orden .pdf"
text = get_pedido_content(path)
file = open(create_file(text, "txt"))
pedido = get_products(file)  # Texto para imagen sin formato(guiones y flecha)
pedido_img = format_img(pedido)  # Texto para imagen con formato(guiones y flecha)
create_file(pedido, "csv")
create_file(pedido, "txt")
print(pedido_img)

presentday = datetime.now()
tomorrow = presentday + timedelta(2)
dia = presentday.strftime('%Y-%m-%d')
print(dia)
img = create_img(pedido_img, dia)

group_id = "L0s12WLZdW5D98LLWKhXtd"
# group_id = "Hf98n4Bc6eg47NB1XHFEgh"
pywhatkit.sendwhats_image(group_id, img, dia, 10, True, 5)
