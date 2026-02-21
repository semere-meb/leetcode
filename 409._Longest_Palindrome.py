class Solution:
    def longestPalindrome(self, s: str) -> int:
        sum = 0
        rem = 0
        for key in set(s):
            sum += s.count(key)//2
            if s.count(key) % 2 == 1:
                rem = 1
        return 2 * sum + rem
