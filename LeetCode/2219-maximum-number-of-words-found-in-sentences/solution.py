class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        count=0
        for i in sentences:
            spaces=i.split(" ")
            sl=len(spaces)
            if sl>count:
                count=sl
        
        return count

            
