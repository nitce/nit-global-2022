import random

# grid = """########
# #..#####
# #..#####
# ########
# ###...##
# ########
# ###.####
# ########""".split('\n')
# k = 3

# Utility functions
def arrayToString(arr: list):
    result: str = ""

    for i in range(len(arr)):
        if i + 1 < len(arr):
            result += "{}".format(arr[i])
        else:
            result += "{}".format(arr[i])
    
    return result
    
# Test-case generator template

count = 0

def giveRandomInput():
    grid =  [ [ '.' for j in range(8) ] for i in range(8) ]
    k = random.randint(1, 6)
    t = random.randint(0, 64)

    ind = set()
    while len(ind) < t:
        ind.add(random.randint(0, 63))
    
    ind = list(ind)
    ind = list(map(lambda x: (x // 8, x % 8), ind))

    for (i,j) in ind:
        grid[i][j] = '#'
    
    return (grid, k)

def solveOut(inputs):
    (grid, k) = inputs

    def bt(grid, k, i, j, row_flag, col_bitmask):
        if k == 0:
            return 1
        if i >= 8:
            return 0
        if j >= 8:
            return bt(grid, k, i+1, 0, False, col_bitmask)
        

        if grid[i][j] == '#':
            col_bitmask[j] = False
            return bt(grid, k, i, j+1, False, col_bitmask)
        if row_flag:
            return bt(grid, k, i, j+1, row_flag, col_bitmask)
        if col_bitmask[j]:
            return bt(grid, k, i, j+1, row_flag, col_bitmask)
        
        ans = 0

        skp = bt(grid, k, i, j+1, row_flag, col_bitmask) # skip
        row_flag = True
        col_bitmask[j] = True
        put = bt(grid, k-1, i, j+1, row_flag, col_bitmask) # put rook
        row_flag = False
        col_bitmask[j] = False

        ans = (skp % 1001) + (put % 1001)
        return ans % 1001

    return str(bt(grid, k, 0, 0, False, [False] * 8) % 1001)

# print(solveOut((grid, k)))

def makeInputs(inString, cnt):
    path = "./in/input" + str(cnt) + ".txt"
    f = open(path, "w")
    f.write(inString)
    f.close()

def makeOutputs(outString, cnt):
    path = "./out/output" + str(cnt) + ".txt"
    f = open(path, "w")
    f.write(outString)
    f.close()

# Manually add some inputs
if "Case 1":
    
    grid = """########
#..#####
########
########
########
########
########
########"""
    k = 1
    
    inString = "{}\n{}\n".format(
        k, grid
    )
    grid = grid.split('\n')
    grid = [ [ row[i] for i in range(len(row)) ] for row in grid ]

    inputs = (grid, k)
    outString = solveOut(inputs)
    
    count += 1
    makeInputs(inString, count)
    makeOutputs(outString, count)
    
if "Case 2":
    
    grid = """########
#..#####
#..#####
########
###...##
########
########
########"""
    k = 3
    
    inString = "{}\n{}\n".format(
        k, grid
    )
    grid = grid.split('\n')
    grid = [ [ row[i] for i in range(len(row)) ] for row in grid ]
    inputs = (grid, k)
    outString = solveOut(inputs)
    
    count += 1
    makeInputs(inString, count)
    makeOutputs(outString, count)
    
# Automatically add inputs
# This tests are NO cases with high chance
for i in range(50):
    inputs = giveRandomInput()
    grid, k = inputs

    gridStr = '\n'.join([ ''.join(grid[i]) for i in range(8) ])

    inString = "{}\n{}\n".format(
        k, gridStr
    )
    outString = solveOut(inputs)

    count += 1
    makeInputs(inString, count)
    makeOutputs(outString, count)


print("Completed!")

