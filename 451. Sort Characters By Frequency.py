class Solution:
    # time complexity: O(nlogn) or O(n+klogk)
    # space complexity: O(n)
    def frequencySort(self, s: str) -> str:
        freq = {}
        cList = []
        resList = []
        for c in s:
            freq[c] = freq.get(c, 0) + 1

        for key, val in freq.items():
            cList.append((key, val))

        cList.sort(key=lambda x: x[1], reverse=True)

        for x in cList:
            resList.append(x[0] * x[1])
        return "".join(resList)

# Approach 2: bucket sort
# time complexity: O(n)
# space complexity: O(n)


class Solution:
    def frequencySort(self, s: str) -> str:
        if not s:
            return s

        counts = collections.Counter(s)
        max_freq = max(counts.values())

        buckets = [[] for _ in range(max_freq + 1)]
        for c, i in counts.items():
            buckets[i].append(c)

        string_builder = []
        for i in range(len(buckets)-1, 0, -1):
            for c in buckets[i]:
                string_builder.append(c * i)

        return "".join(string_builder)
