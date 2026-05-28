class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Use bucket sort
        # categorize elements based on their freq
        # then start looping from the highest index, adding elems in
        # index bucket to an array until the array length is k
        # return arr

        res = []
        len_nums = len(nums)

        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        buckets = [[] for _ in range(len_nums + 1)]
        for num, count in freq.items():
            buckets[count].append(num)

        for f in range(len(buckets) - 1, 0, -1):
            for num in buckets[f]:
                res.append(num)
                if len(res) == k:
                    return res

        