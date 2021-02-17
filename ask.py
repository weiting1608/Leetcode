
class Solution():
    def findpair(self, arr1, arr2, target):

        res = []
        close = float('inf')
        for i in range(len(arr1)):
            for j in range(len(arr2)):
                dif = abs(target - arr1[i] - arr2[j])
                if dif < close:
                    close = dif
                    sum = arr1[i] + arr2[j]
                    res.append([i, j, sum])
                if dif == close:
                    close = dif
                    sum = arr1[i] + arr2[j]
                    res.append([i, j, sum])

        print(res)


sol = Solution()
arr1 = [-1,3,8,2,9,5]
arr2 = [4,1,2,10,5,20]
target = 24
sol.findpair(arr1, arr2, target)

