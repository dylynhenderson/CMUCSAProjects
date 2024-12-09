app.background = 'lightBlue'

#               - CS Paint -
#
#       - Tools - 
#   - Palette - 
#       Click different color on the
#       Palette to change the color 
#       of the strokes
#   - Paintbrushes -
#       Click the small paintbrush to
#       lower the size of strokes by 10
#       Click the large paintbrush to 
#       raise the size of strokes by 10
#   - Golden Paintbrush - 
#       Select the golden paintbrush to
#       paint masterpieces
#   - Paint Bucket - 
#       Select the paint bucket to drop
#       random paint splaters on the 
#       canvas 
#   - Eraser -
#       Select the eraser to wipe 
#       paint from the canvas
#
#   Press 'Enter' to sign your work!
#   (If your name is Dylan...)
#

sizeBank = Rect(0, 0, 1, 1, fill=None, 
    opacity=20) # Trackable Value
sizeBank2 = Rect(0, 399, 1, 1, fill=None,
    opacity=20) # Trackable Value
colorBank = Rect(399, 399, 1, 1, opacity=0, 
    fill='black') # Trackable Value
rotateBank = Rect(399, 0, 1, 1, fill=None,
    rotateAngle=0) # Trackable Value
visibilityBank = Rect(1, 0 , 1, 1, fill=None,
    visible=True)
visibilityBank2 = Rect(1, 0 , 1, 1, fill=None,
    visible=False)
# Constantly Change the rotateAngle Value, opacity Value, and visible Value
# This allows the Paint Splats to look Different Every Time
def onStep():
    rotateBank.rotateAngle += 17
    if(sizeBank2.opacity == 20):
        sizeBank2.opacity = 22
    elif(sizeBank2.opacity == 22):
        sizeBank2.opacity = 24
    elif(sizeBank2.opacity == 24):
        sizeBank2.opacity = 26
    elif(sizeBank2.opacity == 26):
        sizeBank2.opacity = 28
    elif(sizeBank2.opacity == 28):
        sizeBank2.opacity = 30
    elif(sizeBank2.opacity == 30):
        sizeBank2.opacity = 29
    elif(sizeBank2.opacity == 29):
        sizeBank2.opacity = 27
    elif(sizeBank2.opacity == 27):
        sizeBank2.opacity = 25
    elif(sizeBank2.opacity == 25):
        sizeBank2.opacity = 23
    elif(sizeBank2.opacity == 23):
        sizeBank2.opacity = 21
    elif(sizeBank2.opacity == 21):
        sizeBank2.opacity = 20
    if(visibilityBank.visible == True):
        visibilityBank.visible = False
    elif(visibilityBank.visible == False):
        visibilityBank.visible = True
    if(visibilityBank2.visible == False):
        visibilityBank2.visible = True
    elif(visibilityBank2.visible == True):
        visibilityBank2.visible = False
        
# Canvas that the User can Draw on
canvas = Polygon(40, 40, 360, 40, 360, 360, 129, 360, 131, 337, 112, 308, 84, 290, 40, 283, fill='white')
Polygon(40, 40, 55, 25, 375, 25, 360, 40, fill=rgb(217, 216, 212))
Polygon(360, 360, 375, 345, 375, 25, 360, 40, fill=rgb(196, 195, 192))

# The Resulting Design when Using the Paint Bucket
def drawSplat(x, y, size, color, angle, visibility, visibility2):
    Circle(x, y, 20, fill=color)
    Circle(x-10, y+28, 
    size-13,                                #Changes Size 
    fill=color, )
    Circle(x-20, y-30, 
    size-17,                                #Changes Size 
    fill=color)
    Oval(x+10, y-10, 20, 50, fill=color, 
    rotateAngle=angle)                      #Changes Orientation
    Oval(x+9, y+19, 30, 12, fill=color, 
    rotateAngle=angle)                      #Changes Orientation
    Oval(x-30, y, 10, 35, fill=color, 
    rotateAngle=angle)                      #Changes Orientation
    Rect(x+25, y-2, 10, 10, fill=color, rotateAngle=45, 
    visible=visibility)                     #Changes Visibility
    Rect(x-38, y+20, 10, 10, fill=color, rotateAngle=67,
    visible=visibility2)                    #Changes Visibility

    
