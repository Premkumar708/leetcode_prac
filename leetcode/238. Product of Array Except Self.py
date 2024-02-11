class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prev = 1
        post = 1
        pre = [1]* (len(nums)+1)
        pos = [1]* (len(nums)+1)
        ans = [1]*len(nums)
        
        for i in range(1,len(pre)):
            prev *=nums[i-1]
            pre[i] = prev
        for j in range(len(pos)-1,0,-1):
            post *= nums[j-1]
            pos[j-1] = post  
        for k in range(1,len(pre)):
            ans[k-1] = pre[k-1]* pos[k]
        return ans  
