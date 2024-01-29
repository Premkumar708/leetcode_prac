class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        con = {}
        for i in strs:
            sorts="".join(sorted(i))
            if(sorts not in con):
                con[sorts] = [i]
            else:
                print(con[sorts].append(i))           
        return(list(con.values()))        
