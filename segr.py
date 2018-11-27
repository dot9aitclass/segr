import os
import shutil
path="/allimage/"
name=""
dst=""
f=open("anno.txt")
lines=f.readlines()
for i in xrange(len(lines)):
    for j in xrange(6):
        name+=(lines[i][j])
    name+=".ppm"
    if lines[i][8]=="\t":
        dst=lines[i][7]+"/"
        #print dst
    elif lines[i][8]==" ":
        dst=lines[i][7]+"/"
        #print dst
    else:
        dst=lines[i][7]+lines[i][8]+"/"
        #print dst
    #else:
     #   dst=lines[i][7]+lines[i][8]+"/"
    for filename in os.listdir("allimage/"):
       if filename==name:
        src=os.path.join("allimage/", filename)
        fdst=os.path.join(dst, filename)
        print src
        print fdst
        shutil.move(src,fdst)
    name=""
