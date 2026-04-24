class Solution:
    def hammingWeight(self, n: int) -> int:
        if(n==0):
            return 0
        i=0
        while(n!=0):
            i+=n%2;
            n=n>>1
        return i
        