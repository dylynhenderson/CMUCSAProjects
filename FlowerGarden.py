# Landscape
app.background = gradient(rgb(111, 193, 227), rgb(112, 192, 230), rgb(35, 133, 186), start='right-top')
Rect(0, 330, 400, 70, fill=gradient('green', 'seaGreen', start='bottom'))

ladybug = Group(
    Oval(200, 200, 35, 45, fill='red'),
    )

def drawFlower(x, y, color):
    Line(x, y, x, 330, fill='green', lineWidth=3)
    Oval(x, y-40, 25, 35, fill=color)
    Oval(x+25, y-25, 25, 35, rotateAngle=45, fill=color)
    Oval(x+40, y, 25, 35, rotateAngle=90, fill=color)
    Oval(x+25, y+25, 25, 35, rotateAngle=135, fill=color)
    Oval(x, y+40, 25, 35, rotateAngle=180, fill=color)
    Oval(x-25, y+25, 25, 35, rotateAngle=225, fill=color)
    Oval(x-40, y, 25, 35, rotateAngle=270, fill=color)
    Oval(x-25, y-25, 25, 35, rotateAngle=315, fill=color)
    Circle(x, y, 20, fill='yellow')
    
def onMousePress(mouseX, mouseY):
    ladybug.visible=False
    if(mouseY < 110):
        drawFlower(mouseX, mouseY, 'orange')
    elif(mouseY < 220):
        drawFlower(mouseX, mouseY, 'blue')
    elif(mouseY < 330):
        drawFlower(mouseX, mouseY, 'pink')
        
def onMouseRelease(mouseX, mouseY):
    ladybug.visible = True
    
def onMouseMove(mouseX, mouseY):
    if(mouseY < 330):
        ladybug.centerX = mouseX
        ladybug.centerY = mouseY
    
pass
