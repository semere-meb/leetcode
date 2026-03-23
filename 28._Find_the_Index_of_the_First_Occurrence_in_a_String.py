# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/submissions/1957189064/


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle in haystack:
            return haystack.index(needle)
        return -1
