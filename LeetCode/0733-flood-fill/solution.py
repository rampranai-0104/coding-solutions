class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        org=image[sr][sc]
        m=len(image)
        n=len(image[0])
        if org==color:
            return image
        def flood(i,j):
            if i<0 or j<0 or i>=m or j >=n:
                return 
            if image[i][j]!=org:
                return 
            image[i][j]=color
            flood(i-1,j)
            flood(i+1,j)
            flood(i,j-1)
            flood(i,j+1)
        flood(sr,sc)
        return image            
