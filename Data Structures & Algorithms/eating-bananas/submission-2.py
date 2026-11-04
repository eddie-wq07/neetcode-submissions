class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        L, R = 1, max(piles)
        result = R

        while L <= R: 
            M = (L + R) // 2
            
            hours = 0 # resetting hours = 0

            for p in piles: # compute hours for this value M.
                hours += math.ceil(p / M)
            
            if hours <= h: 
                result = min(result, M)
                R = M - 1
            else: 
                L = M + 1
        
        return result


