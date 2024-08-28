class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:

        points.sort(key=lambda x:x[1])
        count=0
        i=0
        j=1

        while j <= len(points)-1: 
            if points[j][0] > points[i][1]:
                count+=1
                i=j
            else:            
                j+=1
        
        return count+1





        
