import bezier

xPos = [200,100,600,800]
yPos = [700,100,600,200]
radius = 40



def setup():  # setup() runs once
    bezier.hello()
    size(1000, 1000)
    frameRate(240)
    global basis
    global num
    global N
    N = 8
    points = 100

    x = 100
    y = 100
    
    global coordinate
    coordinate = [[x,y]]
    
    for i in range(N+1):
        x += 100
        y += 100
        coordinate.append([x,y])
    
    
    basis, num = getBasis(N, 50)

def draw():  # draw() loops forever, until stopped
    
    if mousePressed:
        for i in range(0,N+1):
            if mouseX in range(coordinate[i][0]-(radius),coordinate[i][0]+(radius)):
                if mouseY in range(1000-(coordinate[i][1]+(radius)),
                                       1000-(coordinate[i][1]-(radius))):
                    coordinate[i][0] = mouseX
                    coordinate[i][1] = 1000-mouseY
                    
    noStroke()
    background(255)
    fill(255,0,0)
    textSize(32)
    text(frameRate,10,40)
    
    for i in range(0,N+1):   #plot control and anchor points
        fill(200,0,0)
        if i is 0 or i is N:
            fill(0,200,0)
        ellipse(coordinate[i][0], 1000-(coordinate[i][1]), radius, radius)
        
    stroke(0,0,255)
    strokeWeight(5)
    noFill()
    beginShape()
    linePlot = []
    for t in range(0, num):
        ver = [0, 0]
        for i in range(0,N+1):
            for index in 0,1:
                ver[index]+=basis[i][t]*coordinate[i][index] #ver[0]=x ver[1]=y
            linePlot.append(ver)
                
    for p in linePlot:
        vertex(round(p[0]),1000-round(p[1]))
    
#    for t in range(0, num):
#        xVer = basis[0][t]*xPos[0]+basis[1][t]*xPos[1]+basis[2][t]*xPos[2]+basis[3][t]*xPos[3]
#        yVer = basis[0][t]*yPos[0]+basis[1][t]*yPos[1]+(basis[2][t])*yPos[2]+basis[3][t]*yPos[3]
#        vertex(round(xVer), 1000-round(yVer))

    endShape()
    #noLoop()
    
def getBasis(n, points):
    #basis' need a length of n a[[a1(t0),a1(t1)...a1(t)],[a2(t0...],...[an(t0)]
    basis = []
    basisN = []
    t = []
    num = 0
    
    for k in range(0,points+1):
        t.append(k/(points*1.0))
        num +=1
        
    for i in range(0,n+1):
        for tVal in t:
            basisN.append( choose(n,i) * ((1-tVal)**(n-i)) * (tVal**i))
        basis.append(basisN) #basis[[f0(t)],[f1(t)],...,[fn(t)]] where fn(t) = [fn(t= 0 to 1)]
        basisN = []
    return basis, num #basis has length n
        
        
        
def choose(n, k):
    return fact(n)/(fact(k)*fact(n-k))
        
def fact(val):
    if val < 0:
        return -1
    if val <= 1:
        return 1
    else:
        return val*fact(val-1)
    
    
