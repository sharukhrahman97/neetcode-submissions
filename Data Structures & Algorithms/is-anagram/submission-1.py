class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_hashset = {}
        t_hashset = {}
        if len(s)!=len(t):
            return False
        for i in range(len(s)):
            s_hashset[s[i]] = 1 + s_hashset.get(s[i],0)
            t_hashset[t[i]] = 1 + t_hashset.get(t[i],0)
        if s_hashset == t_hashset:
            return True
        return False