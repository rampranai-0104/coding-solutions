class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m=len(matrix)
        n=len(matrix[0])
        l=0
        r=n-1
        while l<m and r>=0:
            if matrix[l][r]==target:
                return True
            elif matrix[l][r]<target:
                l=l+1
            else:
                r=r-1
        return False

