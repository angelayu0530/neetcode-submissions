class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t) != len(s):
            return False
        s_sorted = defaultdict(int)
        t_sorted = defaultdict(int)
        for i in range(len(s)):
            s_sorted[s[i]] +=1
            t_sorted[t[i]] +=1
        return s_sorted == t_sorted
        