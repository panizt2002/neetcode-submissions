class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for steady in range(len(nums) - 2):

            # Skip duplicate steady values
            if steady > 0 and nums[steady] == nums[steady - 1]:
                continue

            left = steady + 1
            right = len(nums) - 1

            while left < right:
                total = nums[steady] + nums[left] + nums[right]

                if total < 0:
                    left += 1

                elif total > 0:
                    right -= 1

                else:
                    result.append([
                        nums[steady],
                        nums[left],
                        nums[right]
                    ])

                    left += 1
                    right -= 1

                    # Skip duplicate left values
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

        return result