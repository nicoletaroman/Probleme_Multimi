A={1,2,3,4}
import itertools
for i in range(0,len(A)):
    B=itertools.combinations(A,i+1)
    M=itertools.combinations(A,i)
    J=itertools.combinations(A,2)
    W=itertools.combinations(A,1)
    C=set(B)
    F=set(M)
    L=set(J)
    H=set(W)
 
print("submultimile sunt=",C,F,L,H)