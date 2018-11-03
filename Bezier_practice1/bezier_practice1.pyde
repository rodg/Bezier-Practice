xPos = [200,100,600,800]
yPos = [700,100,600,200]
radius = 40
N = 3


def setup():  # setup() runs once
    size(1000, 1000)
    frameRate(240)
    #global basis
    #global num
    #basis, num = getBasis(N, 5)

def draw():  # draw() loops forever, until stopped
    if mousePressed:
        for i in range(0,4):
            if mouseX in range(xPos[i]-(radius),xPos[i]+(radius)):
                if mouseY in range(1000-(yPos[i]+(radius)),1000-(yPos[i]-(radius))):
                    #print(1000-(yPos[i]+(radius/2)),1000-(yPos[i]-(radius/2)))
                    xPos[i] = mouseX
                    yPos[i] = 1000-mouseY
                    
    noStroke()
    background(255)
    fill(255,0,0)
    textSize(32)
    text(frameRate,10,40)
    for i in range(0,4):   #plot control and anchor points
        fill(200,0,0)
        if i is 0 or i is 3:
            fill(0,200,0)
        ellipse(xPos[i], 1000-(yPos[i]), radius, radius)
        
    stroke(0,0,255)
    strokeWeight(5)
    noFill()
    beginShape()
            
    for t in range(0,51):
        t = t/50.0
        xVal = (((1-t)**3)*xPos[0])+((3*t*(1-t)**2)*xPos[1])+((3*(t**2)*(1-t))*xPos[2])+(t**3)*xPos[3]
        yVal = (((1-t)**3)*yPos[0])+((3*t*(1-t)**2)*yPos[1])+((3*(t**2)*(1-t))*yPos[2])+(t**3)*yPos[3]
        vertex(round(xVal),1000-round(yVal))

    endShape()

  
    #noLoop()

#def mouseClicked():
#    if mousePressed:
#        for i in range(0,4):
#            if mouseX in range(xPos[i]-(radius/2),xPos[i]+(radius/2)):
#                if mouseY in range(1000-(yPos[i]+(radius/2)),1000-(yPos[i]-(radius/2))):
                
        
        
def choose(n, k):
    return fact(n)/(fact(k)*fact(n-k))
        
def fact(val):
    if val < 0:
        return -1
    if val <= 1:
        return 1
    else:
        return val*fact(val-1)
    
    
