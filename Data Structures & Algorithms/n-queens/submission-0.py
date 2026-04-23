class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        maze = [['.'] * n for _ in range(n)]

        def solve(row, queens, pos, neg):
            if row == len(maze):
                ans = ["".join(row) for row in maze]
                res.append(ans)
                print(pos, neg)
                return
             
            for idx in range(len(maze)):
                p = idx + row
                n = idx - row

                if idx in queens or p in pos or n in neg:
                    continue
                
                queens.add(idx)
                pos.add(p)
                neg.add(n)
                maze[row][idx] = "Q"
                solve(row + 1, queens, pos, neg)
                maze[row][idx] = "."
                queens.discard(idx)
                pos.discard(p)
                neg.discard(n)

        solve(0, set(), set(), set())
        return res