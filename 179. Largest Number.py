'''
Take this test case [3,30,34,5,9],
Multiplying each of these values by 10 gives this array:
['3333333333', '30303030303030303030', '34343434343434343434', '5555555555', '9999999999']

This strings are compared lexicographically, where the leading char from two strings are compared one at a time. 
We're sorting by descending, so the greater char will win, if they are the same the next one is compared until the tie is broken. 
Therefore '9999999999' is the greatest, and '9' comes first in the output as no char is greater than 9 lexicographically (when only ints are considered), 
then '5555555555', or '5', and then something interesting happens as we have a tie with '34343434343434343434', '30303030303030303030', and '3333333333'. 
The first char of each string is '3', so their next value must be compared. '4' is compared against '0' which is compared against '3'. 
The resulting order is then 34,3,30 as 4>3>0. This leads the final output to be '9534330'. I hope this helps.
'''

class Solution:
    def largestNumber(self, nums: List[int]) -> str:

        nums=sorted(nums,key= lambda i: str(i)*10,reverse=True)

        # Handle the case where the largest number is zero
        if nums[0] == 0:
            return "0"

        return ''.join(map(str,nums))
        
