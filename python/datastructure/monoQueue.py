from collections import deque
def get_max(nums, k):
    """
    nums: 输入的数组
    k: 窗口大小
    返回每个窗口的最大值
    """
    ans = []
    q = deque()
    for i, x in enumerate(nums):
        while q and nums[q[-1]] <= x:
            q.pop()
        q.append(i)
        if q[0] == i - k:
            q.popleft()
        if i >= k - 1:
            ans.append(nums[q[0]])
    return ans

