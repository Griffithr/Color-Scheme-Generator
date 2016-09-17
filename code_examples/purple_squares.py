from PIL import Image, ImageDraw
from generate_scheme import Generate, Hsl
from random import randrange

PURPLE = 268

im = Image.new('RGB', (1000, 1000))
draw = ImageDraw.Draw(im, 'RGB')

start_color = Hsl(h=268, s=100, l=50)
colors = Generate().split_complementary(start_color)
print([i.pillow_format() for i in colors])

draw.rectangle([(0, 0), (1000, 1000)], fill='white')
draw.rectangle([(250, 250), (750, 750)], fill=start_color.pillow_format())

top_left = randrange(0, 800)
size = randrange(100, 400)
draw.rectangle([(top_left, top_left), (top_left + size, top_left + size)], colors[0].pillow_format())

top_left = randrange(0, 800)
size = randrange(100, 400)
draw.rectangle([(top_left, top_left), (top_left + size, top_left + size)], colors[1].pillow_format())

del draw
im.save('purple_squares.png')

