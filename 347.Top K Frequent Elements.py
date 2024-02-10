class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        maps={}
        revmaps = {}
        for o in nums:
            if(o not in maps):
                maps[o] = nums.count(o)
        for j,l in maps.items():
            if l not in revmaps:
                revmaps[l] = [j]
            else:
                revmaps[l].append(j)       
        li=[]
        for i in range(len(nums),0,-1):
            if i in revmaps and len(li) < k :
                li.extend(revmaps[i])
        return li
