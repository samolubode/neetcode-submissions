class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # identify the start of a sequence - num where num - 1 is not in array
        #   put all elem in a hashset
        #   check if num - 1 not in hashset, put num in a hashset of []
        # for all num that starts a sequence, append curr + 1 to hashset[num]
        # loop through to find the max length of num arr value in hashset

        num_set = set(nums)
        seq_hash = {}
        mxs = 0

        for num in num_set:
            if (num - 1) not in num_set:
                seq_hash[num] = True

        for num in seq_hash:
            curr = num + 1
            count = 1

            while curr in num_set:
                count += 1
                curr += 1

            mxs = max(mxs, count)

        return mxs



        