from ant import Ant
a=Ant()
n=1

def setup():
    size(720,720)
    global a
    
    a.display()
    
def draw():
    global a
    global n
    
    # delay(5)
    
    a.update()
    a.display()
    save("video/"+str(n)+".png")
    print(n)
    n+=1
