from PIL import Image, ImageDraw

def img(colors, dif=30):
    amount_of_colors = len(colors)
    y = 100
    x = 100 * amount_of_colors

    im = Image.new('RGB', (x, y))
    draw = ImageDraw.Draw(im, 'RGB')

    draw.rectangle([(0, 0), (x, y)], fill='white')


    for i, cl in enumerate(colors):
        draw.rectangle([(i * 100, 0), ((i+1) * 100, 100)], fill=cl)
    # [ (i* 100, 0), ((i+1) * 100, 100)]

    del draw
    im.save('tst.png')

img(['red', 'green', 'blue', 'pink'])