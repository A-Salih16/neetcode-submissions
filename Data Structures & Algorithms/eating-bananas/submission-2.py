class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low=1
        high=max(piles)
        ans = high

        def isCorrect(num):
            k=0
            for i in piles:
                if i%num==0:
                    k+=i//num
                else:
                    k+=i//num+1
            if k>h:
                return -1
            elif k<=h:
                return 0

        while low<=high:
            mid = (low + high) // 2
            if isCorrect(mid)  < 0:
                low = mid + 1
            else:
                ans = mid
                high = mid - 1
        return ans
