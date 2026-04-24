class Solution:
    memo={}
    def climbStairs(self, n: int) -> int:
        
        if n==0 or n==1:
            return 1
        if n in self.memo:
            return self.memo[n]
        else:
            a=self.climbStairs(n-1)+self.climbStairs(n-2)
            self.memo[n]=a
            return a
        