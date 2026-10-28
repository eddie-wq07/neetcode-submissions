class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxCount = 0
        tracker = 0

        for i in nums: 
            if i == 1: 
                tracker+= 1
            else:   
                maxCount = max(maxCount, tracker)
                tracker = 0

        maxCount = max(maxCount, tracker)

        return maxCount

        