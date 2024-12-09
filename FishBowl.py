Rect(0, 0, 400, 400, fill='mediumOrchid', opacity=20)

table = Group(
Oval(205, 315, 360, 60, fill='SaddleBrown'),
Oval(205, 325, 360, 70, fill='SaddleBrown'),
Oval(205, 335, 360, 60, fill='SaddleBrown'),
Rect(40, 345, 20, 55, fill='SaddleBrown'),
Rect(350, 345, 20, 55, fill='SaddleBrown'),
Rect(75, 345, 16, 55, fill='SaddleBrown', opacity=85),
Rect(319, 345, 16, 55, fill='SaddleBrown', opacity=85)
    )

bowl = Group(
Circle(200, 200, 130, fill='white', opacity=50),
Oval(200, 80, 170, 30, fill='white', opacity=60)
    )
    
water = Polygon(
90, 133, 
313, 133,
321, 151,
327, 173,
332, 192, 
331, 215,
325, 236,
319, 252,
311, 263,
87, 263,
76, 243,
73, 225,
70, 202,
72, 179,
80, 154,
85, 145,
86, 142,
fill='blue', opacity=20)

def drawSeaGrass(mouseX, mouseY):
    Polygon(
    mouseX, mouseY,
    mouseX-4, mouseY-18,
    mouseX, mouseY-32,
    mouseX+9, mouseY-55,
    mouseX, mouseY-66,
    mouseX+16, mouseY-59,  
    mouseX+12, mouseY-44, 
    mouseX+8, mouseY-33,  
    mouseX+2, mouseY-17,  
    mouseX+2, mouseY,
    fill='green'
    )
    
drawSeaGrass(116, 263)
drawSeaGrass(128, 263)
drawSeaGrass(104, 263)

coral = Group(
    Oval(275, 251, 40, 20, rotateAngle=45, fill='Coral'),
    Oval(279, 231, 40, 22, rotateAngle=335, fill='Coral'),
    Oval(283, 204, 51, 18, rotateAngle=65, fill='Coral'),
    Circle(264, 252, 6, fill='red'),
    Circle(285, 234, 7, fill='red'),
    Circle(279, 213, 4.8, fill='red'),
    Circle(285, 190, 6.5, fill='red')
    )

ground = Polygon(
87, 263,
311, 263,
294, 292,
278, 306,
262, 317,
238, 326,
220, 330,
205, 332,
183, 330,
156, 324,
145, 316,
130, 310,
112, 297,
102, 285,
fill = 'LightGoldenRodYellow')

fish = Group(
Oval(200, 200, 50, 40, fill='orange'),
Polygon(217, 200, 232, 175, 232, 225, fill='orange'),
Circle(190, 195, 4)
    )
    
bubbles = Group(
    Circle(165, 187, 5, fill='blue', border='darkBlue', opacity=0),
    Circle(179, 176, 5, fill='blue', border='darkBlue', opacity=0),
    Circle(168, 163, 5, fill='blue', border='darkBlue', opacity=0)
    )

def onMouseMove(mouseX, mouseY):
    if(mouseY > 153):
        if(mouseX > 110):
            if(mouseX < 293):
                if(water.contains(mouseX, mouseY) == True):
                    fish.centerX = mouseX
                    fish.centerY = mouseY
    
def onMousePress(mouseX, mouseY):
    if(mouseY >= 188):
        if(mouseX >= 125):
            if(mouseX < 293):
                if(water.contains(mouseX, mouseY) == True):
                    bubbles.centerX = mouseX-30
                    bubbles.centerY = mouseY-25
                    bubbles.opacity = 20

def onStep():
    if(bubbles.opacity > 0):
        bubbles.opacity -= 2
        bubbles.centerY -= 1
