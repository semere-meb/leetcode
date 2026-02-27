class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        sl = list(s)
        l = 0
        r = len(sl) -1
        while l < r:
            while l < r and s[l] not in vowels:
                l += 1
            while r > l and s[r] not in vowels:
                r -= 1
            sl[l] = s[r]
            sl[r] = s[l]
            l += 1
            r -= 1
        return ''.join(sl)
