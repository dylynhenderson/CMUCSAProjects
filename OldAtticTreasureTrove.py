# Click the mouse button to turn on and off the flashlight. 
# While the flashlight is on you can explore the previosuly hidden scene.
# Use the up and down arrow keys to turn on and off the lights.

# - Treasure Trove -
Rect(0, 0, 400, 400, fill=gradient(rgb(69, 69, 69), rgb(69, 69, 69), rgb(0, 0, 10), start='top'))
Rect(0, 330, 400, 70, fill=gradient(rgb(69, 69, 69), rgb(69, 69, 69), rgb(0, 0, 10), start='bottom'))

Rect(70, 120, 10, 240, fill=gradient(rgb(145, 61, 12), rgb(175, 91, 42), start='top'))
Circle(75, 120, 10, fill=rgb(145, 61, 12))
Oval(75, 130, 18, 10, fill=rgb(145, 61, 12))
Line(75, 130, 85, 140, fill=rgb(145, 61, 12))
Line(75, 130, 65, 140, fill=rgb(145, 61, 12))
Line(65, 140, 60, 135, fill=rgb(145, 61, 12))
Line(85, 140, 90, 135, fill=rgb(145, 61, 12))
Oval(90, 175, 10, 80, fill='teal')
Oval(85, 175, 10, 70, rotateAngle=5, fill='teal')
Oval(95, 175, 10, 70, rotateAngle=175, fill='teal')

Rect(40, 240, 120, 120, fill=gradient(rgb(145, 107, 86), rgb(173, 135, 98), start='top'), rotateAngle=359)
boxFlapLeft = Line(40, 240, 20, 300, lineWidth=3, fill = rgb(145, 107, 86), rotateAngle=358)
boxFlapRight = Line(160, 240, 180, 300, lineWidth=3, fill = rgb(145, 107, 86), rotateAngle=358)
Rect(50, 250, 30, 30, fill='bisque')
Line(140, 265, 140, 285, lineWidth=8, fill='brown')
Polygon(125, 265, 155, 265, 140, 245, fill='brown')
Polygon(93, 360, 107, 360, 107, 330, 105, 332, 103, 329.5, 101, 331.5, 99, 327.8, 97, 331.2, 95, 328.8, 93, 330, fill='brown', opacity=30)

Rect(220, 120, 140, 240, fill=gradient('sienna', 'sienna', 'sienna', 'tan', start='bottom'), border='saddleBrown', borderWidth=10)
Line(224, 356, 356, 124, fill='saddleBrown', lineWidth=10)
Line(224, 124, 356, 356, fill='saddleBrown', lineWidth=10)

Label('FRAGILE', 290, 235, rotateAngle=-50, size=35, fill='tomato', bold=True, font='arial')

Rect(280, 200, 100, 165, fill=gradient('sienna', 'sienna', 'sienna', 'tan', start='bottom'), border='saddleBrown', borderWidth=10)
Line(284, 204, 376, 356, fill='saddleBrown', lineWidth=10)
Line(284, 356, 376, 204, fill='saddleBrown', lineWidth=10)

Rect(40, 0, 10, 10, fill='goldenrod')
Oval(45, 30, 30, 45, fill='white', opacity=10, border='black')
Oval(45, 30, 30, 45, fill=None, border='goldenrod')
Line(43, 10, 43, 35, opacity=20)
Line(47, 10, 47, 35, opacity=20)
Circle(47, 35, 5, fill=None, border='black', opacity=20)
Circle(43, 35, 5, fill=None, border='black', opacity=20)
Line(20, 0, 20, 60, fill='dimGray')
Circle(20, 60, 3, fill='dimGray')
Circle(20, 50, 3, fill='dimGray')
Circle(20, 40, 3, fill='dimGray')
Circle(20, 30, 3, fill='dimGray')
Circle(20, 20, 3, fill='dimGray')

Rect(80, 25, 120, 65, fill='antiqueWhite', border='sienna', borderWidth=4)
Rect(90, 40, 90, 35, fill='lightGoldenrodYellow')
Circle(98, 45, 2, fill='red')
Circle(172, 44, 2, fill='red')
Label('Up and Down', 135, 56, size=12)

