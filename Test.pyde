x1 = 20
y1 = 600
x2 = 600
y2 = 20

def setup():
    size(620, 620)
    background(255, 255, 255)
    stroke(220, 200, 200)
    frameRate(20)
    
def draw():
    global x1
    global y1
    global x2
    global y2

    line(x1, y1, x2, y2)
    
    if x1 < 600:
        x1 = x1 + 10
        x2 = x2 - 10
    else:
        x1 = 20
        y1 = 600
        x2 = 600
        y2 = 20
    
    '''
    for i in range(0, 60):
        offset = i * 10
        coloroffset = i * 4
        stroke(200 - coloroffset, 120, 50 + coloroffset)
        line(20 + offset, 600, 600 - offset, 20)
    '''
