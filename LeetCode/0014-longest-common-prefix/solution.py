class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ml=len(min(strs,key=len))
        for i in range(ml):
            ch=strs[0][i]
            for j in range(1,len(strs)):
                if strs[j][i]!=ch:
                    return strs[0][:i]
        return strs[0][:ml]       

