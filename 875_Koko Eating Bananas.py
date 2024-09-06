# Important:  https://leetcode.com/problems/koko-eating-bananas/solutions/769702/python-clear-explanation-powerful-ultimate-binary-search-template-solved-many-problems
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        piles.sort()
        minimum=1 #piles.index(min(piles))
        maximum=piles[len(piles)-1] #piles.index(max(piles))


        while minimum < maximum :
            k= minimum + (maximum-minimum)//2
        
            if sum([ceil(i/k) for i in piles])<=h:
                #works 
                maximum=k #we found our first value now find minimum
            else:
                minimum= k+1
            
                
        return minimum


