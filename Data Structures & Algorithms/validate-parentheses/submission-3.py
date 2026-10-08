class Solution:
    def isValid(self, s: str) -> bool:
        
        stack=[]

        closeToOpen = { "]":"[" , ")":"(" , "}" : "{" }

        for char in s:
            
            # if its closing bracket
            if char in closeToOpen:

                #if stack means (stack not empty) and top of stack = this closing bracket
                if stack and stack[-1]==closeToOpen[char]:
                #  (  ==  ( as closeToOpen[c] is (
                    stack.pop()
                
                else:
                    return False

            
            # if its opening bracket
            else:
                stack.append(char)
            
        

        # if not stack means (stack is empty) so retrun true, else false
        return True if not stack else False


