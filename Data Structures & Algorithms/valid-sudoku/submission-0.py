class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        squares = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):

                num = board[r][c]
                if num == ".":
                    continue

                sq_i = (r // 3) * 3 + (c // 3)

                if (num in rows[r] or
                    num in cols[c] or
                    num in squares[sq_i]): 
                    return False
                else:
                    cols[c].add(num)
                    rows[r].add(num)
                    squares[sq_i].add(num)


        # finally
        return True