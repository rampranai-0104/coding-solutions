class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n=len(nums)
        freq={}
        for i in nums:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        res=[]
        sf=sorted(freq.items() , key =lambda x:x[1],reverse=True)
        for i in range(k):
            res.append(sf[i][0])
        return res
