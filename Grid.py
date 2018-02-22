import random
# the grid object, which I use to store griddlers. includes some useful functions for easy use.
class grid(object):
    def __init__(self,size,option):
        self.size = size

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
