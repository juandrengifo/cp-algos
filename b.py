from sys import stdin

def countDays(nums, f, to, memo, solved):
    if f != to and not solved[f]:
        solved[f] = True
        memo[f] += countDays(nums, nums[f], to, memo, solved)
    return memo[f]

def main():
    querys = int(stdin.readline())
    for query in range(querys):
        n = int(stdin.readline())
        nums = list(map(int, stdin.readline().strip().split()))
        for i in range(n): nums[i] -= 1
        memo, solved = [1 for _ in range(n)], [False for _ in range(n)]
        ans = [countDays(nums, nums[x], x, memo, solved) for x in range(n)]
        print(*ans)

main()
