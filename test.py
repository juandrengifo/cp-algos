import random

def strToNum(binary):
    ans = 0; binary = binary[::-1]
    for i in range(len(binary)): ans += ((2**i)*int(binary[i]))
    return ans
def intToBin(x, bitsCnt):
    ans = ''
    while x!=0:
        ans+= str(x%2)
        x = x//2
    while len(ans) < bitsCnt: ans += str(0)
    ans = ans[::-1]
    return ans
"""
for i in range(2**8):
    print(intToBin(i, 8), intToBin(random.randint(0,200), 8))
"""

for i in range(300):
    print(intToBin(random.randint(0,2**8), 8))


for i in range(100): print(intToBin(i, 8) + " " + intToBin(random.randint(0,255), 8))
