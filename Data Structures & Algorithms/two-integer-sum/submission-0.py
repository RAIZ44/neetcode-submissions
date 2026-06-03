class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            seen[nums[i]] = i
        
        for i in range(len(nums)):
            remaining = target - nums[i]
            if remaining in seen and seen[remaining] != i:
                return [i,seen[remaining]]
        return []