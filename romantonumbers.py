class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        x=0
        i=0
        while(i<len(s)):
            if ( i != len(s)-1) and (roman[s[i]]<roman[s[i+1]]):
                x+=roman[s[i+1]] - roman[s[i]]
                i+=1
            else:
                x+=roman[s[i]]
            i+=1        
        return x              
        