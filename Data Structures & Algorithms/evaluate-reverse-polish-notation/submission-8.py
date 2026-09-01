import operator
import math
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        if len(tokens) == 1:
            return int(tokens[0])
        
        for token in tokens:
            match token:
                case "+":
                    second = stack.pop()
                    first = stack.pop()
                    stack.append(int(first) + int(second))
                case "-":
                    second = stack.pop()
                    first = stack.pop()
                    stack.append(int(first) - int(second))
                case "*":
                    second = stack.pop()
                    first = stack.pop()
                    stack.append(int(first) * int(second))
                case "/":
                    second = stack.pop()
                    first = stack.pop()
                    stack.append(math.trunc(int(first) / int(second)))
                case _:
                    stack.append(token)
                    
        return stack[-1]
        

            
