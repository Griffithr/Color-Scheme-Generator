from hsl import Hsl
from make_img_of_scheme import img

'''
I used this http://www.tigercolor.com/color-lab/color-theory/color-theory-intro.htm really helpful site
to figure out a bunch of stuff with this project
'''


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


if __name__ == '__main__':
    import os

    def format_examples_path(file_name):
        return os.path.abspath('examples/') + '/' + file_name

    sc_complementary = Generate().complementary(Hsl(h=360, s=100, l=50))
    img(sc_complementary, format_examples_path('complementary.png'))

    sc_monochromatic = Generate().monochromatic(Hsl(h=128, s=100, l=50), amount_of_colors=10)
    img(sc_monochromatic, format_examples_path('monochromatic.png'))

    sc_analogous = Generate().analogous(Hsl(h=20, s=100, l=50))
    img(sc_analogous, format_examples_path('analogous.png'))

    sc_triadic = Generate().triadic(Hsl(h=50, s=100, l=50))
    img(sc_triadic, format_examples_path('traidic.png'))
