class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # define the window based on k
        # slide through to the end
        # keep track of the drift
        # condition to update: drift < minDrift

        n = len(arr)
        start, stop = 0, 0

        l, r = 0, 0
        drift = 0

        for i in range(k):
            drift += abs(arr[i] - x)

        r = k
            
        minDrift = drift

        start = l
        stop = l + k

        while r < n:
            drift = drift - abs(arr[l] - x) + abs(arr[l+k] - x)
            l += 1
            r += 1

            if drift < minDrift: 
                minDrift = drift
                start = l
                stop = l + k

        return arr[start:stop]        