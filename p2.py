# nama file p2.py 
# Isikan email anda dan copy semua cell code yang dengan komentar #Graded

# untuk revisi dan resubmisi sebelum deadline
# silakan di resubmit dengan nilai variable priority yang lebih besar dari
# nilai priority submisi sebelumnya
# JIKA TIDAK ADA VARIABLE priority DIANGGAP priority=0
priority = 1

#netacad email cth: 'abcd@gmail.com'
email='charlessiagian86@gmail.com'
 
# copy-paste semua #Graded cells YANG SUDAH ANDA KERJAKAN di bawah ini




#Graded

def isPointInCircle(x,y,r,center=(0,0)):
    c=((x-center[0])**2+(y-center[1])**2)
    d=r**2
    if c <= d:
        return True
    else:
        return False

#Graded
import random

def generateRandomSquarePoints(n,length,center=(0,0)):
    minx = center[0]-length/2
    miny = center[1]-length/2
    
    points=[[random.uniform(minx,minx+length), random.uniform(miny,miny+length)] for i in range(n)]
    
    return points 

#Graded

def MCCircleArea(r,n=100,center=(0,0)):
    length=r*2
    pointsInside=0
    for x,y in generateRandomSquarePoints(n,length):
        if (isPointInCircle(x,y,r)) == True:
            pointsInside+=1
    luas_lingkaran=(pointsInside/n)*(length**2)
    return luas_lingkaran

#Graded

def LLNPiMC(nsim,nsample):
    total=0
    for i in range(nsim):
        pi=MCCircleArea(1,nsample)
        total +=pi
    return total/nsim

# Graded

def relativeError(act,est):
    relativeerror=abs(((est-act)/act)*100)
    return relativeerror
