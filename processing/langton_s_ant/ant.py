def dir(val):
    if val==0:
        return [0,1]
    if val==1:
        return [1,0]
    if val==2:
        return [0,-1]
    if val==3:
        return [-1,0]


class Ant:
    def __init__(t):
        t.data=[]
        t.l=72
        t.w=72
        
        for i in range(t.l):
            t.data.append([])
            for j in range(t.w):
                t.data[i].append(0)
                
        t.ant=[floor(t.l/2),floor(t.w/2)]
        t.res=[720/t.l,720/t.w]
        
        t.d=3
        
    def display(t):
        for i in range(t.l):
            for j in range(t.w):
                b=t.data[i][j]
                if b==0:
                    fill(255)
                    rect(i*t.res[0],j*t.res[1],t.res[0],t.res[1])
                if b==1:
                    fill(255,0,0)
                    rect(i*t.res[0],j*t.res[1],t.res[0],t.res[1])
                    
        fill(0)
        rect(t.ant[0]*t.res[0],t.ant[1]*t.res[1],t.res[0],t.res[1])
        
    def update(t):
        if t.data[t.ant[0]][t.ant[1]]==0:
            t.d+=1
            t.data[t.ant[0]][t.ant[1]]=1
            
        else:
            t.d-=1
            t.data[t.ant[0]][t.ant[1]]=0
            
        t.d=t.d%4
        di=dir(t.d)
        t.ant[0]+=di[0]
        t.ant[1]-=di[1]
