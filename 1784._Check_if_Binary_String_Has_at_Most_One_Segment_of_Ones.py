class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        return len([x for x in s.split("0") if x]) == 1


if __name__ == "__main__":
    Solution().checkOnesSegment("1001") #false
    Solution().checkOnesSegment("110")  #true
