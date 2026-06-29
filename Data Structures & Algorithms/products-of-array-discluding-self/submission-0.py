class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product=[]
        for i in range(len(nums)):
            j=0
            prod=1
            for j in range(len(nums)):
                if(i!=j):
                    prod=prod*nums[j]
            product.append(prod)   
        return product                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              