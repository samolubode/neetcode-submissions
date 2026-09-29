class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

       

        # [5, 1, 3, 4]


        times_to_rotate = k % len(nums)

        for i in range(times_to_rotate):
            prev = -1
            curr_index = 0
            next_val = nums[prev]
            for i in range(len(nums)):
                curr = prev + 1 #0 1
                curr_val = nums[curr] #5 1

                nums[curr] = next_val #[4, 1, 3, 4 ] [4, 5, 3, 4 ] 

                next_val = curr_val #5 1
                prev = curr #0
