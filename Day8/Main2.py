import numpy as np

forest = np.genfromtxt('C:/Users/Kyleq/OneDrive/src/AOC2022/Day8/test.txt', dtype=int, delimiter=1)
#print(forest)

tree_line = []

#~~~~~~~~~Part 2

def tree_view(xpos, ypos):
    tree_limit_top = 0
    tree_limit_bottom = 0
    tree_limit_right = 0
    tree_limit_left = 0

    #Checking Top
    for x in range(xpos - 1, -1, -1):
        if forest[x][ypos] < forest[xpos][ypos]:
            tree_limit_top += 1
        elif forest[x][ypos] >= forest[xpos][ypos]:
            tree_limit_top += 1
            break
    #Checking Left
    for y in range(ypos - 1, -1, -1):
        if forest[xpos][y] < forest[xpos][ypos]:
            tree_limit_left  += 1
        elif forest[xpos][y] >= forest[xpos][ypos]:
            tree_limit_left += 1
            break
    #Checking Right
    for i in range(ypos + 1, len(forest[xpos])):
        if forest[xpos][i] < forest[xpos][ypos]:
            tree_limit_right += 1
        elif forest[xpos][i] >= forest[xpos][ypos]:
            tree_limit_right += 1
            break
    #Checking Bottom
    for j in range(xpos + 1, len(forest)):
        if forest[j][ypos] < forest[xpos][ypos]:
            tree_limit_bottom += 1
        elif forest[j][ypos] >= forest[xpos][ypos]:
            tree_limit_bottom += 1
            break

    return (tree_limit_top * tree_limit_left * tree_limit_bottom * tree_limit_right)

for x in range(len(forest)):
     for y in range(len(forest[x])):
        if x != 0 and y != 0 and x != (len(forest) - 1) and y != (len(forest[x]) - 1):
            tree_line.append(tree_view(x, y))


print(max(tree_line))