class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:


        stones = [-s for s in stones]
        heapq.heapify(stones)
        while(len(stones)>1):
            a=heapq.heappop(stones)
            b=heapq.heappop(stones)
            heapq.heappush(stones,-abs(a-b))
            if(len(stones)==1 ):
                break
        return -1*stones[0]
      
        