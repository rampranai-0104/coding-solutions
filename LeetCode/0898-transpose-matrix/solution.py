class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m=len(matrix)
        n=len(matrix[0])
        a=[[0 for _ in range(m)] for _ in range(n)]
        j=0
        for i in range(n):
            for j in range(m):
                a[i][j]=matrix[j][i]
        return a
