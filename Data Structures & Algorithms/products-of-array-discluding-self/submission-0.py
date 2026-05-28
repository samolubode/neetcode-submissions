class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # we can use prefix and postfix arrays
        # where prefix contains the product of elems upto the curr elem
        # and postfix contains the product of curr elem & elems after 
        # the res will noe be output[i] = nums[i - 1] *  nums[i + 1]
        # This can also be done with just one instead of 2 arrays:
        # first, input the prefix of all elem (multiplication of previous elems(prefix init to 1 from start)),
        # then, starting from the back, multiply elem[i] with postfix (which is also init to 1)

        n = len(nums)
        output = [0] * n
        prefix = postfix = 1

        # loop forward
        # o[i] = prefix
        # prefix *= nums[i]
        i = 0
        while i < n:
            output[i] = prefix
            prefix *= nums[i]
            i += 1

        # loop backward
        # o[i] *= postfix
        # postfix *= nums[i]
        j = n - 1
        while j >= 0:
            output[j] *= postfix
            postfix *= nums[j]
            j -= 1

        return output
        