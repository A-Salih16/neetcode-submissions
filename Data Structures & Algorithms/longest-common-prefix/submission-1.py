class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        a=strs[0]
        c=0
        k=""
        if len(strs)==1:
            return strs[0]
        for i in range(len(a)):
            z=a[i]


            for j in range (1,len(strs)):
                if i>len(strs[j])-1:
                    c=1
                    break
                if strs[j][i]!=z:
                    return k
                if strs[j][i]==z and j==len(strs)-1:
                    k+=z

            if c==1:
                break
        return k
                 






        