import os
import shutil
def create():
    for i in xrange(0,15):
        path="./"+str(i)
        print path
        os.makedirs(path)
   
def delete():
    for i in xrange(0,15):
        path="./"+str(i)
        print path
        shutil.rmtree(path)
create()