# Small Paintbrush used to Lower the Size of the Strokes
smallPaintbrush = Group(
    Oval(153, 364, 20, 80, rotateAngle=5, fill=rgb(173, 106, 33)),
    Oval(155.5, 333, 20, 30, fill=rgb(212, 147, 87)),
    Polygon(147, 327, 156, 305, 165, 328, fill=gradient(rgb(212, 147, 87), rgb(235, 35, 35), rgb(235, 35, 35), start='bottom'))
    )
  
# Large Paintbrush used to Raise teh SIze of the Stokes
largePaintbrush = Group(
    Oval(187, 371, 28, 110, rotateAngle=-4, fill=rgb(173, 106, 33)),
    Oval(184.5, 324, 23, 35, fill=rgb(212, 147, 87), rotateAngle=-4),
    Polygon(175, 320,181, 293, 196, 320, fill=gradient(rgb(212, 147, 87), rgb(35, 108, 235), rgb(35, 108, 235), start='bottom'))
    )
    
# Guide to Insert Images in CMU CS Academy - Image( <URL> , left, top)

goldenPaintbrush = Group(
    Oval(226, 361, 20, 80, rotateAngle=-5, fill=rgb(242, 207, 124)),
    Oval(223, 325, 20, 30, fill=rgb(219, 185, 105)),
    Polygon(214, 320, 221, 300, 233, 321, fill=gradient(rgb(244, 247, 37), rgb(244, 247, 37), rgb(219, 185, 105), start='top'))
    )
    
paintBucket = Group(
    Rect(250, 340, 60, 63, fill=rgb(117, 116, 111), border=rgb(66, 64, 64), borderWidth=3),
    Oval(280, 340, 60, 20, fill=gradient(rgb(235, 35, 35), rgb(245, 123, 29), rgb(244, 247, 37), rgb(30, 163, 18), rgb(35, 108, 235), rgb(241, 29, 245), start='left'), border=rgb(66, 64, 64), borderWidth=3)
    )
    
eraser = Group(
    Rect(320, 375, 30, 25, fill=rgb(240, 117, 227)),
    Polygon(320, 375, 328, 370, 358, 370, 350, 375, fill=rgb(201, 101, 191)),
    Polygon(350, 375,358, 370, 358, 400, 350, 400, fill=rgb(168, 84, 160))
    )

# Palette used in Every Palette Variation
palette = Group(
    Oval(35, 345, 195, 140, fill=rgb(173, 106, 33), border=rgb(97, 53, 5), borderWidth=3),
    Circle(72, 308, 15, fill='white'),
    Circle(72, 308, 15, fill=None, border=rgb(97, 53, 5), borderWidth=3)
    )

# Rainbow Paints
blackPaint = Oval(23, 308, 27, 33, rotateAngle=13, border=rgb(250, 207, 67), borderWidth=3)
redPaint = Oval(52, 335, 19, 27, rotateAngle=57, fill=rgb(235, 35, 35), border=None, borderWidth=3)
bluePaint = Oval(97, 327, 25, 18, rotateAngle=39, fill=rgb(35, 108, 235), border=None, borderWidth=3)
greenPaint = Oval(80, 357,26, 21, rotateAngle=48, fill=rgb(30, 163, 18), border=None, borderWidth=3)
pinkPaint = Oval(14, 343, 18, 28, rotateAngle=15, fill=rgb(237, 130, 119), border=None, borderWidth=3)
yellowPaint = Oval(42, 362, 27, 19, rotateAngle=7, fill=rgb(244, 247, 37), border=None, borderWidth=3)
orangePaint = Oval(67, 388, 16, 31, rotateAngle=84, fill=rgb(245, 123, 29), border=None, borderWidth=3)
purplePaint = Oval(111, 354, 18, 30, rotateAngle=45, fill=rgb(241, 29, 245), border=None, borderWidth=3)
lightBluePaint = Oval(23, 382, 26, 17, rotateAngle=37, fill=rgb(41, 197, 240), border=None, borderWidth=3)

