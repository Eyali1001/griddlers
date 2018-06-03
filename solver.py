# desc is the line hint, n is the length of the line
# returns all legal possibilities of a griddler line
# pretty elegant :)


def permutation(desc, n):
    if not desc:
        return [[False] * n]
    ret = []
    space = n - sum(desc[1:]) - desc[0] + 1
    for i in range(space):
        pos = [False] * i + [True] * desc[0] + [False] * (not i == space - 1)
        perms = permutation(desc[1:], n - desc[0] - i - 1)
        for j in perms:
            ret.append(pos + j)

    return ret


print permutation([3, 1], 6)