Circle(150, 335, 45, fill=gradient('burlyWood', 'peru'))
Circle(151, 304, 4, fill='saddleBrown')
Circle(165, 326, 4, fill='saddleBrown')
Circle(129, 358, 4, fill='saddleBrown')
Circle(160, 355, 4, fill='saddleBrown')
Circle(126, 328, 4, fill='saddleBrown')
Circle(143, 342, 4, fill='saddleBrown')
Circle(180, 339, 4, fill='saddleBrown')

Circle(290, 35, 20, fill='cyan')
Rect(270, 35, 40, 35, fill='cyan')
Polygon(270, 70, 270, 80, 275, 70, 280, 80, 285, 70, 290, 80, 295, 70, 300, 80, 305, 70, 310, 80, 310, 70, 270, 70, fill='cyan')
Circle(280, 35, 5, fill='white')
Circle(295, 35, 5, fill='white')
Circle(278, 36, 2)
Circle(293, 36, 2)

# - Flashlight -
#Flashlight Light
light = Circle(200, 200, 1050, fill=None, border='black', borderWidth=1000, visible=True)
#Flashlight Body
#flashlightON2 =
on1 = Polygon(315, 359, 242, 331, 318, 242, 358, 313, fill='yellow', opacity=35)
#flashlight =
Line(400, 400, 350, 350, lineWidth=50, fill=rgb(217, 73, 54))
Oval(338, 338, 65, 30, rotateAngle=130, fill=rgb(217, 73, 54), border=rgb(156, 54, 40))
Oval(350, 350, 65, 30, rotateAngle=130, fill=rgb(217, 73, 54))
Oval(347, 347, 65, 30, rotateAngle=130, fill=rgb(217, 73, 54))
Oval(344, 344, 65, 30, rotateAngle=130, fill=rgb(217, 73, 54))
Oval(341, 341, 65, 30, rotateAngle=130, fill=rgb(217, 73, 54))
Line(366, 400, 341, 375, fill=rgb(156, 54, 40))
Line(400, 363, 373, 339, fill=rgb(156, 54, 40))
Line(341, 375, 373, 339, fill=rgb(156, 54, 40))
Line(315, 359, 331, 376, fill=rgb(156, 54, 40))
Line(358, 313, 373, 328, fill=rgb(156, 54, 40))
Line(373, 328, 373, 339, fill=rgb(156, 54, 40))
Line(331, 376, 341, 375,fill=rgb(156, 54, 40))
#flashlightON1 = 
on2 = Rect(367, 365, 20, 25, rotateAngle=130, visible=True, fill=rgb(81, 109, 143), border=rgb(61, 77, 97))
#flashlightOFF = 
off1 = Rect(384, 379, 20, 25, rotateAngle=130, visible=False, fill=rgb(81, 109, 143), border=rgb(61, 77, 97))

