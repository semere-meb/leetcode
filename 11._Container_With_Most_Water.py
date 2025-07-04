class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        max_area = 0
        left = 0
        right = len(height) - 1

        while right > left:
            area = (right - left) * (
                height[left] if height[left] < height[right] else height[right]
            )
            if area > max_area:
                max_area = area

            if height[right] < height[left]:
                right -= 1
            else:
                left += 1

        return max_area


s = Solution()
print(s.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
print(s.maxArea([1, 1]))
