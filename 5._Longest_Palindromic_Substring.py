class Solution(object):
    # def _is_palindrome(self, sub):
    #     start = 0
    #     end = len(sub) - 1
    #     while start < end:
    #         if sub[start] != sub[end]:
    #             return False
    #         start += 1
    #         end -= 1
    #     return True
    #
    # def longestPalindrome(self, s):
    #     """
    #     :type s: str
    #     :rtype: str
    #     """
    #
    #     longest = ""
    #     length = len(s)
    #     if length == 0:
    #         return longest
    #
    #     for start in range(length):
    #         ends = []
    #         for _ in range(s.count(s[start], start)):
    #             if len(ends) == 0:
    #                 ends.append(s.rfind(s[start], start))
    #             else:
    #                 ends.append(s.rfind(s[start], start, ends[-1]))
    #
    #         for end in ends:
    #             if self._is_palindrome(s[start : end + 1]):
    #                 longest = (
    #                     s[start : end + 1]
    #                     if end - start + 1 > len(longest)
    #                     else longest
    #                 )
    #     return longest

    def longestPalindrome(self, s):
        length = len(s)
        if length <= 1:
            return s
        start = 0
        end = 0

        def expand(left, right):
            while left >= 0 and right < length and s[left] == s[right]:
                left -= 1
                right += 1
            return left + 1, right - 1

        for i in range(length):
            l1, r1 = expand(i, i)
            l2, r2 = expand(i, i + 1)

            if r1 - l1 > end - start:
                start, end = l1, r1
            if r2 - l2 > end - start:
                start, end = l2, r2

        return s[start : end + 1]


if __name__ == "__main__":
    print(Solution().longestPalindrome("babadd"))
    print(Solution().longestPalindrome("cbbdg"))
    print(Solution().longestPalindrome("a"))
    print(Solution().longestPalindrome("acg"))