def onMouseDrag(mouseX, mouseY):
    if(canvas.contains(mouseX, mouseY) == True):
        if(sizeBank.opacity > 0.2):
            Circle(mouseX, mouseY, sizeBank.opacity, fill=colorBank.fill)
        elif(sizeBank.opacity == 0.1):
            # Image('link', mouseX-10, mouseY-15)

def onMousePress(mouseX, mouseY):
    if(blackPaint.contains(mouseX, mouseY) == True):
        colorBank.fill = 'black'
        blackPaint.border = rgb(250, 207, 67)
        redPaint.border = None
        bluePaint.border = None
        greenPaint.border = None
        pinkPaint.border = None
        yellowPaint.border = None
        orangePaint.border = None
        purplePaint.border = None
        lightBluePaint.border = None
        if(sizeBank.opacity == 0.1):
            sizeBank.opacity = 20
        elif(sizeBank.opacity == 5):
            sizeBank.opacity = 20
        elif(sizeBank.opacity == 15):
            sizeBank.opacity = 20
        elif(sizeBank.opacity == 25):
            sizeBank.opacity = 20
        elif(sizeBank.opacity == 35):
            sizeBank.opacity = 20
        elif(sizeBank.opacity == 45):
            sizeBank.opacity = 20
        elif(sizeBank.opacity == 55):
            sizeBank.opacity = 20
        elif(sizeBank.opacity == 65):
            sizeBank.opacity = 20
        elif(sizeBank.opacity == 75):
            sizeBank.opacity = 20
        elif(sizeBank.opacity == 85):
            sizeBank.opacity = 20
        elif(sizeBank.opacity == 95):
            sizeBank.opacity = 20
    elif(redPaint.contains(mouseX, mouseY) == True):
        colorBank.fill = rgb(235, 35, 35)
        blackPaint.border = None
        redPaint.border = rgb(250, 207, 67)
        bluePaint.border = None
        greenPaint.border = None
        pinkPaint.border = None
        yellowPaint.border = None
        orangePaint.border = None
        purplePaint.border = None
        lightBluePaint.border = None
        if(sizeBank.opacity == 0.1):
            sizeBank.opacity = 20
        elif(sizeBank.opacity == 5):
            sizeBank.opacity = 20
        elif(sizeBank.opacity == 15):
            sizeBank.opacity = 20
        elif(sizeBank.opacity == 25):
            sizeBank.opacity = 20
        elif(sizeBank.opacity == 35):
            sizeBank.opacity = 20
        elif(sizeBank.opacity == 45):
            sizeBank.opacity = 20
        elif(sizeBank.opacity == 55):
            sizeBank.opacity = 20
        elif(sizeBank.opacity == 65):
            sizeBank.opacity = 20
        elif(sizeBank.opacity == 75):
            sizeBank.opacity = 20
        elif(sizeBank.opacity == 85):
            sizeBank.opacity = 20
        elif(sizeBank.opacity == 95):
            sizeBank.opacity = 20
    elif(bluePaint.contains(mouseX, mouseY) == True):
        colorBank.fill = rgb(35, 108, 235)
        blackPaint.border = None
        redPaint.border = None
        bluePaint.border = rgb(250, 207, 67)
        greenPaint.border = None
        pinkPaint.border = None
        yellowPaint.border = None
        orangePaint.border = None
        purplePaint.border = None
        lightBluePaint.border = None
        if(sizeBank.opacity == 0.1):
            sizeBank.opacity = 20
        elif(sizeBank.opacity == 5):
            sizeBank.opacity = 20
        elif(sizeBank.opacity == 15):
            sizeBank.opacity = 20
        elif(sizeBank.opacity == 25):
            sizeBank.opacity = 20
        elif(sizeBank.opacity == 35):
            sizeBank.opacity = 20
        elif(sizeBank.opacity == 45):
            sizeBank.opacity = 20
        elif(sizeBank.opacity == 55):
            sizeBank.opacity = 20
        elif(sizeBank.opacity == 65):
            sizeBank.opacity = 20
        elif(sizeBank.opacity == 75):
            sizeBank.opacity = 20
        elif(sizeBank.opacity == 85):
            sizeBank.opacity = 20
        elif(sizeBank.opacity == 95):
            sizeBank.opacity = 20
    elif(greenPaint.contains(mouseX, mouseY) == True):
        colorBank.fill = rgb(30, 163, 18)
        blackPaint.border = None
        redPaint.border = None
        bluePaint.border = None
        greenPaint.border = rgb(250, 207, 67)
        pinkPaint.border = None
        yellowPaint.border = None
        orangePaint.border = None
        purplePaint.border = None
        lightBluePaint.border = None
        if(sizeBank.opacity == 0.1):
            sizeBank.opacity = 20
        elif(sizeBank.opacity == 5):
            sizeBank.opacity = 20
        elif(sizeBank.opacity == 15):
            sizeBank.opacity = 20
        elif(sizeBank.opacity == 25):
            sizeBank.opacity = 20
        elif(sizeBank.opacity == 35):
            sizeBank.opacity = 20
        elif(sizeBank.opacity == 45):
            sizeBank.opacity = 20
        elif(sizeBank.opacity == 55):
            sizeBank.opacity = 20
        elif(sizeBank.opacity == 65):
            sizeBank.opacity = 20
        elif(sizeBank.opacity == 75):
            sizeBank.opacity = 20
        elif(sizeBank.opacity == 85):
            sizeBank.opacity = 20
        elif(sizeBank.opacity == 95):
            sizeBank.opacity = 20
    elif(pinkPaint.contains(mouseX, mouseY) == True):
        colorBank.fill = rgb(237, 130, 119)
        blackPaint.border = None
        redPaint.border = None
        bluePaint.border = None
        greenPaint.border = None
        pinkPaint.border = rgb(250, 207, 67)
        yellowPaint.border = None
        orangePaint.border = None
        purplePaint.border = None
        lightBluePaint.border = None
        if(sizeBank.opacity == 0.1):
            sizeBank.opacity = 20
        elif(sizeBank.opacity == 5):
            sizeBank.opacity = 20
        elif(sizeBank.opacity == 15):
            sizeBank.opacity = 20
        elif(sizeBank.opacity == 25):
            sizeBank.opacity = 20
        elif(sizeBank.opacity == 35):
            sizeBank.opacity = 20
        elif(sizeBank.opacity == 45):
            sizeBank.opacity = 20
        elif(sizeBank.opacity == 55):
            sizeBank.opacity = 20
        elif(sizeBank.opacity == 65):
            sizeBank.opacity = 20
        elif(sizeBank.opacity == 75):
            sizeBank.opacity = 20
        elif(sizeBank.opacity == 85):
            sizeBank.opacity = 20
        elif(sizeBank.opacity == 95):
            sizeBank.opacity = 20
    elif(yellowPaint.contains(mouseX, mouseY) == True):
        colorBank.fill = rgb(244, 247, 37)
        blackPaint.border = None
        redPaint.border = None
        bluePaint.border = None
        greenPaint.border = None
        pinkPaint.border = None
        yellowPaint.border = rgb(250, 207, 67)
        orangePaint.border = None
        purplePaint.border = None
        lightBluePaint.border = None
        if(sizeBank.opacity == 0.1):
            sizeBank.opacity = 20
        elif(sizeBank.opacity == 5):
            sizeBank.opacity = 20
        elif(sizeBank.opacity == 15):
            sizeBank.opacity = 20
        elif(sizeBank.opacity == 25):
            sizeBank.opacity = 20
        elif(sizeBank.opacity == 35):
            sizeBank.opacity = 20
        elif(sizeBank.opacity == 45):
            sizeBank.opacity = 20
        elif(sizeBank.opacity == 55):
            sizeBank.opacity = 20
        elif(sizeBank.opacity == 65):
            sizeBank.opacity = 20
        elif(sizeBank.opacity == 75):
            sizeBank.opacity = 20
        elif(sizeBank.opacity == 85):
            sizeBank.opacity = 20
        elif(sizeBank.opacity == 95):
            sizeBank.opacity = 20
    elif(orangePaint.contains(mouseX, mouseY) == True):
        colorBank.fill = rgb(245, 123, 29)
        blackPaint.border = None
        redPaint.border = None
        bluePaint.border = None
        greenPaint.border = None
        pinkPaint.border = None
        yellowPaint.border = None
        orangePaint.border = rgb(250, 207, 67)
        purplePaint.border = None
        lightBluePaint.border = None
        if(sizeBank.opacity == 0.1):
            sizeBank.opacity = 20
        elif(sizeBank.opacity == 5):
            sizeBank.opacity = 20
        elif(sizeBank.opacity == 15):
            sizeBank.opacity = 20
        elif(sizeBank.opacity == 25):
            sizeBank.opacity = 20
        elif(sizeBank.opacity == 35):
            sizeBank.opacity = 20
        elif(sizeBank.opacity == 45):
            sizeBank.opacity = 20
        elif(sizeBank.opacity == 55):
            sizeBank.opacity = 20
        elif(sizeBank.opacity == 65):
            sizeBank.opacity = 20
        elif(sizeBank.opacity == 75):
            sizeBank.opacity = 20
        elif(sizeBank.opacity == 85):
            sizeBank.opacity = 20
        elif(sizeBank.opacity == 95):
            sizeBank.opacity = 20
    elif(purplePaint.contains(mouseX, mouseY) == True):
        colorBank.fill = rgb(241, 29, 245)
        blackPaint.border = None
        redPaint.border = None
        bluePaint.border = None
        greenPaint.border = None
        pinkPaint.border = None
        yellowPaint.border = None
        orangePaint.border = None
        purplePaint.border = rgb(250, 207, 67)
        lightBluePaint.border = None
        if(sizeBank.opacity == 0.1):
            sizeBank.opacity = 20
        elif(sizeBank.opacity == 5):
            sizeBank.opacity = 20
        elif(sizeBank.opacity == 15):
            sizeBank.opacity = 20
        elif(sizeBank.opacity == 25):
            sizeBank.opacity = 20
        elif(sizeBank.opacity == 35):
            sizeBank.opacity = 20
        elif(sizeBank.opacity == 45):
            sizeBank.opacity = 20
        elif(sizeBank.opacity == 55):
            sizeBank.opacity = 20
        elif(sizeBank.opacity == 65):
            sizeBank.opacity = 20
        elif(sizeBank.opacity == 75):
            sizeBank.opacity = 20
        elif(sizeBank.opacity == 85):
            sizeBank.opacity = 20
        elif(sizeBank.opacity == 95):
            sizeBank.opacity = 20
    elif(lightBluePaint.contains(mouseX, mouseY) == True):
        colorBank.fill = rgb(41, 197, 240)
        blackPaint.border = None
        redPaint.border = None
        bluePaint.border = None
        greenPaint.border = None
        pinkPaint.border = None
        yellowPaint.border = None
        orangePaint.border = None
        purplePaint.border = None
        lightBluePaint.border = rgb(250, 207, 67)
        if(sizeBank.opacity == 0.1):
            sizeBank.opacity = 20
        elif(sizeBank.opacity == 5):
            sizeBank.opacity = 20
        elif(sizeBank.opacity == 15):
            sizeBank.opacity = 20
        elif(sizeBank.opacity == 25):
            sizeBank.opacity = 20
        elif(sizeBank.opacity == 35):
            sizeBank.opacity = 20
        elif(sizeBank.opacity == 45):
            sizeBank.opacity = 20
        elif(sizeBank.opacity == 55):
            sizeBank.opacity = 20
        elif(sizeBank.opacity == 65):
            sizeBank.opacity = 20
        elif(sizeBank.opacity == 75):
            sizeBank.opacity = 20
        elif(sizeBank.opacity == 85):
            sizeBank.opacity = 20
        elif(sizeBank.opacity == 95):
            sizeBank.opacity = 20
    elif(smallPaintbrush.contains(mouseX, mouseY) == True):
        if(sizeBank.opacity > 10):
            sizeBank.opacity -= 10
            smallPaintbrush.opacity = 90
    elif(largePaintbrush.contains(mouseX, mouseY) == True):
        if(sizeBank.opacity == 95):
            sizeBank.opacity += 0
        elif(sizeBank.opacity < 100):
            sizeBank.opacity += 10
            largePaintbrush.opacity = 90
    elif(goldenPaintbrush.contains(mouseX, mouseY) == True):
        if(sizeBank.opacity != 0.1):
            sizeBank.opacity=0.1
            colorBank.fill=None
            blackPaint.border = None
            redPaint.border = None
            bluePaint.border = None
            greenPaint.border = None
            pinkPaint.border = None
            yellowPaint.border = None
            orangePaint.border = None
            purplePaint.border = None
            lightBluePaint.border = None
            goldenPaintbrush.opacity = 90
        elif(sizeBank.opacity == 0.1):
            sizeBank.opacity=20
            colorBank.fill='black'
            blackPaint.border = rgb(250, 207, 67)
            redPaint.border = None
            bluePaint.border = None
            greenPaint.border = None
            pinkPaint.border = None
            yellowPaint.border = None
            orangePaint.border = None
            purplePaint.border = None
            lightBluePaint.border = None
            goldenPaintbrush.opacity = 90
    elif(paintBucket.contains(mouseX, mouseY) == True):
        if(sizeBank.opacity != 0.2):
            sizeBank.opacity=0.2
            paintBucket.opacity = 90
        elif(sizeBank.opacity == 0.2):
            sizeBank.opacity=20
            paintBucket.opacity = 90
        if(colorBank.fill == 'white'):
            colorBank.fill='black'
            blackPaint.border = rgb(250, 207, 67)
        if(colorBank.fill == None):
            colorBank.fill='black'
            blackPaint.border = rgb(250, 207, 67)
    elif(canvas.contains(mouseX, mouseY) == True):
        if(sizeBank.opacity == 0.2):
            drawSplat(mouseX, mouseY, sizeBank2.opacity, colorBank.fill, rotateBank.rotateAngle, visibilityBank.visible, visibilityBank2.visible)
    elif(eraser.contains(mouseX, mouseY) == True):
        if(colorBank.fill != 'white'):
            sizeBank.opacity=15
            colorBank.fill='white'
            blackPaint.border = None
            redPaint.border = None
            bluePaint.border = None
            greenPaint.border = None
            pinkPaint.border = None
            yellowPaint.border = None
            orangePaint.border = None
            purplePaint.border = None
            lightBluePaint.border = None
            eraser.opacity = 90
        elif(colorBank.fill == 'white'):
            sizeBank.opacity=20
            colorBank.fill='black'
            blackPaint.border = rgb(250, 207, 67)
            redPaint.border = None
            bluePaint.border = None
            greenPaint.border = None
            order = None
            pinkPaint.border = None
            yellowPaint.border = None
            orangePaint.border = None
            purplePaint.border = None
            lightBluePaint.border = None
            eraser.opacity = 90
            
def onMouseRelease(mouseX, mouseY):
        if(smallPaintbrush.contains(mouseX, mouseY) == True):
            smallPaintbrush.opacity = 100
        elif(largePaintbrush.contains(mouseX, mouseY) == True):
            largePaintbrush.opacity = 100
        elif(goldenPaintbrush.contains(mouseX, mouseY) == True):
            largePaintbrush.opacity = 100
        elif(paintBucket.contains(mouseX, mouseY) == True):
            paintBucket.opacity = 100
        elif(eraser.contains(mouseX, mouseY) == True):
            eraser.opacity = 100

def onKeyPress(key):
    if(key == 'enter'):
        Label('Dylan', 345, 350, rotateAngle=-15, font='caveat')
