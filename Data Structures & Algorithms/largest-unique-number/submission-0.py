class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        nums.sort()
        max=-1
        lol=set()
        for i in range(len(nums)-1,0,-1):
            if nums[i]>max:
                if nums[i]==nums[i-1]:
                    lol.add(nums[i])
            if nums[i] not in lol and nums[i]>max:
                max=nums[i]
        if nums[0] not in lol and nums[0]>max :
            max=nums[0]
        return max



             
            
        