# - Treasure Trove Copy - 
copy1 = Rect(0, 0, 400, 400, fill=gradient(rgb(69, 69, 69), rgb(69, 69, 69), rgb(0, 0, 10), start='top'), visible=False)
copy2 = Rect(0, 330, 400, 70, fill=gradient(rgb(69, 69, 69), rgb(69, 69, 69), rgb(0, 0, 10), start='bottom'), visible=False)
copy3 = Rect(70, 120, 10, 240, fill=gradient(rgb(145, 61, 12), rgb(175, 91, 42), start='top'), visible=False)
copy4 = Circle(75, 120, 10, fill=rgb(145, 61, 12), visible=False)
copy5 = Oval(75, 130, 18, 10, fill=rgb(145, 61, 12), visible=False)
copy6 = Line(75, 130, 85, 140, fill=rgb(145, 61, 12), visible=False)
copy7 = Line(75, 130, 65, 140, fill=rgb(145, 61, 12), visible=False)
copy8 = Line(65, 140, 60, 135, fill=rgb(145, 61, 12), visible=False)
copy9 = Line(85, 140, 90, 135, fill=rgb(145, 61, 12), visible=False)
copy10 = Oval(90, 175, 10, 80, fill='teal', visible=False)
copy11 = Oval(85, 175, 10, 70, rotateAngle=5, fill='teal', visible=False)
copy12 = Oval(95, 175, 10, 70, rotateAngle=175, fill='teal', visible=False)
copy13 = Rect(40, 240, 120, 120, fill=gradient(rgb(145, 107, 86), rgb(173, 135, 98), start='top'), rotateAngle=359, visible=False)
copy14 = boxFlapLeft = Line(40, 240, 20, 300, lineWidth=3, fill = rgb(145, 107, 86), rotateAngle=358, visible=False)
copy15 = boxFlapRight = Line(160, 240, 180, 300, lineWidth=3, fill = rgb(145, 107, 86), rotateAngle=358, visible=False)
copy16 = Rect(50, 250, 30, 30, fill='bisque', visible=False)
copy17 = Line(140, 265, 140, 285, lineWidth=8, fill='brown', visible=False)
copy18 = Polygon(125, 265, 155, 265, 140, 245, fill='brown', visible=False)
copy19 = Polygon(93, 360, 107, 360, 107, 330, 105, 332, 103, 329.5, 101, 331.5, 99, 327.8, 97, 331.2, 95, 328.8, 93, 330, fill='brown', opacity=30, visible=False)
copy20 = Rect(220, 120, 140, 240, fill=gradient('sienna', 'sienna', 'sienna', 'tan', start='bottom'), border='saddleBrown', borderWidth=10, visible=False)
copy21 = Line(224, 356, 356, 124, fill='saddleBrown', lineWidth=10, visible=False)
copy22 = Line(224, 124, 356, 356, fill='saddleBrown', lineWidth=10, visible=False)
copy23 = Label('FRAGILE', 290, 235, rotateAngle=-50, size=35, fill='tomato', bold=True, font='arial', visible=False)
copy24 = Rect(280, 200, 100, 165, fill=gradient('sienna', 'sienna', 'sienna', 'tan', start='bottom'), border='saddleBrown', borderWidth=10, visible=False)
copy25 = Line(284, 204, 376, 356, fill='saddleBrown', lineWidth=10, visible=False)
copy26 = Line(284, 356, 376, 204, fill='saddleBrown', lineWidth=10, visible=False)
copy27 = Rect(40, 0, 10, 10, fill='goldenrod', visible=False)
copy28 = Oval(45, 30, 30, 45, fill='white', opacity=10, border='black', visible=False)
copy29 = Oval(45, 30, 30, 45, fill=None, border='goldenrod', visible=False)
copy30 = Line(43, 10, 43, 35, fill='yellow', opacity=80, visible=False)
copy31 = Line(47, 10, 47, 35, fill='yellow', opacity=80, visible=False)
copy32 = Circle(47, 35, 5, fill=None, border='yellow', opacity=80, visible=False)
copy33 = Circle(43, 35, 5, fill=None, border='yellow', opacity=80, visible=False)
copy34 = Line(20, 0, 20, 60, fill='dimGray', visible=False)
copy35 = Circle(20, 60, 3, fill='dimGray', visible=False)
copy36 = Circle(20, 50, 3, fill='dimGray', visible=False)
copy37 = Circle(20, 40, 3, fill='dimGray', visible=False)
copy38 = Circle(20, 30, 3, fill='dimGray', visible=False)
copy39 = Circle(20, 20, 3, fill='dimGray', visible=False)
copy41 = Rect(80, 25, 120, 65, fill='antiqueWhite', border='sienna', borderWidth=4, visible=False)
copy42 = Rect(90, 40, 90, 35, fill='lightGoldenrodYellow', visible=False)
copy43 = Circle(98, 45, 2, fill='red', visible=False)
copy44 = Circle(172, 44, 2, fill='red', visible=False)
copy45 = Label('Up and Down', 135, 56, size=12)
copy46 = Circle(150, 335, 45, fill=gradient('burlyWood', 'peru'), visible=False)
copy47 = Circle(151, 304, 4, fill='saddleBrown', visible=False)
copy48 = Circle(165, 326, 4, fill='saddleBrown', visible=False)
copy49 = Circle(129, 358, 4, fill='saddleBrown', visible=False)
copy50 = Circle(160, 355, 4, fill='saddleBrown', visible=False)
copy51 = Circle(126, 328, 4, fill='saddleBrown', visible=False)
copy52 = Circle(143, 342, 4, fill='saddleBrown', visible=False)
copy53 = Circle(180, 339, 4, fill='saddleBrown', visible=False)
copy54 = Circle(290, 35, 20, fill='cyan', visible=False)
copy55 = Rect(270, 35, 40, 35, fill='cyan', visible=False)
copy56 = Polygon(270, 70, 270, 80, 275, 70, 280, 80, 285, 70, 290, 80, 295, 70, 300, 80, 305, 70, 310, 80, 310, 70, 270, 70, fill='cyan', visible=False)
copy57 = Circle(280, 35, 5, fill='white', visible=False)
copy58 = Circle(295, 35, 5, fill='white', visible=False)
copy59 = Circle(278, 36, 2, visible=False)
copy60 = Circle(293, 36, 2, visible=False)


