class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = 0
        j = 0
        temp=[]
        while( i < m and j < n):
            if(nums1[i] < nums2[j]):
                temp.append(nums1[i])
                i+=1
            elif(nums1[i] == nums2[j]):
                temp.append(nums2[j])
                j+=1
            else:
                temp.append(nums2[j])
                j+=1        
        if(i >= m):
            temp=temp+nums2[j:n]
        else:
            print(i,j)
            temp=temp+nums1[i:m]
        for k in range(len(temp)):
            nums1[k] = temp[k]
        return nums1    
