class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Pay attention that there is no need for using "for"
        i = 0
        j = len(numbers) - 1
        while i < j:
            if numbers[i] + numbers[j] > target:
                j -= 1
            elif numbers[i] + numbers[j] < target:
                i += 1
            elif i != j:
                return [i+1, j+1]