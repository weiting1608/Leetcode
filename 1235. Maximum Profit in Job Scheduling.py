class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        """
        classical dp problem
        initialize an array to store the max profit until ith item was selected, maxProfit.
        For every ith item, traverse backwards, if the endTime is smaller than the startTime of the ith item,
        meaning that the benefit of ith item can be added on maxProfit[j] to achieve a larger profit.
        lots of dp problem needs to think from the last elements
        """

        # need to sort the item according to the endTime, as the reference to traverse j.
        seq = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])
        maxProfit = [0 for _ in range(len(seq))]

        for i in range(len(seq)):
            startTime, endTime, profit = seq[i]
            # profit without selecting ith item
            prevProfitN = maxProfit[i-1] if i > 0 else 0
            prevProfitY = profit  # initialize the profit with selecting ith item
            for j in range(i-1, -1, -1):  # traverse
                # if jth item's endTime is <= startTime of ith item, meaning both can be selected
                if seq[j][1] <= startTime:
                    prevProfitY += maxProfit[j]
                    break  # since the seq is ordered by endTime, break is necessary

            # choose from whether select ith item or not
            maxProfit[i] = max(prevProfitN, prevProfitY)

        return maxProfit[-1]
