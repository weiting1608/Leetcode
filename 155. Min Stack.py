class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.items = []     

    def push(self, x: int) -> None:
        # for get the minimum in O(1) time, we need to mark down the min up to the value added
        # along with the recently added value. [value, min] like a pair
        if not self.items:
            self.items.append([x, x])
        else:
            cur_min = self.items[-1][1]
            self.items.append([x, min(x, cur_min)])

    def pop(self) -> None:
        try:
            self.items.pop()
        except ValueError:
            print("Oops, no value in the stack!")

    def top(self) -> int:
        return self.items[-1][0]
        
    def getMin(self) -> int:
        return self.items[-1][1]
                


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()