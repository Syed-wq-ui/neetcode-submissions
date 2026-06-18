class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        max=0
        if len(nums)==1:
            return nums[0]
        for i in range(len(nums)-1):
            count=1
            for j in range(i+1,len(nums)):
                if nums[i]==nums[j]:
                    count+=1
            if max<count:
                max=count
                majority=nums[i]
        return majority              