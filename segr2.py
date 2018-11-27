import os
import shutil
def ins(t,n):
        for filename in os.listdir("allimage/"):
            if filename==n:
                src=os.path.join("allimage/", filename)
                #fdst=os.path.join(t, filename)
                print src
                print t
                shutil.copy(src,t)
#path="/allimage/"
name=""
dst=""
lis=[]
f=open("anno.txt")
lines=f.readlines()
for e in xrange(len(lines)):
    lis=lines[e].split( )
    for ind in xrange(len(lis)):
        name=lis[0]+".ppm"
        if (ord(lis[ind][0])>=48) and (ord(lis[ind][0])<=57):
            dst = lis[ind]+"/"
            ins(dst,name)