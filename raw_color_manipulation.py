import colorsys

print(
    colorsys.hls_to_rgb(20, 40, 50),
    colorsys.rgb_to_hls(255, 255, 50)
)


"""
c = Color(rgb=(255, 60, 40))
c.hue(value=240)
c.hue()
    -> 240
c.hue(by_percent=10)
c.hue()
    -> 24
"""