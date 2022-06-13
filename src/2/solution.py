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

n = int(input())

print(solveOut((n)))