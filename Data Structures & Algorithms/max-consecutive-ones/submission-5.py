class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxCount = 0
        tracker = 0

        for i in nums: 
            if i == 1: 
                tracker += 1
                maxCount = max(maxCount, tracker)
            else: 
                tracker = 0
        
        return maxCount


        

