class Solution:
    def isValid(self, s: str) -> bool:

        # for every open paraenthese there should be a closing one 
        # one theres an open, put the closing one into a stack, 
        # the next of the string, check if its equal to the top of stack, 
        # if it is remove (pop) it and if not then move on to the next of
        # the string, and then add its opposite to the stack

        pairs = {
            '(' : ')', 
            '{' : '}',
            '[' : ']'
        }

        stack = [] 

        for c in s: 
            if c in pairs: 
                stack.append(pairs[c])
            else: 
                if not stack or stack[-1] != c: 
                    return False 
                stack.pop()

        return not stack 
        
        

        