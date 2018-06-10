import random
# the grid object, which I use to store griddlers. includes some useful functions for easy use.
class grid(object):
    def __init__(self,name="emptygrid",size=5,option=1):
        self.size = size
        self.name = name
        # options for creating grid: 0=randomize,1=blank
        if option==0:
            self.body = [[random.choice([False,True]) for i in range(size)] for i in range(size)]
        elif option>=1:
            self.body = [[False for i in range(size)] for i in range(size)]

    def __getitem__(self, i):
        return self.body[i]

    def __setitem__(self, key, value):
        self.body[key]=value

    def __str__(self):
        st = ""
        for i in self.body:
             st+="".join([[' ','X'][x] for x in i])+'\n'
        return st

    def row(self,n):
        return self.body[n]

    def col(self,n):
        return[line[n] for line in self.body]

    #fill a spot
    def fill(self,row,col):
        self.body[row][col] = True

    #erase a spot
    def erase(self,row,col):
        self.body[row][col] = False

    #save a grid to grid_storage
    def save(self):
        with open("grid_storage",'r+') as f:
            cont = f.readlines()
            if self.name+'\n' in cont:
                print self.name+" already exists!"
                return
            f.write(self.name+'\n'+str(self.body)+'\n')

    #load a grid from storage into self by name
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

    #return a list of the describing lines of a grid, for testing the solver module
    def tolist(self):
        return [desc_line(i) for i in self]+[desc_line(self.col(i)) for i in range(self.size)]


# the algorithm which describes a line/column, griddler style (distinguishing the "blobs" in aline and counting them)
def desc_line(line):
    c = 0
    res = []
    for i in line:
        if i:
            c+=1
        elif not i and c:
            res.append(c)
            c=0
    if c:
        res.append(c)
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

