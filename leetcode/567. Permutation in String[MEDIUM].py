class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        i = 0 
        j = len(s1)-1
        while(j<len(s2)):
            count=0
            for elem in s2[i:j+1]:
                if(elem in s1 and (s1.count(elem) == s2[i:j+1].count(elem))):
                    print(elem)
                    count +=1
                else:
                    break                 
            if(count == len(s1)):
                return True 
                break
            i+=1
            j+=1    
        return False                
