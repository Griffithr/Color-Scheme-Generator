from unittest import TestCase
from generate_scheme import Generate
from hsl import Hsl


class TestGenerate(TestCase):

    hue_360 = Hsl(360, 100, 50)
    hue_180 = Hsl(180, 100, 50)
    hue_90 = Hsl(90, 100, 50)
    hue_0 = Hsl(0, 100, 50)

    def test_complementary(self):
        self.assertEqual(Generate().complementary(self.hue_360).h, 180)
        self.assertEqual(Generate().complementary(self.hue_180).h, 0)
        self.assertEqual(Generate().complementary(self.hue_90).h, 270)
        self.assertEqual(Generate().complementary(self.hue_0).h, 180)

    def test_monochromatic(self):
        self.fail()

    def test_analogous(self):
        scheme = Generate().analogous(self.hue_360, degree_dif=45)
        print(self.hue_360.h)
        self.assertEqual(scheme[0].h, (self.hue_360.h) - 45)
        self.assertEqual(scheme[1].h, self.hue_360.h + 45)

    def test_triadic(self):
        self.fail()

    def test_split_complementary(self):
        self.fail()

    def test_square(self):
        self.fail()
