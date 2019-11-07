from sys import stdin

class SuffixAutomaton:
	def __init__(self, s):
		self.edges, self.link, self.length, self.last, self.firstpos, self.clones = [dict()], [-1], [0], 0, [], []
		for i in range(len(s)):
			self.edges.append(dict())
			self.length.append(i+1)
			self.link.append(0)
			r, p = len(self.edges)-1, self.last
			self.clones.append((-1, r))
			while p >= 0 and s[i] not in self.edges[p]:
				self.edges[p][s[i]] = r
				p = self.link[p]
			if p != -1:

				q = self.edges[p][s[i]]
				if self.length[p] + 1 == self.length[q]: self.link[r] = q
				else:
					self.edges.append(self.edges[q].copy())
					self.length.append(self.length[p]+1)
					self.link.append(self.link[q])
					qq = len(self.edges)-1
					self.link[q] = qq
					self.link[r] = qq
					self.clones.append((qq, q))

					while p >= 0 and self.edges[p][s[i]] == q:
						self.edges[p][s[i]] = qq
						p = self.link[p]


			self.last = r

ans, cnt = tuple(), 0

def dfs(G, visited, u, vows, cons):
	global ans, cnt
	visited[u] = True
	if vows+cons > sum(ans) and vows <= (cons*2): ans, cnt = (vows, cons), 1
	elif vows+cons == sum(ans) and vows <= (cons*2): cnt += 1; 
	for c in G[u]:
		v = G[u][c]
		if c == "a" or c == "e" or c == "i" or c == "o" or c == "u" or c == "A" or c == "E" or c == "I" or c == "O" or c == "U":
			dfs(G, visited, v, vows+1, cons)
		else:
			dfs(G, visited, v, vows, cons+1)

def solve(sa):
	global ans, cnt
	G, visited, ans = sa.edges, [False for _ in range(len(sa.edges))], (0,0)
	dfs(G, visited, 0, 0, 0)
	ans = sum(ans)
	return ans, cnt



def main():
	global ans, cnt
	sa = SuffixAutomaton(stdin.readline().strip())
	ans, cnt = solve(sa)
	if ans != 0: print(ans, cnt)
	else: print("No solution")

main()