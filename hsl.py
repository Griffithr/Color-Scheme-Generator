class Hsl:

    MAX_HUE = 360

    def __init__(self, h, s, l):
        self._h = h
        self.h = h
        self.s = s
        self.l = l

    @property
    def h(self):
        return self._h

    @h.setter
    def h(self, hue):

        if hue <= 0 or hue > self.MAX_HUE:
            self._h = hue % self.MAX_HUE
        else:
            self._h = hue



    def pillow_format(self):
        return 'hsl({}, {}%, {}%)'.format(self.h, self.s, self.l)
