class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        if len(nums)%k!=0:
            return False
        nums = sorted(nums)
        nums_count = Counter(nums)
        i=0
        el=0
        total_reps=0 
        while nums_count.keys():
            if i<k:
                if i==0:
                    el = min(nums_count.keys())
                    total_reps=nums_count[el]
                    removeKeysWithZeroValue(total_reps, nums_count, el)
                    i+=1
                    if not nums_count.keys() and k!=1:
                        return False
                else:
                    el = el+1
                    i+=1
                    if el in nums_count.keys():
                        removeKeysWithZeroValue(total_reps, nums_count, el)
                    else: 
                        return False
            else:
                i=0
        if not nums_count.keys():
            return True

def removeKeysWithZeroValue(total_reps, nums_count, el):
    nums_count[el] = nums_count[el] - total_reps
    if nums_count[el] == 0:
        nums_count.pop(el)