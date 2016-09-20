class Hsl:

    def __init__(self, h, s, l):
        self.h = h % 360
        self.s = s
        self.l = l

    '''
        @property
    def h(self):
        return self._h

    @h.setter
    def h(self, hue):

        self._h = hue % 360
        self.h = self._h

                if hue in range(0, self.MAX_HUE ):
            self._h = hue % self.MAX_HUE - 1
        else:
            self._h = hue


    '''



    def pillow_format(self):
        return 'hsl({}, {}%, {}%)'.format(self.h, self.s, self.l)

