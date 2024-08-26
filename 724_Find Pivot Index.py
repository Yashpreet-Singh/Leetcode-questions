class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        n=len(nums)
        prefix=[0]*n
        postfix=[0]*n

        for i in range(1,n):
            prefix[i] = prefix[i-1]+nums[i-1]

       

        for j in range(n-2,-1,-1):
            postfix[j]= postfix[j+1]+nums[j+1]


        for ind,tup in enumerate(zip(prefix,postfix)):
          
            if tup[0]==tup[1]:
                return ind
        else:
            return -1
    
       
    
        
        
