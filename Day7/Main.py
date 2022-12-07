from aocd import get_data
#Need to set ID in env variable or file
# ~/.config/aocd/token
#53616c7465645f5fe151da2c14f5b436e1d51201cae430101406135a4d3c3d1fa6b1bb26a4ade2385e9dc8b571dcff1a273fa5a9de5976a03e1a70de017fe3f1
import operator

class Directory:
    def __init__(self, name, parent=None):
        self.name = name
        self.files = set()
        self.directories = set()
        self.parent = parent

    @property
    def sub_directories(self):
        sub_directories = {directory.name:directory for directory in self.directories}
        return sub_directories

    @property
    def size(self):
        file_total = sum([file.size for file in self.files])
        sub_directory_total = sum([directory.size for directory in self.directories if directory.size])
        total_size = file_total + sub_directory_total
        return total_size

class File:
    def __init__(self, name, size):
        self.name = name
        self.size = int(size)

class Terminal:
    def __init__(self):
        self.root = Directory('/')
        self.cwd = self.root
        self.stdout = get_data(year=2022, day=7).splitlines()

    def df(self):
        disk_size = 70000000
        space_used = self.root.size
        space_available = disk_size - space_used
        return {'disk_size':disk_size, 'space_used':space_used, 'space_available':space_available}
    
    def touch(self, line):
        x, name = line.split()
        if line.startswith('dir'):
            self.cwd.directories.add(Directory(name,parent=self.cwd))
        else:
            self.cwd.files.add(File(name, x))

    def cd(self, directory_name):
        if directory_name == '..':
            if self.cwd != self.root:
                self.cwd = self.cwd.parent
        elif directory_name =='/':
            self.cwd = self.root
        else: 
            self.cwd = self.cwd.sub_directories[directory_name]

    def find(self, directory, threshold, op):
        directories = [directory] if op(directory.size, threshold) else []

        for subdirectory in directory.directories:
            directories += self.find(subdirectory, threshold, op)
        
        return directories

    def run_cmds(self):
        for line in self.stdout:
            if line.startswith('$ ls'):
                continue

            elif line.startswith('$ cd'):
                directory = line.split()[-1]
                self.cd(directory) 
            else:
                self.touch(line)

class Solution():
    def __init__(self):
        self.terminal = Terminal()
        self.terminal.run_cmds()

    def part_one(self):
        total = sum([directory.size for directory in self.terminal.find(self.terminal.root, 100000, operator.le)])
        return total

    def part_two(self):
        total_space_needed = 30000000
        remaining_space_needed = total_space_needed - self.terminal.df()['space_available']
        directory = min(self.terminal.find(self.terminal.root, remaining_space_needed, operator.ge), key=lambda x: x.size)
        return directory.size

if __name__ == '__main__':
    solution = Solution()
    print(f'Solution for part one: {solution.part_one()}')
    print(f'Solution for part two: {solution.part_two()}')


