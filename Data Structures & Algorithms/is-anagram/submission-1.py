class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hash_s = {}
        hash_t = {}

        for n in s:
            hash_s[n] = hash_s.get(n, 0) + 1

        for m in t:
            hash_t[m] = hash_t.get(m, 0) + 1

        if hash_s == hash_t:
            return True
        else:
            return False