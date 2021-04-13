# Sorting according to its start time and check if the end time of the previous
# has overlap with the start time of the next
# similar to LC1235. Maximum profit in job scheduling (sorting according to end time)

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        res = []

        for interval in intervals:
            # compare the interval with the last pair in res currently.
            # if the start time of interval is bigger than end time of last pair,
            # meaning no overlap, just append.
            if not res or res[-1][1] < interval[0]:
                res.append(interval)
            # when there is overlap, just update the end time of the last pair in res
            else:
                res[-1][1] = max(res[-1][1], interval[1])

        return res
