from sys import stdin
from math import log2
from random import randint
import matplotlib.pyplot as plt

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

class RAM:
    def __init__(self, file): self.data = [strToNum(s.strip().split()[1][::-1]) for s in open(file, "r").readlines()]
    def write(self, dir, data): self.data[dir] = data
    def read(self, dir): return self.data[dir]


class Block:
    def __init__(self, tag, data):
        self.v = 1
        self.tag = tag
        self.data = data

class Cache:
    def __init__(self, memo, blockSize):
        self.memo = memo
        self.memoSize = len(memo.data)
        self.size = self.memoSize//4
        self.blocksCnt = self.size//(blockSize*8)
        self.depth = self.blocksCnt//2
        self.indexBitsCnt = int(log2(self.depth))
        self.offsetBitsCnt = int(log2(blockSize))
        self.data = [[None, None] for _ in range(self.depth)]
        self.misses = 0
        self.hits = 0
        self.tagBitsCnt = 0

    def getParameters(self, direction):
        direction = direction[::-1]
        offset = direction[:self.offsetBitsCnt]
        index = direction[self.offsetBitsCnt:self.offsetBitsCnt+self.indexBitsCnt]
        self.tagBitsCnt = len(direction)-(self.offsetBitsCnt+self.indexBitsCnt)
        tag = direction[self.offsetBitsCnt+self.indexBitsCnt:]
        offset, index, tag = offset[::-1], index[::-1], tag[::-1]
        offset, index, tag = strToNum(offset), strToNum(index), strToNum(tag)
        direction = direction[::-1]
        return (tag, index, offset)

    def genDirections(self, direction, offsetBitsCnt):
        direction = direction[::-1]
        direction = direction[offsetBitsCnt:]
        direction = direction[::-1]
        directions = []
        for i in range(2**offsetBitsCnt): directions.append(strToNum(direction+intToBin(i, offsetBitsCnt)))
        return directions

    def read(self, direction):
        tag, index, offset = self.getParameters(direction)
        ans = None

        if self.data[index][0] == None:
            self.misses += 1
            self.data[index][0] = Block(tag, [self.memo.data[dir] for dir in self.genDirections(direction, self.offsetBitsCnt)])
            ans = intToBin(self.data[index][0].data[offset], 8)
        elif self.data[index][0].v == 1 and self.data[index][0].tag == tag:
            self.hits += 1
            ans = intToBin(self.data[index][0].data[offset], 8)
        elif self.data[index][1] == None:
            self.misses += 1
            self.data[index][1] = Block(tag, [self.memo.data[dir] for dir in self.genDirections(direction, self.offsetBitsCnt)])
            ans = intToBin(self.data[index][1].data[offset], 8)
        elif self.data[index][1].v == 1 and self.data[index][1].tag == tag:
            self.hits += 1
            ans = intToBin(self.data[index][1].data[offset], 8)
        else:
            self.misses += 1
            way = randint(0,1)
            self.data[index][way] = Block(tag, [self.memo.data[dir] for dir in self.genDirections(direction, self.offsetBitsCnt)])
            ans = intToBin(self.data[index][way].data[offset], 8)
        return ans

    def write(self, direction, data):
        tag, index, offset = self.getParameters(direction)
        self.memo.data[strToNum(direction)] = data

        if self.data[index][0] == None:
            self.misses += 1
            self.data[index][0] = Block(tag, [self.memo.data[dir] for dir in self.genDirections(direction, self.offsetBitsCnt)])
        elif self.data[index][0].v == 1 and self.data[index][0].tag == tag:
            self.hits += 1
            self.data[index][0] = Block(tag, [self.memo.data[dir] for dir in self.genDirections(direction, self.offsetBitsCnt)])
        elif self.data[index][1] == None:
            self.misses += 1
            self.data[index][1] = Block(tag, [self.memo.data[dir] for dir in self.genDirections(direction, self.offsetBitsCnt)])
        elif self.data[index][1].v == 1 and self.data[index][1].tag == tag:
            self.hits += 1
            self.data[index][1] = Block(tag, [self.memo.data[dir] for dir in self.genDirections(direction, self.offsetBitsCnt)])
        else:
            self.misses += 1
            way = randint(0,1)
            self.data[index][way] = Block(tag, [self.memo.data[dir] for dir in self.genDirections(direction, self.offsetBitsCnt)])

def main():
    ram1, ram2, ram3, ram4 = RAM("ram.txt"), RAM("ram.txt"), RAM("ram.txt"), RAM("ram.txt")
    cache1, cache2, cache3, cache4 = Cache(ram1, 2), Cache(ram2, 10), Cache(ram3, 6), Cache(ram4, 8)

    instructions = [s.strip().split() for s in open("querys.txt", "r").readlines()]

    for instruction in instructions:
        if len(instruction) == 1: cache1.read(instruction[0])
        else: cache1.write(instruction[0], instruction[1])
    for instruction in instructions:
        if len(instruction) == 1: cache2.read(instruction[0])
        else: cache2.write(instruction[0], instruction[1])
    for instruction in instructions:
        if len(instruction) == 1: cache3.read(instruction[0])
        else: cache3.write(instruction[0], instruction[1])
    for instruction in instructions:
        if len(instruction) == 1: cache4.read(instruction[0])
        else: cache4.write(instruction[0], instruction[1])

    f = open("modRam.txt", "w")
    for i in range(len(ram1.data)): f.write(intToBin(i, 16) + " " + str(ram1.data[i]) + "\n")
    f.close()
    f = open("cache.txt", "w")
    for i in range(len(cache1.data)):
        b1, b2 = cache1.data[i][0], cache1.data[i][1]
        f.write(str(b1.v) + " " + intToBin(b1.tag, cache1.tagBitsCnt) + " " + str(b1.data) + " --- " + str(b2.v) + " " + intToBin(b2.tag, cache1.tagBitsCnt) + " " + str(b2.data) + "\n")
    f.close()

    plt.plot([cache4.depth, cache3.depth, cache1.depth], [cache1.misses, cache3.misses, cache4.misses])
    plt.show()





main()
