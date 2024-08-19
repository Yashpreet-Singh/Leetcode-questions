class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        l=0
        r=len(nums)-1

        while l<=r:
            m= l+(r-l)//2

            if nums[m] ==target:
                return m
            elif target < nums[m]:
                r = m-1    #at last if a number isnt a match, and the target is less mid, we change r to prevois index and l==m remains 
            elif target > nums[m]:
                l=m+1     #at last if a number isnt a match, and the target is greater mid, we change l to next index and r==m remains 

        #return l
        #OR
        if target < nums[m] and l==m==0:
            return m
        elif target > nums[m]:
            return l
        else:
            return r+1
            
        
