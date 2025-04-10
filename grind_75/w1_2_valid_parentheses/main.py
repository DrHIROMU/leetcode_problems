class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s: 
            top_p = '' if not stack else stack[len(stack)-1]
            match c:
                case ")":
                    if top_p != '(':
                        return False  
                    stack.pop()                  
                case "]":
                    if top_p != '[':
                        return False
                    stack.pop()
                case "}":
                    if top_p != '{':
                        return False
                    stack.pop()
                case _:
                    stack.append(c)            
        return not stack

def main():
    s = Solution()
    print(s.isValid("(({}[])){}"))

if __name__ == '__main__':
    main()