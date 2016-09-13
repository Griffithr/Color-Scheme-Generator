class Hsl:

    def __init__(self, h, s, l):
        # You have to do this not to get a recursion error
        self._h = h
        # You have to do this so the setter will give it a valid value
        self.h = h
        self.s = s
        self.l = l

    @property
    def h(self):
        return self._h

    @h.setter
    def h(self, hue):
        # Wraps around 360
        if hue < 0 or hue > 360:
            self._h = hue % 360
        else:
            self._h = hue

    def pillow_format(self):
        return 'hsl({}, {}%, {}%)'.format(self.h, self.s, self.l)
