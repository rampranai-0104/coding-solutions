class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n=len(citations)
        h=0
        citations.sort(reverse=True)
        for i in range(0,n):
            if citations[i]>=i+1:
                h+=1
        return h
