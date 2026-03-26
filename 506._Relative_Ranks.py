from typing import List


class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        rank = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        s = sorted(score, reverse=True)
        for i in range(len(score)):
            idx = s.index(score[i])
            if idx < 3:
                score[i] = rank[idx]
            else:
                score[i] = str(idx + 1)
        return score
