class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}
        for word in strs:
            sort = sorted(word)
            key = "".join(sort)
            if key not in group:
                group[key] = []
            group[key].append(word)
        return list(group.values())
