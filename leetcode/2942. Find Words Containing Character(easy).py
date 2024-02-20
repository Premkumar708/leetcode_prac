class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        li=[]
        for i,word in enumerate(words):
            if(x in word):
                li.append(i)
        return li            
