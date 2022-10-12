from PIL import Image, ImageDraw, ImageFont


def create_img(text, date):
    img = Image.new('RGB', (1000, 1000), color=(250, 250, 250))
    fnt = ImageFont.truetype("C:/Windows/Fonts/AGENCYB.TTF", 50)
    d = ImageDraw.Draw(img)
    d.text((100, 100), text, font=fnt, fill=(0, 0, 0))
    img_name = f'Pedido_{date}.png'
    img.save(img_name)
    return img_name
