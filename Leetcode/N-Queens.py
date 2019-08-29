'''
The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.

Example:

Input: 4
Output: [
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above.

'''
import copy

class Solution:
    def solveNQueens(self, n):
        board = [['.'] * n for i in range(n)]
        res = []
        self.solve(board, 0, n, res)
        return res #self.printSolution(res)
    
    def solve(self, board, col, n, res):
        if col == n:
            #path = copy.deepcopy(board)
            r = self.printSolution(board)
            res.append(r)
            print(len(res))
            return
        # check every row, col for every row
        for i in range(n):
            if self.isValid(board, i, col):
                board[i][col] = 'Q'
                #import pdb; pdb.set_trace()
                self.solve(board, col + 1, n, res)
                board[i][col] = '.'
    
    def isValid(self, board, row, col):
        n = len(board)
        # horizontal check
        i = 0
        while i < n and row < n:
            if board[row][i] == 'Q':
                return False
            i += 1

        # Upper left diagonal
        i = 0
        while i < n and row - i >= 0  and col - i >= 0:
            if board[row - i][col - i] == 'Q':
                return False
            i += 1
        
        # Lower left diagonal
        i = 0
        while i < n and row + i < n and col - i >= 0:
            if board[row + i][col - i] == 'Q':
                return False
            i += 1

        return True
    
    def printSolution(self, result):
        r = []
        for row in result:
            r.append(''.join(row))
        return r


if __name__ == "__main__":
    print(Solution().solveNQueens(4))