class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for n in nums: 
            o = target - n
            for i in range(nums.index(n) + 1, len(nums)):
                if nums[i] == o:
                    return [nums.index(n), i]
                    
