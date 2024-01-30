class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sets=set(nums)
        length=0
        for i in sets:
            if (i - 1) not in sets:
                count = 0
                while (i + count) in sets:
                    count += 1
                length = max(count,length)
        return length 