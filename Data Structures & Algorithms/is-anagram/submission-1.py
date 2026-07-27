class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        seen = list()
        for sa in s:
            seen.append(sa)
        for ta in t:
            if ta in seen:
                seen.remove(ta)
        if seen == list():
            return True
        else:
            return False
