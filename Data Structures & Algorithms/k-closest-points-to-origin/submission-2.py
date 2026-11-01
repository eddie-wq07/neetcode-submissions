class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Assume e and s are given. 

        def dist(p): 
            return p[0] ** 2 + p[1] ** 2

        def quickSelect(s, e):
            pivot = dist(points[e])
            left = s
        
            for i in range (s, e):
                if dist(points[i]) < pivot: 
                    points[i], points[left] = points[left], points[i]
                    left+=1
            
            points[left], points[e] = points[e], points[left]

            if left == k - 1: 
                return
            elif left < k - 1: 
                quickSelect(left + 1, e)
            else: 
                quickSelect(s, left - 1)
        
        quickSelect(0, len(points) - 1)

        return points[0:k]

            





        


        


        