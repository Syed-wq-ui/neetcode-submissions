class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        #count=0  -->MY METHOD BRUTE FORCE
        #for i in range(len(nums)):
         #  sum=0
          #  for j in range(i,len(nums)):
           #  sum=sum+nums[j]
            #    if sum==k:
             #       count=count+1
        #return count

        prefix = 0
        count = 0
        mp = {0:1}

        for num in nums:
          prefix += num
          count += mp.get(prefix-k, 0)
          mp[prefix] = mp.get(prefix, 0) + 1

        return count            