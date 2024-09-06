import heapq
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:

        k=3
        for i in range(len(nums)-1):

            heap = [-x for x in nums[i:i+k]]
            heapq.heapify(heap) #gets us the max +ve (smallest -ve) at root
            if -heap[0]== nums[i+1]:
                return i+1 #return index where we find peak
        return 0 # or nums.index(max(nums))

      
        # if nowhere else then our top index should be at 0, as that's the one which isnt checked
        # like [4,0] and given the nums[0] is alwasy greater than out of array element
        '''
        You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always considered 
        to be strictly greater than a neighbor that is outside the array
        '''
