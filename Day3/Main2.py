with open('C:/Users/Kyleq/OneDrive/src/AOC2022/Day3/test.txt') as f:
    group = f.read().split('\n')

total = 0
rownum = 0

# split the entire file into groups of 3 rows
for row in group:
    if rownum == 0:
        a = row
        rownum += 1
        continue
    if rownum == 1:
        b = row
        rownum += 1
        continue
    if rownum == 2:
        c = row
        rownum = 0

        # Combine all the rows into one group
        s = a + b + c
        # print(s)

        # for each character in group we are going to check if that char is in a, b, and c
        for x in s:
            if x in a and x in b and x in c:
                common_char = x
                # print(common_char)
                break

        # finally get the priority of the common_char value
        if common_char.islower():
            priority = ord(common_char) - ord('a') + 1
        else:
            priority = ord(common_char) - ord('A') + 27
        total += priority
print(total)