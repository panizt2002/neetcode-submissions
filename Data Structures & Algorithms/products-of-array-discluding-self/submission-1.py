class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        sum_num = 1

        for i in range(len(nums)):
            res[i] = sum_num
            sum_num *= nums[i]

        sum_num = 1

        for i in range(len(nums)-1, -1, -1):
            res[i] *= sum_num
            sum_num *= nums[i]

        return res

