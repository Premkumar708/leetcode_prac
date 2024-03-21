class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        l = 0
        res=0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r],0)
            if((r-l+1) - max(count.values()) <= k):
                temp = r - l + 1
            else:
                count[s[l]] = count[s[l]] -  1
                l+=1
                temp = r - l + 1
            res=max(res,temp)
        return res    
