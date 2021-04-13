
class Solution(defaultdict):
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)
        print(ans)
        for s in strs:
            ans[tuple(sorted(s))].append(s)
        return ans.values()
