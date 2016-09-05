from hsl import Hsl
from make_img_of_scheme import img


class Generate:

    def __init__(self):
        pass

        '''
            There needs to be a way to specify if you want to keep the saturation and lightness
            or just use normal values ie 100 and 50
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

    def analogous(self, color, degree_dif=45):
        return [
            Hsl(h=color.h - degree_dif, s=color.s, l=color.l),
            color,
            Hsl(h=color.h + degree_dif, s=color.s, l=color.l)
        ]


if __name__ == '__main__':
    sc_complementary = Generate().complementary(Hsl(h=360, s=100, l=50))
    img(sc_complementary, 'complementary.png')

    sc_monochromatic = Generate().monochromatic(Hsl(h=128, s=100, l=50), amount_of_colors=10)
    img(sc_monochromatic, 'monochromatic.png')

    sc_analogous = Generate().analogous(Hsl(h=50, s=100, l=50))
    img(sc_analogous, 'analogous.png')