# dynamic programming -- little special
# specialty: not every day should be purchase the tickets, therefore checking the day is necessary!
# Time complexity: O(N)
# Space complexity: O(N)  N is the number of the last day in days array, less than 365.
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = [float('inf')] * (days[-1]+1)
        dp[0] = 0
        days = set(days)
        du = [1, 7, 30]

        for i in range(1, len(dp)):
            # for day in days set, this day must purchase the ticket.
            if i in days:
                for d, c in zip(du, costs):
                    # different from coin change, in coin change
                    # when i-coin<0, meaning the combination can't make exact the amount.
                    # however, here, if i-d<0, it doesn't matter. it only needs that day to be covered
                    # as for the case when it covers the day before 1st day, it doesn't matter.
                    # important for the case that 7 days tickets is cheaper than the 1 day ticket.
                    dp[i] = min(dp[i], dp[max(i-d, 0)]+c)

            # for day not in days set, no need to buy ticket, just use the value ahead.
            else:
                dp[i] = dp[i-1]

        return dp[-1]
