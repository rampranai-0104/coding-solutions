class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m=len(matrix)
        n=len(matrix[0])
        rc=m*n
        l=0
        r=rc-1
        while l<=r:
            mid=(l+r)//2
            ro=mid//n
            co=mid%n
            if matrix[ro][co]==target:
                return True
            elif matrix[ro][co]<target:
                l=mid+1
            else:
                r=mid-1
        return False
