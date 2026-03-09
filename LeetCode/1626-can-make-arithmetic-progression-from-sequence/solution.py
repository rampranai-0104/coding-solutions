class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        n=len(arr)
        arr.sort()
        diff=0
        l=[]
        for i in range(0,n-1):
            diff=arr[i+1]-arr[i]
            l.append(diff)
        res=all(x==l[0] for x in l)
        return res
