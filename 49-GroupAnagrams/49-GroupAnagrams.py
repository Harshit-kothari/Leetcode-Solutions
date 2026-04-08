# Last updated: 4/8/2026, 9:14:22 PM
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        group = defaultdict(list)
        for w in strs:
            key = "".join(sorted(w))
            group[key].append(w)

        return list(group.values())
