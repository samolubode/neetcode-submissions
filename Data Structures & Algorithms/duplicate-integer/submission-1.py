class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # create a new set from the list
        new_set = set(nums)

        # check if length of list and set are equal
        if len(new_set) != len(nums):
            return True
        return False
        