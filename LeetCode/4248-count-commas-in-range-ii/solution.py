class Solution:
    def countCommas(self, n: int) -> int:
        no=n
        a=0
        commas=1
        st=1000
        while st<=no:
            end=st * 1000 -1
            count=max(0,min(no,end)-st+1)
            a+=count * commas
            st*=1000
            commas+=1
        return a
