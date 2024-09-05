class StockSpanner:

    def __init__(self):
        self.stack=[]
       
        
        
        

    def next(self, price: int) -> int:

        '''
        Rather than recalucating span , we can store span of an element so it next item is less than
        or equal to prevoius element . we can just add the span pf previous element.
        '''
    

        count=1
       

        while self.stack and price >= self.stack[-1][0]:
            count= count + self.stack.pop()[1] # to check all previous position, and store the popped items
            

        # if len(self.res)!=0:
        #     self.stack.extend(self.res) # puting popped item backin stack
        self.stack.append((price,count))
        
        
        

        return count


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
