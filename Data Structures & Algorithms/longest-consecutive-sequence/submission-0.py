class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
      #brute
      n=len(nums)
      max_count=0
      for i in range(0,n):
        num=nums[i]
        count=1
        while num + 1 in nums:
            count=count+1
            num=num+1
        if max_count<count:
            max_count=count
      return max_count                