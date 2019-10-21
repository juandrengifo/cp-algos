from sys import stdin
import sys
sys.setrecursionlimit(100000000)

def floydwarshall(graph):
    N = len(graph)

    #initialization
    dp = [[10000000 if i != j else 0 for j in range(N)] for i in range(N)]
    for u in range(len(graph)):
        for v, w in graph[u]: dp[u][v] = w; dp[v][u] = w
    #fat-man
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if dp[i][k] + dp[k][j] < dp[i][j]:
                    dp[i][j] = dp[i][k] + dp[k][j]
    return dp


def main():
    cases = int(stdin.readline())
    stdin.readline()
    for case in range(cases):
        N, M = list(map(int, stdin.readline().split()))
        N += 1
        graph = [[] for _ in range(N)]
        for edge in range(M):
            u, v, w = list(map(float, stdin.readline().split()))
            u = int(u); v = int(v)
            graph[u].append((v,w));graph[v].append((u,w))
        
        destCnt  = int(stdin.readline())
        dests, saved = [0], 0
        for d in range(destCnt):
            dest, save = list(map(float, stdin.readline().split()))
            dest = int(dest)
            saved += save; dests.append(dest)
        print(dests, saved)


main()