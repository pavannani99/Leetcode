class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        num = 0
        oper = '+'
        
        s += '+'  # To process the last number
        
        for i in s:
            if i.isdigit():
                num = num * 10 + int(i)  # Build multi-digit numbers
                
            elif i == '(':
                stack.append(oper)
                stack.append('(')
                oper = '+'  # Reset operator inside parentheses
                num = 0
                
            elif i in '+-*/)':
                if oper == '+':
                    stack.append(num)
                elif oper == '-':
                    stack.append(-num)
                elif oper == '*':
                    stack.append(stack.pop() * num)
                elif oper == '/':
                    stack.append(int(stack.pop() / num))  # Truncate towards zero
                
                num = 0  # Reset num
                oper = i  # Update current operator
                
                if i == ')':
                    temp = 0
                    # Evaluate inside the parentheses
                    while stack[-1] != '(':
                        temp += stack.pop()
                    stack.pop()  # Remove '('
                    prev_oper = stack.pop() if stack and stack[-1] in '+-' else '+'
                    
                    if prev_oper == '+':
                        stack.append(temp)
                    else:
                        stack.append(-temp)
                    
        return sum(stack)
