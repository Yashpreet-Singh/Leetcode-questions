
#two pointer approach

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        merged=[]
        i=0
        j=0

        if len(nums1)==0:
            merged=nums2
        elif len(nums2)==0:
            merged=nums1
       
        while i!=len(nums1) and j!=len(nums2):
          
            if nums1[i]<nums2[j]:
                merged.append(nums1[i])
                i+=1
            else:
                merged.append(nums2[j])
                j+=1
        
            
        if i==len(nums1) and len(nums1)!=0:
            merged.extend(nums2[j:])
        elif j==len(nums2) and len(nums2)!=0:
            merged.extend(nums1[i:])
        
       

        if len(merged)%2==0:
           
            return (merged[(len(merged)-1)//2] + merged[1+(len(merged)-1)//2] )/2
        else:
        
            return merged[(len(merged)-1)//2]

  --------------------------------------------------------------------------------------------------------
#binary search



