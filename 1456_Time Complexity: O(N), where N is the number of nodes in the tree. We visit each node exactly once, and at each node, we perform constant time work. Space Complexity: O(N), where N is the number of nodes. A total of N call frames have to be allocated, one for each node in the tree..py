#question: https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/description/?envType=study-plan-v2&envId=leetcode-75
#fixed length - sliding window , as k is given
class Solution:
    def maxVowels(self, s: str, k: int) -> int:

        state=0
        start=0
        max_length=0

        for end in range(len(s)):
            if s[end] in 'aeiou': #adding an element
                state+=1
                
            if end - start + 1 == k:
               
                max_length=max(max_length,state)
                if s[start] in 'aeiou':
                    state-=1  #check if removed is vowel
                start+=1
            
        return max_length 





        
