class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(remain, stack, start):
            if remain == 0:
                res.append(stack[:])
                return
            elif remain < 0:
                return

            for i in range(start, len(candidates)):
                stack.append(candidates[i])
                # since the elements can be used multiple times, so next start from i again.
                backtrack(remain-candidates[i], stack, i)
                stack.pop()

        backtrack(target, [], 0)
        return res
