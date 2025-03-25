class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = self.remove_non_alphanumeric(s)
        
        #s[::-1]反向逐一取出文字
        return s == s[::-1]
    
    def remove_non_alphanumeric(self, s: str) -> str:
        alphanumeric = ''.join(char.lower() for char in s if char.isalnum())
        return alphanumeric

def main():
    s = Solution()
    is_palindrome = s.isPalindrome("A man, a plan, a casnal: Panama")
    print(is_palindrome)

if __name__ == '__main__':
    main()