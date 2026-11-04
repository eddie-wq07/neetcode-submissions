class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxSoFar = currentMax =  0

        for n in nums: 
            if n == 1: 
                currentMax += 1
            else: 
                maxSoFar = max(currentMax, maxSoFar)
                currentMax = 0
        
        return max(currentMax, maxSoFar)

                
            