class MinStack:

    def __init__(self):
        self.st = []
        self.min_stack = [float('inf')]

        

    def push(self, val: int) -> None:
        self.st.append(val)
        m = min(val,self.min_stack[-1])
        self.min_stack.append(m)
        

    def pop(self) -> None:
        self.min_stack.pop()
        return(self.st.pop())
        

    def top(self) -> int:
        return(self.st[-1])
        

    def getMin(self) -> int:
        print(self.min_stack)
        return(self.min_stack[-1])
        
