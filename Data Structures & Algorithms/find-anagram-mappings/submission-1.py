class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        a=0
        log=[]
        visited={}
        for i in range(len(nums1)):
            a=i
            z=nums1[i]
            for j in range(len(nums2)):
                if(nums2[j]==z):
                    a=j
            log.append(a)

        return log
                    