from collections import Counter
from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        nums_count = Counter(nums)
        total_reps = nums_count[val]
        for _ in range(total_reps):
            nums.remove(val)

s = Solution()
print(s.removeElement([0,1,2,2,3,0,4,2],2))
