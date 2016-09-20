from unittest import TestCase
from hsl import Hsl

class TestHsl(TestCase):

    def test_h(self):
        self.assertEqual(Hsl(370, 50, 50).h, 10)
        self.assertEqual(Hsl(360, 50, 50).h, 0)
        self.assertEqual(Hsl(361, 50, 50).h, 1)
        self.assertEqual(Hsl(-360, 50, 50).h, 0)

    def test_pillow_format(self):
        self.fail()
