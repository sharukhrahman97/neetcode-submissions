class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashset = {}

        for i,num in enumerate(nums):
            k=target-num
            if k in hashset:
                return [hashset[k],i]
            else:
                hashset[num] = i
        return []