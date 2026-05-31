class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        result = []

        for r in range(len(nums)):
            # Remove indexes outside the window
            while q and q[0] <= r - k:
                q.popleft()

            # Remove smaller values from the back
            # They can never be maximum while nums[r] is in the window
            while q and nums[q[-1]] < nums[r]:
                q.pop()

            q.append(r)

            # First valid window ends at r = k - 1
            if r >= k - 1:
                result.append(nums[q[0]])

        return result