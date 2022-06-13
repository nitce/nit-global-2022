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

print(solveOut(int(input())))