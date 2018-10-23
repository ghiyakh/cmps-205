#6. random walk

import random

#mxn rows by cols
m=5
n=11

grid=[]
for i in range(m):
    #creat list of n 0
    inner=[]
    for j in range(n):
        inner.append(0)
    grid.append(inner)

# print(grid)

#(x,y) center of manhattan
x=n//2
y=m//2

while -1<x<n and -1<y<m :
    grid[y][x] = grid[y][x]+1
    dir=random.randint(0,4)
    if dir==0:
        y=y-1
    elif dir==1:
        y=y+1
    elif dir==2:
        x=x+1
    else:
        x=x-1

for r in grid:
    print(r)