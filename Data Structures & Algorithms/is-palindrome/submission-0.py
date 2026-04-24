class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean= ''.join(filter(str.isalnum,s)).lower()
        l=0
        r=len(clean)-1
        while r>l:
            if clean[r]!=clean[l]:
                print(clean[r],clean[l])
                return False

            l+=1
            r-=1



        return True
        
        