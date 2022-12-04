# Driver code
count = 0

with open('C:/Users/Kyleq/OneDrive/src/AOC2022/Day4/test.txt') as f:
    lines = f.read().split('\n')

    for l in lines:
        pair = l.split(',')
        str1 = pair[0]
        str2 = pair[1]

        str1_split = str1.split('-')
        str2_split = str2.split('-')

        str1_start = int(str1_split[0])
        str1_end = int(str1_split[len(str1_split)-1])
        str2_start = int(str2_split[0])
        str2_end = int(str2_split[len(str2_split)-1])
        
        if (str1_start == str1_end):
            list1 = [str1_start]
        else:
            list1 = list(range(str1_start, str1_end + 1))

        if (str2_start == str2_end):
            list2 = [str2_start]
        else:
            list2 = list(range(str2_start, str2_end + 1))

        if(set(list1) & set(list2)):
            count += 1
        
print(count)