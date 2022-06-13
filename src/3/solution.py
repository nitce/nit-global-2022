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

k =int(input())
s = [ input() for i in range(8) ]
grid = [ [ s[i][j] for j in range(8) ] for i in range(8) ]
print(bt(grid, k, 0, 0, False, [False] * 8))
