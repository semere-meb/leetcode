class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        for c in s:
            if c not in t:
                return False
            t = t[t.index(c)+1:]
        return True