# Turn flashlight ON and OFF
def onMousePress(x, y):
    if  (light.fill == None):
        light.fill = 'black'
        on1.opacity = 0
        off1.visible = True
        on2.visible = False
        
    elif  (light.fill == 'black'):
        light.fill = None
        on1.opacity = 35
        off1.visible = False
        on2.visible = True
        
def onMouseMove(x, y):
    light.centerX = x
    light.centerY = y
    
# Moves a copy of the room infront of the flashlight
def onKeyPress(key):
    if (key == 'up'):
        copy1.visible = True
        copy2.visible = True
        copy3.visible = True
        copy4.visible = True
        copy5.visible = True
        copy6.visible = True
        copy7.visible = True
        copy8.visible = True
        copy9.visible = True
        copy10.visible = True
        copy11.visible = True
        copy12.visible = True
        copy13.visible = True
        copy14.visible = True
        copy15.visible = True
        copy16.visible = True
        copy17.visible = True
        copy18.visible = True
        copy19.visible = True
        copy20.visible = True
        copy21.visible = True
        copy22.visible = True
        copy23.visible = True
        copy24.visible = True
        copy25.visible = True
        copy26.visible = True
        copy27.visible = True
        copy28.visible = True
        copy29.visible = True
        copy30.visible = True
        copy31.visible = True
        copy32.visible = True
        copy33.visible = True
        copy34.visible = True
        copy35.visible = True
        copy36.visible = True
        copy37.visible = True
        copy38.visible = True
        copy39.visible = True
        copy41.visible = True
        copy42.visible = True
        copy43.visible = True
        copy44.visible = True
        copy45.visible = True
        copy46.visible = True
        copy47.visible = True
        copy48.visible = True
        copy49.visible = True
        copy50.visible = True
        copy51.visible = True
        copy52.visible = True
        copy53.visible = True
        copy54.visible = True
        copy55.visible = True
        copy56.visible = True
        copy57.visible = True
        copy58.visible = True
        copy59.visible = True
        copy60.visible = True
    elif (key == 'down'):
        copy1.visible = False
        copy2.visible = False
        copy3.visible = False
        copy4.visible = False
        copy5.visible = False
        copy6.visible = False
        copy7.visible = False
        copy8.visible = False
        copy9.visible = False
        copy10.visible = False
        copy11.visible = False
        copy12.visible = False
        copy13.visible = False
        copy14.visible = False
        copy15.visible = False
        copy16.visible = False
        copy17.visible = False
        copy18.visible = False
        copy19.visible = False
        copy20.visible = False
        copy21.visible = False
        copy22.visible = False
        copy23.visible = False
        copy24.visible = False
        copy25.visible = False
        copy26.visible = False
        copy27.visible = False
        copy28.visible = False
        copy29.visible = False
        copy30.visible = False
        copy31.visible = False
        copy32.visible = False
        copy33.visible = False
        copy34.visible = False
        copy35.visible = False
        copy36.visible = False
        copy37.visible = False
        copy38.visible = False
        copy39.visible = False
        copy41.visible = False
        copy42.visible = False
        copy43.visible = False
        copy44.visible = False
        copy45.visible = False
        copy46.visible = False
        copy47.visible = False
        copy48.visible = False
        copy49.visible = False
        copy50.visible = False
        copy51.visible = False
        copy52.visible = False
        copy53.visible = False
        copy54.visible = False
        copy55.visible = False
        copy56.visible = False
        copy57.visible = False
        copy58.visible = False
        copy59.visible = False
        copy60.visible = False
