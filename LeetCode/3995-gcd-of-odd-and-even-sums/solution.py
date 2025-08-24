from math import gcd
class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        odd=[]
        even=[]
        for i in range(1,(n*2)+1):
            if i%2==0:
                even.append(i)
            else:
                odd.append(i)
        no=len(odd)
        sumo=0
        for i in odd:
            sumo+=i
        ne=len(even)
        sume=0
        for i in even:
            sume+=i
        g=gcd(sume,sumo)
        return g
