from bisect import bisect_left
def discretisize(arr):
    """
    离散化
    """
    a = sorted(set(arr))
    return [bisect_left(a, x) for x in arr] # 从 0 开始

a = [1, 2, 2, 231, 124125, 21314]
print(discretisize(a))