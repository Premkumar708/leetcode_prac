class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if(len(nums) == 1):
            return len(nums)
        else:    
            i = 0
            j = 1   
            while(j !=(len(nums))):
                if(nums[i] == nums[j]):
                    nums.remove(nums[j])
                else:
                    i=j
                    j+=1
            return(len(nums))
                                
