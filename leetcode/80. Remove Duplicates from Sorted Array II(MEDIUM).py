class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 1
        i,j = 0 , 1
        while(j != len(nums)):
            if(count<=1 and nums[i] == nums[j]):
                j+=1
                count+=1
            elif(nums[i] == nums[j]):
                nums.remove(nums[j])
            else:
                i=j
                j+=1
                count=1        
        return len(nums)              
