#2. towers of hanoi

moves=[]
A,B,C = 'A','B','C'
def towers(orig, dest, aux, n):
    if n==1:
        moves.append((orig,dest))
    else:
        towers(orig, aux, dest, n-1)
        towers(orig, dest, aux, 1)
        towers(aux, dest, orig, n-1)

towers(A,B,C,2)
print(moves)