import math
import numpy as np

class RootishArayStack():
    def __init__(self, N):
        i = len(N)
        self.n = i
        b = self.i2b(i)
        self.array = [[-1]*(j+1) for j in range(b+1)]
        p = 0
        for l,j in enumerate(self.array):
            i -= len(j)
            if i >= 0:
                for k in range(len(j)):
                    self.array[l][k] = N[p]
                    p += 1
            else:
                for k in range(len(j)+i):
                    self.array[l][k] = N[p]
                    p += 1

    def i2b(self,i):
        return math.ceil((-3 + np.sqrt(9+8*i))/2)

    def get(self,i):
        b = self.i2b(i)
        j = i-b*(b+1)/2
        return self.array[b][int(j)]

    def set(self,i,x):
        b = self.i2b(i)
        j = i-b*(b+1)/2
        y = self.get(i)
        self.array[b][int(j)] = x
        return y

    def add(self,i,x):
        r = len(self.array)
        if r*(r+1)/2 < self.n+1:
            self.grow()
        self.n += 1
        for j in range(self.n-1,i,-1):
            self.set(j,self.get(j-1))
        self.set(i,x)

    def grow(self):
        self.array.append([-1]*(len(self.array)+1))

    def remove(self,i):
        x = self.get(i)
        for j in range(i,self.n-1):
            self.set(j,self.get(j+1))
        self.set(self.n-1,-1)
        self.n -= 1
        r = len(self.array)
        if (r-2)*(r-1)/2 >= self.n:
            print('b')
            self.shrink()
        return x

    def shrink(self):
        r = len(self.array)
        while r > 0 and (r-2)*(r-1)/2 >= self.n:
            self.array.pop(r-1)
            r -= 1



