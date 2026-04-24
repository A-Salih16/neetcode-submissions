class Solution:
    def countBits(self, n: int) -> List[int]:
        liste=[0]*(n+1)

        for i in range(n+1):
            a=i
            while(a!=0):
                liste[i]+=a%2
                a=a>>1
        return liste
                
        