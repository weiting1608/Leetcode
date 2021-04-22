# time complexity: O(n)
# space complextiy: O(1)
# only iterate once (no need to check the path from 0 to the starting point)


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        totalCost, currCost = 0, 0
        startPoint = 0

        for i in range(len(gas)):
            diff = gas[i] - cost[i]
            currCost += diff
            totalCost += diff
            if currCost < 0:
                currCost = 0
                startPoint = i + 1

        return startPoint if totalCost >= 0 else -1
