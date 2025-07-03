class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows >= len(s):
            return s
        rows = [""] * numRows

        row = 0
        direction = -1

        for i in s:
            rows[row] += i
            if row == numRows - 1 or row == 0:
                direction *= -1
            row += direction

        return "".join(rows)


if __name__ == "__main__":
    print(Solution().convert("paypalishiring", 3))
    print(Solution().convert("paypalishiring", 4))
