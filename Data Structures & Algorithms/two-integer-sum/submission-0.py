class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashset = dict()

        for i in range(len(nums)):
            bal = target-nums[i]
            if bal in hashset:
                return [hashset[bal],i]
            hashset[nums[i]]=i