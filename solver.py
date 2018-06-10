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
def test_grid(pos):
    lines = pos[:len(pos) / 2]
    cols = pos[len(pos) / 2:]
    g = grid('tester', len(pos) / 2)
    for i in range(len(lines)):
        g[i] = lines[i]
    for i in range(len(cols)):
        if desc_line(g.col(i)) != cols[i]:
            return (False, None)
    return (True, g)


# inital try: before dynamic shortening, try to bruteforce the grid by trying all permutations
def bf(lines):
    a = filterperms(lines)[:len(lines)/2]
    print a
    ops = product(*filterperms(lines)[:len(lines)/2])

    for i in ops:

        (status, grid) = test_grid(list(i)+lines[len(lines)/2:])
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
def filterperms(lines):
    size = len(lines)/2
    perms = [permutations(l,size) for l in lines]


    for i,l in enumerate(lines):
        #filtering by full or blank lines
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
    #print (sum([len(perms[i]) for i in range(len(perms))]))
    return perms
a = grid("bla", 10, 0)
print a
print("\n")
print bf(a.tolist())
