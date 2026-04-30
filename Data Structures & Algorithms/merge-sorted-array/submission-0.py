class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        L = nums1[0:m]
        R = nums2

        i = 0 #Pointer for L
        j = 0 #Pointer for R
        k = 0 #Pointer for num1

        # while both L, R have elements
        while i < len(L) and j < len(R): 
            if L[i] >= R[j]: 
                nums1[k] = R[j]
                j+=1
            else: 
                nums1[k] = L[i]
                i+=1
            k+=1
        
        # Now, no more elements in 1 of the arrays 

        while i < len(L): 
            nums1[k] = L[i]
            i+=1
            k+=1

        while j < len(R):
            nums1[k] = R[j]
            j+=1
            k+=1
         
        return nums1



        

