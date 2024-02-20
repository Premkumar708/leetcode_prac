class Solution:
    def maxArea(self, height: List[int]) -> int:
        l=0
        r=len(height)-1
        res=0
        while(l<r):
            if(height[r]<=height[l]):
                area= (r-l) * min(height[r],height[l])
                res=max(res,area)
                r-=1
            else:
                area= (r-l) * min(height[r],height[l])
                res=max(res,area)
                l+=1
        return res 
