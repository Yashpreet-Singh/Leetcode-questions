class Solution:
    def largestAltitude(self, gain: List[int]) -> int:

        #altitude array

        n=len(gain)
        prefix=[0]* (n+1)

        for i in range(1,n+1):
            prefix[i] = prefix[i-1] + gain[i-1]

        return max(prefix)
            
        
