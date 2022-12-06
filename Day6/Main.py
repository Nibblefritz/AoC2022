def find_marker(datastream : str, buffer_len: int) -> int:

    buffer = set() # use sets to create buffers of unique characters
    start = 0
    stop = len(datastream)

    for idx in range(start, stop):   
        # We are basically creating sets (non repeating characters) of length 4 (from the buffer) 
        # but because sets aren't repeating it will only be length 4 if the 4 characters are different. 
        # So even though the first buffer of 4 is 4 long it will remove 1 due to the similar characters
        buffer = set(datastream[idx:idx+buffer_len]) 
        #print(buffer) # uncomment this to see the buffers total
        if len(buffer) == buffer_len: # if the length of our set is equal to the length we need, 
            # then we are going to return the current index + length we need (for the last element of the buffer)
            #print(buffer)
            return idx + buffer_len

with open('C:/Users/Kyleq/OneDrive/src/AOC2022/Day6/test.txt') as f:
    lines = f.read().split('\n')
    #print(lines)

    buffer_part_1 = 4
    buffer_part_2 = 14

    for line in lines:
        index_part_1 = find_marker(line, buffer_part_1)
        index_part_2 = find_marker(line, buffer_part_2)
        print(f'Part 1: {index_part_1}, Part 2: {index_part_2}')
        print('--------------------------')