input_file = open('C:/Users/Kyleq/OneDrive/src/AOC2022/Day2/test.txt', "r")

score = 0

for s in input_file.readlines():
    opp, outcome = ord(s[0]), ord(s[2])
    score += 1 + (opp + outcome + 2) % 3 + 3 * ((outcome + 2) % 3)

print("AOC 2022: day 2, part 2: {}".format(score))

input_file.close()