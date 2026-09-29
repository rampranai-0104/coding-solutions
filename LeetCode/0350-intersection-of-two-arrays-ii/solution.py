class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        m=len(nums1)
        n=len(nums2)
        l=[]
        f={}
        for i in range(n):
            if nums2[i] not in f:
                f[nums2[i]]=1
            else:
                f[nums2[i]]+=1
        for i in range(m):
            if nums1[i] in f and f[nums1[i]]>0:
                l.append(nums1[i])
                f[nums1[i]]-=1
        return l
