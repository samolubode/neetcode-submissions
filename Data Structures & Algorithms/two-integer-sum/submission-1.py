class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # init empty hashmap
        # loop through array
            # do rem = target - arr[i]
            # if rem in hashmap, return [hashmap[rem], i]
            # else, hashmap[arr[i]] = i
        
        my_dict = {}

        for i in range(len(nums)):
            rem = target - nums[i]

            if rem not in my_dict:
                my_dict[nums[i]] = i
            else:
                return[my_dict[rem], i]
        