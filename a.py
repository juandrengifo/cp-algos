from sys import stdin

def main():
	n = int(stdin.readline().strip())
	string = list(stdin.readline().strip())
	a, b, i, ans = 0, 0, 0, 0
	for i in range(len(string)):
		if string[i] == "a": a+=1
		else: b+= 1
		if i%2 != 0 and a != b: 
			ans += 1
			if string[i] == "a": string[i] = 'b'
			else: string[i] = 'a'
			a, b = 0, 0
	print(ans)
	for c in string: print(c, end='')
	print("")


main()