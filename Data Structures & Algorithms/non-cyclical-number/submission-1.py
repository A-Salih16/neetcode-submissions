class Solution:
    def isHappy(self, n: int) -> bool:

        a=set()
        while(n!=1):
            k=str(n)
            z=0
            for i in range (len(k)):
                z+=int(k[i])**2;
            if z in a:
                return False
            a.add(z);
            n=z
                    
        return True;

        