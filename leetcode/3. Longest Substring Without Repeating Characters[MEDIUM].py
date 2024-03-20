class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        li = set()
        i = 0
        j = 0
        count = 0
        while(j < len(s)):
            if(s[j] not in li):
                li.add(s[j])
            else:
                while(s[j] in li):
                    li.remove(s[i])
                    i+=1
                li.add(s[j])    
            count = max(len(li),count)        
            j+=1        
        return count
