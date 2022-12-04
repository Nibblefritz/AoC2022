with open('C:/Users/Kyleq/OneDrive/src/AOC2022/Day3/test.txt') as f:
    whole = f.read().split('\n')

total = 0
# for each rucksack (line in file)
for rucksack in whole:
    # find midway point
    length = len(rucksack)
    half = int(length/2)

    # split out two containers at midway point
    container1 = rucksack[0:half]
    container2 = rucksack[half:]

    # Sort container 1
    container1_chars = sorted(container1)
    unique_container1_chars = []

    # find only unique chars
    for char in container1_chars:
        if char not in unique_container1_chars:
            unique_container1_chars.append(char)

    # Sort container 2
    container2_chars = sorted(container2)

    # find whatever char is the same in the unique chars of container 1
    for char in container2_chars:
        if char in unique_container1_chars:
            common_char = char

    # caluclate priority
    if common_char.islower():
        priority = ord(common_char) - ord('a') + 1
    else:
        priority = ord(common_char) - ord('A') + 27
    total += priority
print(total)