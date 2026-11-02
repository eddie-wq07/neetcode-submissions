class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counts = [0, 0, 0] # 0, 1 ,2

        for i in nums:
            counts[i] += 1
        # nums [2, 1, 0, 1]
        # counts = [1, 2, 1]

        i = 0
        for n in range(0, len(counts)): #4
            for j in range(0, counts[n]): #3
                nums[i] = n
                i+=1 
                        


            
