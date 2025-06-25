class Solution(object):
    # def lengthOfLongestSubstring(self, s):
    #     """
    #     :type s: str
    #     :rtype: int
    #     """
    #     length = len(s)
    #     size = length
    #
    #     while size > 0:
    #         left = 0
    #         right = size
    #         while right <= length:
    #             if len(s[left:right]) != len(set(s[left:right])):
    #                 left += 1
    #                 right += 1
    #             else:
    #                 return size
    #         size -= 1
    #     return size

    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_set = set()
        left = 0
        max_len = 0

        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            char_set.add(s[right])
            max_len = max(max_len, right - left + 1)

        return max_len
