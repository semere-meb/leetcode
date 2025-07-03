class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = -1 if x < 0 else 1
        x = abs(x)

        int_max = 2**31 - 1

        rev = str(x)[::-1]

        x_int = 0

        for i in rev:
            if x_int > int_max / 10:
                return 0
            x_int *= 10
            if sign == 1 and x_int > int_max - int(i):
                return 0
            elif sign == -1 and x_int > int_max - int(i) + 1:
                return 0
            x_int += int(i)

        return sign * x_int
