# You are given an m x n integer matrix matrix with the following two properties:

# Each row is sorted in non-decreasing order.
# The first integer of each row is greater than the last integer of the previous row.
# Given an integer target, return true if target is in matrix or false otherwise.

# You must write a solution in O(log(m * n)) time complexity.

#SOLUTION 1: Bin Search on rows first and check if in bounds,
# then bin search on the row itself

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        lr, rr = 0, m - 1

        while lr <= rr:
            mr = lr + (rr - lr) // 2
            row = matrix[mr]

            if target < row[0]: rr = mr-1
            elif target > row[n-1]: lr = mr+1
            else: 
                l, r = 0, len(row) - 1
                while l <= r:
                    m = l + (r - l) // 2
                    if row[m] == target: return True
                    elif target < row[m]: r = m-1
                    else: l = m+1
                return False
        return False
        

# SOLUTION 2: Bin search on whole matrix at once

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        l, r = 0, m*n - 1

        while l <= r:
            m = l + (r - l) // 2
            row, col = divmod(m, n)
            val = matrix[row][col]

            if target == val: return True
            elif target > val: l = m+1
            else: r = m-1
        return False
        