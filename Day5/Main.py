def read_input(path: str = 'C:/Users/Kyleq/OneDrive/src/AOC2022/Day5/test.txt'):
    with open(path) as file_in:

        # get the crates on the ship
        crates = []
        line = ' '
        while line:
            # get the line
            line = file_in.readline().rstrip()

            # check for empty line - By breaking here we will move on out of this while loop onto restructure crates and commands loop
            if not line:
                break

            #print(line[1::4])
            line = list(line[1::4]) # line[1::4] is saying take the 1 element every four steps so 'n', '=0 n=1 '=2 ,=3 space=4 
            #print(line)
            crates.append(line)

        # restructure the crates
        tmp = [[] for _ in range(len(crates[-1]))]
        for line in crates[:-1]: # we are going from the last line -1 which means we are removing the index number line from consideration
            for idx, ele in enumerate(line):
                if ele != ' ':
                    tmp[idx].append(ele) # this is removing the white space stack elements
        #print(tmp)
        crates = [list(reversed(stack)) for stack in tmp] # we are reversing our reversal from earlier
        #print(crates)

        # get the commands
        commands = []
        for line in file_in.readlines():
            line = line.rstrip()
            commands.append(list(int(ele) for ele in line.split()[1::2])) # here we specify ele is an int and then we are taking our line and starting at element 1 and then only taking every second element (all the numbers)
    return crates, commands


def main1():

    # get the input (get's the crates[] and commands[])
    crates, commands = read_input()

    # go through the instructions where the commands numbers are defined as number, source, destination
    for number_of_crates, source_stack, destination_stack in commands:

        # extend the crates to the destination stack. The extend() method adds the specified list elements (or any iterable) to the end of the current list.
        crates[destination_stack-1].extend(reversed(crates[source_stack-1][-number_of_crates:]))

        # delete the crates that we moved from the source stack
        crates[source_stack-1] = crates[source_stack-1][:-number_of_crates]

    print(f'The result for solution 1 is: {"".join(ele[-1] for ele in crates)}')


def main2():

    # get the input
    crates, instructions = read_input()

    # go through the instructions
    for number_of_crates, source_stack, destination_stack in instructions:
        # extend the destination
        crates[destination_stack - 1].extend(crates[source_stack - 1][-number_of_crates:])

        # delete the source
        crates[source_stack - 1] = crates[source_stack - 1][:-number_of_crates]

    print(f'The result for solution 2 is: {"".join(ele[-1] for ele in crates)}')


if __name__ == '__main__':
    main1()
    main2()
