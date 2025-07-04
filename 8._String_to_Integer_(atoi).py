class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """

        int_max = 2**31 - 1
        int_min = -(2**31)

        s = s.lstrip()
        length = len(s)
        i = 0
        if i < length and s[i] in ("-", "+"):
            i = 1
        j = i

        while j < length:
            if not s[j].isdigit():
                break
            j += 1

        if j - i > 0:
            res = int(s[:j])
            if res < int_min:
                return int_min
            elif res > int_max:
                return int_max
            return res
        else:
            return 0


s = Solution()

print(s.myAtoi("42"))
print(s.myAtoi(" -042"))
print(s.myAtoi("1337c0d3"))
print(s.myAtoi("0-1"))
print(s.myAtoi("words and 987"))
print(s.myAtoi(str(2**31 + 4)))
