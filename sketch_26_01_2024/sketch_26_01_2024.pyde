q = 1
w= 1
e= 1
def setup():
    size(1000,1000)






def draw():
    global q,w,e

    background(q,w,e)
    rect(20,30,50,50)
    rect(80,30,50,50)
    text(u"фиолетовый"20,30)
    
    
    
    
    
def mouseClicked():
    global q,w,e
    if mouseX > 20 and mouseX < 70 and mouseY > 30 and mouseY < 80:
        q=109
        w= 89
        e= 139
     elif mouseX > 80 and mouseX < 130 and mouseY > 30 and mouseY < 80:
          q=190
          w=229
          e=247
