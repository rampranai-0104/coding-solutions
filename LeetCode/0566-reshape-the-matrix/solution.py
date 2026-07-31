class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m=len(mat)
        n=len(mat[0])
        a=[]
        for i in range(m):
            for j in range(n):
                a.append(mat[i][j])
        if m*n != r*c:
            return mat
        m=[[0 for _ in range(c)] for _ in range(r)]
        k=0
        for i in range(r):
            for j in range(c):
                m[i][j]=a[k]
                k+=1
        return m
