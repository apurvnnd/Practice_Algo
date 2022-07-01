from collections import Counter

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums_count = Counter(nums)
        unique_nums = list(nums_count.keys())
        for i in range(len(unique_nums)):
            nums[i]=unique_nums[i]
        return len(unique_nums)