class Solution:
    def isValid(self, s: str) -> bool:
        a=[]


        for i in s:
            if i=="(" or i=="[" or i=="{":
                a.append(i)
            elif len(a)!=0:
                if i==")":
                    if a[-1]=="(":
                        a.pop()
                    else:
                        break
                if i=="}":
                    if a[-1]=="{":
                        a.pop()
                    else:
                        break
                if i=="]":
                    if a[-1]=="[":
                        a.pop()
                    else:
                        break
            else:
                return False
                    






        if len(a)!=0:
            return False
        return True


        