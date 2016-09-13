from hsl import Hsl
from make_img_of_scheme import img

# SO to ttp://www.tigercolor.com/color-lab/color-theory/color-theory-intro.htm

class Generate:

    def __init__(self):
        pass

    def complementary(self, color):
        new_color = Hsl(h=color.h + 180, s=color.s, l=color.l)
        return color, new_color

    def monochromatic(self, color, amount_of_colors=10):
        new_colors = []

        for i in range(amount_of_colors):
            new_colors.append(
                Hsl(
                    h=color.h, s=color.s, l=int(color.l - (color.l/amount_of_colors) * i)
                ))

        return new_colors

    def analogous(self, color, degree_dif=45):
        return [
            Hsl(h=color._h - degree_dif, s=color.s, l=color.l),
            color,
            Hsl(h=color.h + degree_dif, s=color.s, l=color.l)
        ]

    def triadic(self, color):
        # 120 is a third of the color wheel
        return [
            Hsl(h=color.h - 120, s=color.s, l=color.l),
            color,
            Hsl(h=color.h + 120, s=color.s, l=color.l)
        ]

    def split_complementary(self, color):
        # takes complementary color and finds the two other colors next to it
        return [
            color,
            Hsl(h=color.h + 180 - 45, s=color.s, l=color.l),
            Hsl(h=color.h + 180 + 45, s=color.s, l=color.l)
        ]

    def square(self, color):
        return [
            color,
            Hsl(h=color.h + 90, s=color.s, l=color.l),
            Hsl(h=color.h + 180, s=color.s, l=color.l),
            Hsl(h=color.h - 90, s=color.s, l=color.l)
        ]

if __name__ == '__main__':
    import os

    def format_examples_path(file_name):
        return os.path.abspath('examples/') + '/' + file_name

    def generate_example_folder(fldr_name, scheme):
        for i in range(60):
            sc_img = scheme(Hsl(h=i*6, s=100, l=50))
            img(sc_img, format_examples_path('{}/{}.png'.format(fldr_name, str(i).zfill(3))))

    generate_example_folder('triadic', Generate().triadic)
    generate_example_folder('monochromatic', Generate().monochromatic)
    generate_example_folder('analogous', Generate().analogous)
    generate_example_folder('complementary', Generate().complementary)
    generate_example_folder('split_complementary', Generate().split_complementary)
    generate_example_folder('square', Generate().square)
