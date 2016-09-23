class Hsl:

    def __init__(self, h, s, l):
        self.h = h % 360
        self.s = s
        self.l = l

    def pillow_format(self):
        return 'hsl({}, {}%, {}%)'.format(self.h, self.s, self.l)

