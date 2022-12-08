import numpy as np

forest = np.genfromtxt('C:/Users/Kyleq/OneDrive/src/AOC2022/Day8/test.txt', dtype=int, delimiter=1)
print(forest)

counter = 0
forest_line_counter = 0

def is_visible(xpos, ypos):
    visible_top = False
    visible_bottom = False
    visible_right = False
    visible_left = False

    #Checking Top
    if forest[xpos - 1][ypos] < forest[xpos][ypos]:
        visible_top = True
        for x in range(xpos - 1, -1, -1):
            if forest[x][ypos] >= forest[xpos][ypos]:
                visible_top = False
                break
    #Checking Left
    if forest[xpos][ypos - 1] < forest[xpos][ypos]:
        visible_left = True
        for y in range(ypos - 1, -1, -1):
            if forest[xpos][y] >= forest[xpos][ypos]:
                visible_left = False
                break
    #Checking Right
    if forest[xpos][ypos + 1] < forest[xpos][ypos]:
        visible_right = True
        for i in range(ypos + 1, len(forest[xpos])):
            if forest[xpos][i] >= forest[xpos][ypos]:
                visible_right = False
                break
    #Checking Bottom
    if forest[xpos + 1][ypos] < forest[xpos][ypos]:
        visible_bottom = True
        for j in range(xpos + 1, len(forest)):
            if forest[j][ypos] >= forest[xpos][ypos]:
                visible_bottom = False
                break

    if visible_top == True or visible_bottom == True or visible_left == True or visible_right == True:
        return True
    else:
        return False

for x in range(len(forest)):
     for y in range(len(forest[x])):
        #print(forest[x][y])
        if x != 0 and y != 0 and x != (len(forest) - 1) and y != (len(forest[x]) - 1):
            #if top is greater than current val, add one to counter. Else: loop through until you find lower value or until end of index. 
            check_pos = is_visible(x, y)
            if check_pos == True:
                counter += 1
        else:
            forest_line_counter += 1

print(counter + forest_line_counter)