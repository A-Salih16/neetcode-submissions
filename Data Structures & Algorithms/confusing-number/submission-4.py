class Solution:
    def confusingNumber(self, n: int) -> bool:
        K=str(n)
        s="0"

        for i in range(len(K)-1,-1,-1):
            if K[i]=="6":
                s+="9"
            elif K[i]=="9":
                s+="6"
            elif K[i] in "23457":
                return False
            else:
                s+=K[i]

        K=int(s)
        return K!=n
        