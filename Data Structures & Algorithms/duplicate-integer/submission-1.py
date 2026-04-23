class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset = set()

        for num in nums:
            if num not in hashset:
                hashset.add(num)
                continue
            return True
        return False