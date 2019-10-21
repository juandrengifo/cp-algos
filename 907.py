from sys import stdin

def possible(target, dist, kTar):
    dist = [0]+dist
    N, k, i, ac, consistent = len(dist), 0, 0, 0, True

    while i < N-1 and consistent:
        if ac + dist[i+1] <= target:
            ac += dist[i+1] ; i +=1
        else:
            k+=1 ; ac = 0
            if k > kTar: consistent = False
    ans = bool()
    if not consistent: ans = False
    else: ans = k<=kTar
    
    return ans


def bisec(nums, k):
    lo, hi = 0, sum(nums)+1
    while lo+1 < hi:
        mid = (lo+hi)//2
        if possible(mid, nums, k): hi = mid
        else: lo = mid
    return hi

def main():
    inp = stdin.readline()
    while inp != "":
        inp = list(map(int, inp.split()))
        N, k = inp
        nums = list()
        for i in range(N+1): nums.append(int(stdin.readline()))

        print(bisec(nums, k))

        inp = stdin.readline()
main()