from hsl import Hsl
from make_img_of_scheme import img

'''
I used this http://www.tigercolor.com/color-lab/color-theory/color-theory-intro.htm really helpful site
to figure out a bunch of stuff with this project
'''

"""
The code bellow is really ugly and poorly written. Im going to wrewrite it once I have a clearer image of
what I want/need to do. Regardless the code still shows the operations that need to be perormed on
the hues to get the right color
"""

class Generate:

    def __init__(self):
        pass

        '''
            There needs to be a way to specify if you want to keep the saturation and lightness
            or just use normal values ie 100 and 50.

            There also should be a way to specify if you want to use actual color values or perceived ones
            if that important. Idk how that really works.
        '''

    def complementary(self, color):
        new_color = Hsl(h=color.h + 180, s=color.s, l=color.l)
        return color, new_color

    def monochromatic(self, color, amount_of_colors):
        new_colors = []

        for i in range(amount_of_colors):
            new_colors.append(
                Hsl(
                    h=color.h, s=color.s, l=int(color.l - (color.l/amount_of_colors) * i)
                ))

        return new_colors

    def _loop_around_three_sixty(self, hue):
        if hue < 0:
            return 360 - hue
        else:
            return hue

    def analogous(self, color, degree_dif=45):
        return [
            Hsl(h=self._loop_around_three_sixty(color.h - degree_dif), s=color.s, l=color.l),
            color,
            Hsl(h=color.h + degree_dif, s=color.s, l=color.l)
        ]

    def triadic(self, color):
        # 120 is a third of the color wheel
        return [
            Hsl(h=self._loop_around_three_sixty(color.h - 120), s=color.s, l=color.l),
            color,
            Hsl(h=color.h + 120, s=color.s, l=color.l)
        ]

    def split_complementary(self, color):
        # takes complementary color and finds the two other colors next to it
        return [
            color,
            Hsl(h=self._loop_around_three_sixty(color.h + 180 - 45), s=color.s, l=color.l),
            Hsl(h=self._loop_around_three_sixty(color.h + 180 + 45), s=color.s, l=color.l)
        ]

    def square(self, color):
        return [
            color,
            Hsl(h=self._loop_around_three_sixty(color.h + 90), s=color.s, l=color.l),
            Hsl(h=self._loop_around_three_sixty(color.h + 180), s=color.s, l=color.l),
            Hsl(h=self._loop_around_three_sixty(color.h - 90), s=color.s, l=color.l)
        ]

if __name__ == '__main__':
    import os

    def format_examples_path(file_name):
        return os.path.abspath('examples/') + '/' + file_name

    for i in range(60):
        sc_complementary = Generate().complementary(Hsl(h=i*6, s=100, l=50))
        img(sc_complementary, format_examples_path('complementary/{}.png'.format(str(i).zfill(3))))

    for i in range(60):
        sc_monochromatic = Generate().monochromatic(Hsl(h=i*6, s=100, l=50), amount_of_colors=10)
        img(sc_monochromatic, format_examples_path('monochromatic/{}.png'.format(str(i).zfill(3))))


    for i in range(60):
        sc_analogous = Generate().analogous(Hsl(h=i*6, s=100, l=50))
        img(sc_analogous, format_examples_path('analogous/{}.png'.format(str(i).zfill(3))))


    for i in range(60):
        sc_triadic = Generate().triadic(Hsl(h=i*6, s=100, l=50))
        img(sc_triadic, format_examples_path('triadic/{}.png'.format(str(i).zfill(3))))

    for i in range(60):
        starting_color = Hsl(h=i*6, s=100, l=50)
        sc_split_complementary = Generate().split_complementary(starting_color)
        img(sc_split_complementary, format_examples_path('split_complementary/{}.png'.format(str(i).zfill(3))))

    for i in range(60):
        sc_square = Generate().square(Hsl(h=i * 6, s=100, l=50))
        img(sc_square, format_examples_path('square/{}.png'.format(str(i).zfill(3))))

    '''
    After these go throw I run this commmand  convert   -delay 20   -loop 0   sphere*.gif   animatespheres.gif
    which I got from https://www.tjhsst.edu/~dhyatt/supercomp/n401a.html
    '''

