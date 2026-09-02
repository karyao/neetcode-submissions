class Solution:
    def isValid(self, s: str) -> bool:
       
        opening_brackets = []
        closing_brackets = [')', ']', '}']
        
        # go through each parenthesis
        for p in s:
            # If closing bracket, pop the opening bracket list and compare.
            if p in closing_brackets:
                if not opening_brackets:
                    return False

                target = opening_brackets.pop()
                # check if p matches the popped target
                if not ((target == '[' and p == ']') or (target == '{' and p == '}') or (target == '(' and p == ')')):
                    return False
            else:
                opening_brackets.append(p)
        
        return not opening_brackets