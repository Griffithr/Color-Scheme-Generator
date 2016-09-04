from PIL import Image, ImageDraw

# just rotate 180 degrees on hue


COLOR_MODE = 'RGB'
im_height = 200
im_width = 200

im_size = (im_height, im_width)

im = Image.new(COLOR_MODE, im_size)

draw = ImageDraw.Draw(im, COLOR_MODE)

draw.rectangle([(0, 0), (200, 200)], fill='black')


for i in range(360):
    hue_val = i

    draw.rectangle([(0, 0), (200, 100)], fill='hsl({}, 80%, 60%)'.format(hue_val))
    draw.rectangle([(0, 100), (200, 200)], fill='hsl({}, 80%, 60%)'.format(hue_val + 180))

    im.save('tst{}.png'.format(str(i).zfill(3)))

'''
img magik
convert -delay 0 -loop 0 *.png animation.gif
'''
del draw

