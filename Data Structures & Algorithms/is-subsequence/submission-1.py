class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s1=0
        tr=False
        if len(s)<1:
            return True


        for i in range(len(t)):
            
            if t[i]==s[s1]:
                s1+=1
            if s1==len(s):
                return True
            


        return tr

        