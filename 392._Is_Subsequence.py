class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        index = -1
        for c in s:
            print(f"testing '{c}' - '{t[index+1:]}'")
            if c not in t:
                return False
            t = t[t.index(c)+1:]
        return True
