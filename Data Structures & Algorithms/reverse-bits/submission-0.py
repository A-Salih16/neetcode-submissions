class Solution:
    def reverseBits(self, n: int) -> int:
        k=0
        i=31
        while(n!=0):
            if(n%2==1):
                k+=2**i


            n=n>>1
            i-=1

        return k
        