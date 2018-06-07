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

#recives a possibility(grid) and tests it
def test_grid(pos):
    lines = pos[:len(pos)/2]
    cols = pos[len(pos)/2:]
    g = grid('tester',len(pos)/2)
    for i in range(len(lines)):
        g[i] = lines[i]
    for i in range(len(cols)):
        if desc_line(g.col(i))!=desc_line(cols[i]):
            return (False,None)
    return (True,g)

#inital try: before dynamic shortening, try to bruteforce the grid by trying all permutations
def bf(lines):
    ops = product(*[permutations(l,len(lines)/2) for l in lines])
    for i in ops:
        (status,grid)=test_grid(i)
        if status:
            return grid
    return "unsuccesful"

a = grid("bla",5,0)
print a
print("\n")
print bf([desc_line(i) for i in a]+[desc_line(a.col(i)) for i in range(a.size)])




