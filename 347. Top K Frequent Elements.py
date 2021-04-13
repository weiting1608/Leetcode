class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if not nums or k == 0:
            return None
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        arr = []
        for num, fre in freq.items():
            arr.append((num, fre))

        sortedArr = sorted(arr, key=lambda x: x[1], reverse=True)
        freqK = sortedArr[:k]
        ans = []
        for (key, val) in freqK:
            ans.append(key)

        return ans
