def get_left(nums):
    """
    nums: 输入的数组
    返回每个数左边第一个严格大于它的数的下标
    0 表示不存在
    """
    n = len(nums) - 1
    stack = []
    left = [0] * (n + 1)
    for i in range(1, n + 1):
        while stack and nums[stack[-1]] <= nums[i]:
            stack.pop()
        if stack:
            left[i] = stack[-1]
        stack.append(i)
    return left

def get_right(nums):
    """
    nums: 输入的数组
    返回每个数右边第一个严格大于它的数的下标
    0 表示不存在
    """
    n = len(nums) - 1
    stack = []
    right = [0] * (n + 1)
    for i in range(n, 0, -1):
        while stack and nums[stack[-1]] <= nums[i]:
            stack.pop()
        if stack:
            right[i] = stack[-1]
        stack.append(i)
    return right

# luogu 5788 【模板】单调栈
if __name__ == "__main__":
    n = int(input())
    nums = [0] + list(map(int, input().split()))
    right = get_right(nums)
    print(*right[1:])
