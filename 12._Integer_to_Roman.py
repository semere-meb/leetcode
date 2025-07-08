class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """

        literals = {1000: "M", 500: "D", 100: "C", 50: "L", 10: "X", 5: "V", 1: "I"}
        divisors = list(literals.keys())

        res = ""
        i = 0
        p = 3

        while i <= len(divisors):
            digit = num // divisors[i]

            if digit < 1:
                if divisors[i] in (1000, 100, 10):
                    p -= 1
                i += 1
            elif digit in (4, 9):
                res += literals[divisors[i]] + literals[divisors[i - 1]]
                num -= digit * 10**p
            else:
                res += literals[divisors[i]]
                num -= divisors[i]
        return res


s = Solution()
print(s.intToRoman(3749))
# print(s.intToRoman(58))
# print(s.intToRoman(1994))
