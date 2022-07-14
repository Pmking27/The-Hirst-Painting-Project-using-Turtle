import colorgram 
#pip install colorgram.py
# https://pypi.org/project/colorgram.py/

colors = colorgram.extract('img.jpg', 49)
rgb_color=[]
for color in colors:
    r=color.rgb.r
    g=color.rgb.g
    b=color.rgb.b
    new_color=(r,g,b)
    rgb_color.append(new_color)

print(rgb_color)    

