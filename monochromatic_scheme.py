
# 123 is the hue, there is not tinting and there is no shading

color = [230, 100, 50]

for i in range(11):

    print(
        "<div style='width:50;height:50;border: none; background-color: hsl({}, {}%, {}%);' >.</div>".format(
            color[0], color[1] - (10 * i), color[2]
        ))
