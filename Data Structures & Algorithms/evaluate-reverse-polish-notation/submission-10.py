class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        if len(tokens) == 1:
            return int(tokens[0])

            
        for token in tokens:
            if token in "+-*/":
                b = stack.pop()
                a = stack.pop()
                
                match token:
                    case "+":
                        stack.append(a+b)
                    case "-":
                        stack.append(a-b)
                    case "*":
                        stack.append(a*b)
                    case "/":
                        stack.append(int(a/b)) # turn into int again because we ant to truncate the zeroes
            else:
                stack.append(int(token))
        
        return stack.pop()
            