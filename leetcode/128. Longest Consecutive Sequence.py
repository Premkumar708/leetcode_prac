class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sets=set(nums)
        curr=0
        for i in sets:
            count=1
            if(i+1 not in sets):
                j = i-1
                while(j in sets):
                    count+=1
                    j-=1
            curr=max(curr,count)    
        return curr    
