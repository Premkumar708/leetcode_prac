class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sets = set()
        i = 0
        count = 0
        for j in range(len(s)):
            while s[j] in sets:
                sets.remove(s[i])
                i+=1
            sets.add(s[j])
            count = max(count,(j-i+1))
        return count 