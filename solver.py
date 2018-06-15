from Grid import *
from itertools import product


# desc is the line hint, n is the length of the line
# returns all legal possibilities of a griddler line
# pretty elegant :)
def permutations(desc, n):
    if not desc:
        return [[False] * n]
    ret = []
    space = n - sum(desc[1:]) - desc[0] + 1
    for i in range(space):
        pos = [False] * i + [True] * desc[0] + [False] * (not i == space - 1)
        perms = permutations(desc[1:], n - desc[0] - i - 1)
        for j in perms:
            ret.append(pos + j)

    return ret


# recives a possibility(grid) and tests it
def test_grid(lines,cols):

    g = grid('tester', len(lines))
    for i in range(len(lines)):
        g[i] = lines[i]
    for i in range(len(cols)):
        if desc_line(g.col(i)) != cols[i]:
            return (False, None)
    return (True, g)



def bf(d):
    ops = product(*d[0])

    for i in ops:
        (status, grid) = test_grid(i,d[1])
        if status:
            return grid
    return "unsuccesful"


'''
------------------------------------------DYNAMIC SHORTENING---------------------------------------
Dynamic shortening allows me to significantly decrease the time it takes to solve a grid.
we use multiple strategies here to filter the permutations and decrease the number of tries neccessary
the logic behind these strategies is explained in the book.
'''

#gets list of bool lists, returns indexes where all the lists share a common True
def findcommon(ls):
    ret =[]
    for i in range(len(ls[0])):
        if(not ls[0][i]):
            continue
        cond = True
        if [ls[j][i] for j in range(len(ls))].count(ls[0][i])==len(ls):
            ret.append(i)
    return ret

#CLEAN UP!
def filterperms(d):
    size = len(d[0])
    lines = d[0]+d[1]
    perms = [permutations(l,size) for l in lines]


    for i,l in enumerate(lines):
        # filtering by full or blank lines
        if l==[] or l == [size]:

            if i>=size:
                perms[:size]=[filter(lambda ls: ls[i-size]==bool(l),line) for line in perms[:size]]
            else:
                perms[size:] = [filter(lambda ls: ls[i] == bool(l), line) for line in perms[size:]]
        # filters by guaranteed spots
        spots = findcommon(perms[i])

        if len(spots) != 0:
            if i>=size:
                for p in spots:
                    perms[p] = filter(lambda ls: ls[i-size],perms[p])
            else:
                for p in spots:
                    perms[p+size] = filter(lambda ls: ls[i], perms[p+size])

    return perms[:size],perms[size:]


def suitable(level,lines,line,cols):
    for i in range(len(line)):
        possiblecols = filter(lambda c: c[0]==line[i],cols[i])
        commoncount =  [c[level] for c in possiblecols].count(True)
        if commoncount==0 or commoncount==len(possiblecols):
            lines = filter(lambda l: l[i]==bool(commoncount),lines)
    return lines


def griddlersproduct(d):
    column_disc = d[1]
    lines,cols = filterperms(d)
    for line in lines[0]:
        ls = [[line]]
        for i in range(1,len(line)):
            ls.append(suitable(i,lines[i],line,cols))
        stat  = bf((ls,column_disc))
        if(stat!="unsuccesful"):
            return stat



a = grid("bla", 15, 0)
print a
print("\n")

print griddlersproduct(a.tolist())
