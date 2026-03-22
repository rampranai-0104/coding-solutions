class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        rav=nums1[:]
        nums1.sort()
        so=float('inf')
        te=nums1[0]%2==0
        for x in nums1:
            if (x%2==1 and te) or (x%2==0 and not te):
                if so>=x:
                    return False
            if x%2==1:
                so=min(so,x)
        return True
