from functools import reduce


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        res = [reduce(lambda a, b: a if a == b else None, item) for item in zip(*strs)]
        last = res.index(None) if None in res else len(res)

        return "".join(res[:last])
