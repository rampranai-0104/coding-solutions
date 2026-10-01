class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        n=len(nums)
        t=[0]*n
        def merge(a,l,m,h):
            i=l
            j=m+1
            k=l
            while i<=m and j<=h:
                if a[i]<=a[j]:
                    t[k]=a[i]
                    i+=1
                else:
                    t[k]=a[j]
                    j+=1
                k+=1
            while i<=m:
                t[k]=a[i]
                i+=1
                k+=1
            while j<=h:
                t[k]=a[j]
                j+=1
                k+=1
            k=l
            while k<=h:
                a[k]=t[k]
                k+=1
        def mergesort(a,l,h):
            if l>=h:
                return 
            m=(l+h)//2
            mergesort(a,l,m)
            mergesort(a,m+1,h)
            merge(a,l,m,h)
        mergesort(nums,0,n-1)
        return nums
