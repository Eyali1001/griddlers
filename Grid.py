import random
# the grid object, which I use to store griddlers. includes some useful functions for easy use.
class grid(object):
    def __init__(self,name="emptygrid",size=5,option=1):
        self.size = size
        self.name = name
        # options for creating grid: 0=randomize,1=blank
        if option==0:
            self.body = [[random.choice(['X',' ']) for i in range(size)] for i in range(size)]
        elif option>=1:
            self.body = [[" " for i in range(size)] for i in range(size)]



    def draw(self):
        for i in self.body:
            print "".join(i)

    def row(self,n):
        return self.body[n]

    def col(self,n):
        return[line[n] for line in self.body]

    def fill(self,row,col):
        self.body[row][col] = 'X'

    def erase(self,row,col):
        self.body[row][col] = ' '

    def save(self):
        with open("grid_storage",'r+') as f:
            cont = f.readlines()
            if self.name+'\n' in cont:
                print self.name+" already exists!"
                return
            f.write(self.name+'\n'+str(self.body)+'\n')

    def load(self,name):
        self.name = name
        with open("grid_storage") as f:
            content = f.readlines()
        for i in range(len(content)):
            if content[i].strip()==name:
                self.body=eval(content[i+1].strip())
                self.size=len(self.body)
                return
        print "didn't find grid"
# the algorithm which describes a line/column, griddler style (distinguishing the "blobs" in aline and counting them)
def desc_line(line):
    c = 0
    res = []
    for i in line:
        if i=='X':
            c+=1
        elif i==' ' and c!=0:
            res+=str(c)
            c=0
    if c!=0:
        res+=str(c)
    return res

def compare(g1,g2):
    assert g1.size == g2.size
    b1 = g1.body
    b2= g2.body
    for i,j in zip(b1,b2):
        for x,y in zip(i,j):
            if x!=y:
                return False
    return True
