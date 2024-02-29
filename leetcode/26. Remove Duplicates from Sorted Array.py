class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 0
        con = set()
        i=0
        while(i < len(nums)):
            if(nums[i] not in con):
                con.add(nums[i])
                i+=1
                count+=1
            else:
                nums.remove(nums[i])
        return count            
