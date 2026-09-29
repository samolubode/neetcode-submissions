class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        times_to_rotate = k % len(nums)

        for i in range(times_to_rotate):
            prev = -1
            curr_index = 0
            next_val = nums[prev]
            for i in range(len(nums)):
                curr = prev + 1 
                curr_val = nums[curr] 

                nums[curr] = next_val 

                next_val = curr_val 
                prev = curr 
