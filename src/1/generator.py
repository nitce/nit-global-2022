import random

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

def giveRandomInput(minValue=0, maxValue=10**9):
    n = random.randint(minValue, maxValue)
    return (n)

def solveOut(inputs):
    (n) = inputs
    
    ans = ''
    def N(i, j, n):
        if 0 <= j <= n-1:
            if j == 0:
                return '#'
            if j == n-1:
                return '#'
            if j == i:
                return '#'
            return '.'
    
    def I(i, j, n):
        j -= n+1
        if 0 <= j <= n-1:
            if i == 0 and (j != 0 and j != n-1):
                return '#'
            if i == n-1 and (j != 0 and j != n-1):
                return '#'
            if j == n // 2:
                return '#'
            return '.'

    def T(i, j, n):
        j -= 2 * n+2
        if 0 <= j <= n-1:
            if i == 0:
                return '#'
            if j == n // 2:
                return '#'
            return '.'


    for i in range(n):
        for j in range(3 * n + 2):
            c: chr = ''
            if 0 <= j <= n-1:
                c = N(i, j, n)
            if n+1 <= j <= 2*n:
                c = I(i, j, n)
            if 2*n+2 <= j <= 3*n+1:
                c = T(i, j, n)
            if j == n or j == 2 * n + 1:
                c = '.'
            ans += c
        ans += '\n'
    return ans

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
    n = 5
    inputs = (n)
    
    inString = "{}\n".format(
        n
    )
    outString = solveOut(inputs)
    
    count += 1
    makeInputs(inString, count)
    makeOutputs(outString, count)
    
if "Case 2":
    n = 7
    inputs = (n)
    
    inString = "{}\n".format(
        n
    )
    outString = solveOut(inputs)
    
    count += 1
    makeInputs(inString, count)
    makeOutputs(outString, count)

# Automatically add inputs
for i in range(9, 100, 2):
    print(count)
    n = i

    inString = "{}\n".format(
        n
    )
    outString = solveOut(n)

    count += 1
    makeInputs(inString, count)
    makeOutputs(outString, count)


print("Completed!")