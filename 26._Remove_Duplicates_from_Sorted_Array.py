#! /usr/bin/env python3


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[count-1]:
                nums[count] = nums[i]
                count += 1
        return count


if __name__ == "__main__":
    print(Solution().removeDuplicates([1, 1, 2]))
    print(Solution().removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
