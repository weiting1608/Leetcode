# Approach 1: naive approach
# Time Complexity: O(N)
# Space Complexity: O(1)
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = []

        for i in range(1, n+1):
            if i % 3 == 0 and i % 5 == 0:
                res.append("FizzBuzz")
            elif i % 3 == 0:
                res.append("Fizz")
            elif i % 5 == 0:
                res.append("Buzz")
            else:
                res.append(str(i))

        return res

# Approach 2: use hashmap to deal with more complicated cases


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = []
        dic = {3: "Fizz", 5: "Buzz"}

        for i in range(1, n+1):
            strPrint = ""
            for key in dic:
                if i % key == 0:
                    strPrint += dic[key]
            if not strPrint:
                res.append(str(i))
            else:
                res.append(strPrint)
        return res
