from PIL import Image, ImageDraw


def img(colors, fl_name):
    colors_in_scheme = len(colors)
    y = 100
    x = 100 * colors_in_scheme

    im = Image.new('RGB', (x, y))
    draw = ImageDraw.Draw(im, 'RGB')

    draw.rectangle([(0, 0), (x, y)], fill='white')

    for i, cl in enumerate(colors):
        draw.rectangle([(i * 100, 0), ((i+1) * 100, 100)], fill=cl.pillow_format())

    del draw
    im.save(fl_name)

