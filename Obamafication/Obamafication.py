from Myro import *
DarkBlue = makeColor(0,51,76)
Red = makeColor(217, 26, 33)
Blue = makeColor(112,150,158)
Yellow = makeColor(252, 227, 166)
Magenta = makeColor(255,0,255)
pic = makePicture(pickAFile())

for pixel in getPixels(pic):
      gray = getBlue(pixel)
      if gray > 180:
             setColor(pixel,Yellow)
      red = getRed(pixel)
      if gray > 120:
             setColor(pixel, Blue)
      black = getGreen(pixel)
      if gray > 60:
             setColor(pixel, Red)
      else:
        setColor(pixel, DarkBlue)


        
#obamicon(pic)
show(pic)
