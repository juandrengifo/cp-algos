from sys import stdin
from collections import deque

def main():
    n, k = list(map(int, stdin.readline().strip().split()))
    nums = list(map(int, stdin.readline().strip().split()))
    queue = deque()
    onScreen = set()

    for num in nums:
        if num not in onScreen:
            if len(queue) == k:
                onScreen.remove(queue.popleft())
                queue.append(num)
                onScreen.add(num)
            else: onScreen.add(num); queue.append(num)
    ans = ""
    while len(queue): ans += (str(queue.pop())+" ")
    print(len(ans)//2)
    print(ans[:-1])



main()
