class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        m=len(ransomNote)
        n=len(magazine)
        freq={}
        for i in magazine:
            if i in freq:
                freq[i]=freq[i]+1
            else:
                freq[i]=1
        for i in range(m):
            ch=ransomNote[i]
            if ransomNote[i] not in freq:
                return False
            elif freq[ch]==0:
                return False
            else:
                if freq[ch]>0:
                    freq[ch]=freq[ch]-1
        return True
