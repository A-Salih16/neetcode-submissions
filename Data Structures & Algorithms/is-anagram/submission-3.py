class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a={}
        b={}

        for i in s:
            a[i]=a.get(i,0)+1
        for i in t:
            if i in a:
                a[i]-=1
        for i in t:
            b[i]=b.get(i,0)+1
        for i in s:
            if i in b:
                b[i]-=1
        
        for i  in a.values():
            if i!=0:
                return False
        for i  in b.values():
            if i!=0:
                return False
        
        return True
        