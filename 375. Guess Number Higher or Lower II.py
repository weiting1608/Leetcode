"""
最坏（max)的情况下支付最少(min)的钱
假定选了一个错的数，那么接下来就要从[1,x-1]/[x+1,n]的范围内再找，这两个区间内哪个支付最多选哪个区间；
然后对于再选的这个区间采取相同的策略，所以就需要用到dp不能再用二分法了。
总的损失是f(x) = x + max(helper(l,x-1), helper(x+1,r))
把x从 1~n 遍历一遍，取f(x)最小（这里的意思是假设这个人足够聪明，在给定n的情况下知道先猜几再猜几），递归。
题目只要求返回需要支付的最多值，这里的printPath func是方便看猜的最坏情况的路径的。
"""
class Solution:
    def getMoneyAmount(self, n: int) -> int:
        dp = [[0] * (n+1) for _ in range(n+1)]
        self.helper(dp,1,n)
        self.printPath(dp,1,n)
        return dp[1][n]
        
    def helper(self, dp, l, r):
        if l >= r: return 0
        if dp[l][r]: return dp[l][r]
        dp[l][r] = min(i + max(self.helper(dp,l,i-1), self.helper(dp,i+1,r)) for i in range(l,r+1))
        return dp[l][r]
    
    def printPath(self, dp, l, r):
        if l >= r: return
        for i in range(l, r+1):
            if dp[l][r] == i + max(dp[l][i-1], dp[i+1][r]):
                print(i)
                if dp[l][i-1] > dp[i+1][r]:
                    self.printPath(dp,l,i-1)
                else:
                    self.printPath(dp,i+1,r)
                break
        