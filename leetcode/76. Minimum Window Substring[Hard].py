class Solution:
    def minWindow(self, s: str, t: str) -> str:
        hashT,hashS = {}, {}
        k = 0
        res, resLen = [-1, -1], float("infinity")
        for i in t:
            hashT[i] = 1 + hashT.get(i,0)
        have,need = 0, len(hashT)        
        for j in range(len(s)):
            v = s[j]
            hashS[v] = 1 + hashS.get(v,0)
            if (v in hashT) and (hashS[v] == hashT[v]):
                have += 1
            print(have == need,have)        
            while(have == need):
                print(j-k+1)
                if( (j-k+1) < resLen):
                    res = [k,j]
                    resLen = j-k+1
                hashS[s[k]] -=1    
                if(s[k] in hashT) and (hashS[s[k]] < hashT[s[k]]):
                        have -=1
                k+=1      
        l,r= res                          
        if( resLen != float('infinity')):
            return s[l:r+1]
        else:
            return ""               
