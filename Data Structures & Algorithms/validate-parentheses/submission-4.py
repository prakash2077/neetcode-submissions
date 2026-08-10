class Solution:
    def isValid(self, s: str) -> bool:
        mapp = {
            "}" : "{",
            ")" : "(",
            "]" : "["
        }
        stack = []

        for i in s:
            # if this is ending bracket
            if i in mapp:
                if stack and stack[-1] == mapp[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i) 
        
        return False if stack else True