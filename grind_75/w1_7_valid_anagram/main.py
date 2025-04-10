class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        volcabulary_map = {}
        if len(s) != len(t):
            return False

        for c in s:
            volcabulary_count = 1 if volcabulary_map.get(c) is None else volcabulary_map.get(c)+1
            volcabulary_map[c] = volcabulary_count
        for c in t:
            if volcabulary_map.get(c) is None:
                return False
            elif volcabulary_map.get(c) == 0:
                return False
            else:
                volcabulary_map[c] = volcabulary_map[c]-1

        return True

def main():
    s = 'catsddf'
    t = 'cas'
    solution = Solution()
    is_anagram = solution.isAnagram(s, t)
    print(is_anagram)

if __name__ == '__main__':
    main()