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
    
    s = bin(n)[2:]
    def check(s):
        if len(s) < 2:
            return False
        if s[:2] != '11':
            return False

        for i in range(len(s)):
            if i == 0:
                if i+1 < len(s) and s[i] != s[i+1]:
                    return False
            elif i == len(s) - 1:
                if i-1 >= 0 and s[i] != s[i-1]:
                    return False
            else:
                if s[i] != s[i-1] and s[i] != s[i+1]:
                    return False
        return True
 
    return 'YES' if check(s) else 'NO'

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
    n = 12
    inputs = (n)
    
    inString = "{}\n".format(
        n
    )
    outString = solveOut(inputs)
    
    count += 1
    makeInputs(inString, count)
    makeOutputs(outString, count)
    
if "Case 2":
    n = 13
    inputs = (n)
    
    inString = "{}\n".format(
        n
    )
    outString = solveOut(inputs)
    
    count += 1
    makeInputs(inString, count)
    makeOutputs(outString, count)
    
if "Case 3":
    n = 399
    inputs = (n)
    
    inString = "{}\n".format(
        n
    )
    outString = solveOut(inputs)
    
    count += 1
    makeInputs(inString, count)
    makeOutputs(outString, count)
    
if "Case 4":
    n = 6
    inputs = (n)
    
    inString = "{}\n".format(
        n
    )
    outString = solveOut(inputs)
    
    count += 1
    makeInputs(inString, count)
    makeOutputs(outString, count)

if "Case 5":
    n = int('10', 2)
    inputs = (n)
    
    inString = "{}\n".format(
        n
    )
    outString = solveOut(inputs)
    
    count += 1
    makeInputs(inString, count)
    makeOutputs(outString, count)

if "Case 6":
    n = int('1', 2)
    inputs = (n)
    
    inString = "{}\n".format(
        n
    )
    outString = solveOut(inputs)
    
    count += 1
    makeInputs(inString, count)
    makeOutputs(outString, count)

if "Case 7":
    n = int('110', 2)
    inputs = (n)
    
    inString = "{}\n".format(
        n
    )
    outString = solveOut(inputs)
    
    count += 1
    makeInputs(inString, count)
    makeOutputs(outString, count)

if "Case 8":
    n = int('101', 2)
    inputs = (n)
    
    inString = "{}\n".format(
        n
    )
    outString = solveOut(inputs)
    
    count += 1
    makeInputs(inString, count)
    makeOutputs(outString, count)



# Automatically add inputs
# This tests are NO cases with high chance
for i in random.choices(range(1, 10**9), k=40):
    n = i

    inString = "{}\n".format(
        n
    )
    outString = solveOut(n)

    count += 1
    makeInputs(inString, count)
    makeOutputs(outString, count)

# This tests are YES cases 100%
for i in range(40):
    s = ""

    def opr(c):
        return c * random.randint(2, 5)

    for step in range(5, 20):
        c = '0' if step % 2 else '1'
        more = opr(c)

        if len(more) + len(s) < 60:
            s += more
        else:
            break

    n = int(s, 2)
    inString = "{}\n".format(n)
    outString = solveOut((n))
    count += 1
    makeInputs(inString, count)
    makeOutputs(outString, count)


print("Completed!")