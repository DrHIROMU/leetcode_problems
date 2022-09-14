# Given a string s containing only three types of characters: '(', ')' and '*', 
# return true if s is valid.

# The following rules define a valid string:
# Any left parenthesis '(' must have a corresponding right parenthesis ')'.
# Any right parenthesis ')' must have a corresponding left parenthesis '('.
# Left parenthesis '(' must go before the corresponding right parenthesis ')'.
# '*' could be treated as a single right parenthesis ')' 
# or a single left parenthesis '(' or an empty string "".
 
# Example 1:
# Input: s = "()"
# Output: true
# Example 2:
# Input: s = "(*)"
# Output: true
# Example 3:
# Input: s = "(*))"
# Output: true
 
# Constraints:
# 1 <= s.length <= 100
# s[i] is '(', ')' or '*'.

class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stringStack = []
        remainLeftCount = 0

        lefCount = 0
        rightCount = 0
        asteriskCount = 0

        for c in s:
            if c == '(':
                lefCount += 1
            if c == '*':
                asteriskCount += 1
            if c == ')':
                rightCount += 1

            if c == "(" or c == "*":
                stringStack.append(c)
            elif c == ")":
                if not stringStack:
                    return False
                else:
                    hasLeft = False
                    for i in range(len(stringStack)-1, -1, -1):
                        if stringStack[i] == "(":
                            del stringStack[i]
                            hasLeft = True
                            break     
                    if not hasLeft:
                        if len(stringStack)>0:
                            stringStack.pop()
                        else:
                            return False                       
        
        print(lefCount, rightCount, asteriskCount)
        print(stringStack)

        for c in stringStack:
            if c == '(':
                remainLeftCount += 1                
            elif c == '*' and remainLeftCount>0:
                remainLeftCount -= 1

        if remainLeftCount > 0:
            return False

        return True


s = "((((()(()()()*()(((((*)()*(**(())))))(())()())(((())())())))))))(((((())*)))()))(()((*()*(*)))(*)()"
solution = Solution()
print(solution.checkValidString(s))