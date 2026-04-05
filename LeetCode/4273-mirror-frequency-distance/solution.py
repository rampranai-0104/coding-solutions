class Solution:
    def mirrorFrequency(self, s: str) -> int:
        fq=Counter(s)
        vis=set()
        ans=0
        def mirror(c):
            if c.isdigit():
                return chr(ord('0')+(9-(ord(c)-ord('0'))))
            else:
                return chr(ord('a')+(25-(ord(c)-ord('a'))))
        for c in fq:
            if c in vis:
                continue
            m=mirror(c)
            ans+=abs(fq[c]-fq.get(m,0))
            vis.add(c)
            vis.add(m)
        return ans
