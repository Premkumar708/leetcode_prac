class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        checker = {}
        for i in range(len(s)):
            if(t[i] not in checker):
                if(s[i] not in checker.values()):
                    checker[t[i]] = s[i]
                else:
                    return False
            else:
                if(s[i] != checker[t[i]]):
                    return False
        return True
