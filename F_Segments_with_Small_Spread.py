
# n, k = map(int, input().split())
# a = list(map(int, input().split()))

# ans = n
# l =0
# maxi = float("-inf")
# mini= float("inf")
# for r in range(n):
#     maxi = max(a[r], maxi)
#     mini = min(a[r], mini)
#     if max - min <= k:
#         ans += (r-l)
#     else:
#         l+=1
# print(ans)

from collections import deque

def count_good_segments():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    l = 0
    ans = 0
    max_deque = deque()
    min_deque = deque()

    for r in range(n):
        while max_deque and a[max_deque[-1]] <= a[r]:
            max_deque.pop()
        max_deque.append(r)

        while min_deque and a[min_deque[-1]] >= a[r]:
            min_deque.pop()
        min_deque.append(r)

        while a[max_deque[0]] - a[min_deque[0]] > k:
            l += 1
            if max_deque[0] < l:
                max_deque.popleft()
            if min_deque[0] < l:
                min_deque.popleft()

        ans += r - l + 1

    return ans

print(count_good_segments())