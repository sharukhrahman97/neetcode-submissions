class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_hashset = dict()
        t_hashset = dict()
        if len(s)!= len(t):
            return False
        for i in range(len(s)):
            s_hashset[s[i]]= s_hashset.get(s[i],0)+1
            t_hashset[t[i]]= t_hashset.get(t[i],0)+1
        if t_hashset == s_hashset:
            return True
        else:
            return False