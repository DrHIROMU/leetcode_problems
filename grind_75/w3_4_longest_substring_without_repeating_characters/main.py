class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_len = 0
        char_set = set()
        
        for i in range(len(s)):
            c = s[i]
            if c not in char_set:
                char_set.add(c)
            else:
                if len(char_set) > longest_len:
                    longest_len = len(char_set)                
                char_set.clear()
                char_set.add(c)

        if len(char_set) > longest_len:
            longest_len = len(char_set)  
        return longest_len    

def main():
    s = "dvdf"
    solution = Solution()
    result = solution.lengthOfLongestSubstring(s)
    print(result)

if __name__ == '__main__':
    main()