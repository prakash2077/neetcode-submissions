class Solution:
    def findMin(self, nums: List[int]) -> int:
        min_arr = nums[0]

        l, r = 0, len(nums) - 1
        while(l <= r):
            if (nums[l] <= nums[r]):
                min_arr = min(nums[l], min_arr)
                break
            
            m = (l + r) // 2
            min_arr = min(nums[m], min_arr)
            if nums[l] <= nums[m]:
               l = m + 1
            else:
                r = m - 1
        return min_arr 