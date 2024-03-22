class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = 1
        while(count <= k):
            a = nums.pop()
            nums.insert(0,a)
            count+=1
          
      
