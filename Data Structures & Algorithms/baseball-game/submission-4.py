class Solution:
    def calPoints(self, ops: List[str]) -> int:
        record = []
        stack = []

        for i in range(len(ops)):
            if ops[i] not in ("+", "C", "D"):
                record.append(int(ops[i]))
                stack.append(int(ops[i]))
            elif ops[i] == "+":
                addition = stack[-1] + stack[-2]
                record.append(addition)
                stack.append(addition)
            elif ops[i] == "C":
                stack.pop()
                record.pop()
            elif ops[i] == "D":
                double = 2 * stack[-1]
                record.append(double)
                stack.append(double)
        
        return sum(record)
