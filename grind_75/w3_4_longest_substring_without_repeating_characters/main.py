# Sliding window + HashSet
# 使用left, right指標與set
# 每輪right+1, 當substring沒有重複max(longest_len, right-left+1)
# 當發現重複字元, left持續+1, 直到找到當下right指到的字元, 過程中持續從set中丟出字元

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:   
        if len(s)==0: return 0
        if len(s)==1: return 1

        char_set = set()
        char_set.add(s[0])
        longest_len = 1
        left, right = 0, 1
                
        while right < len(s):
            c = s[right]
            if c not in char_set:
                longest_len = max(longest_len, right-left+1)                
            else:
                while True:
                    left_c = s[left]
                    char_set.remove(left_c)
                    left+=1
                    if left_c == c:   
                        break
            
            char_set.add(c)        
            right+=1

        return longest_len    

def main():
    s = "dvdf"
    solution = Solution()
    result = solution.lengthOfLongestSubstring(s)
    print(result)

if __name__ == '__main__':
    main()