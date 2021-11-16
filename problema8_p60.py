A=set(map(int, input('dati elementele A= ').split()))
n=True

for i in A:
    if type(i)!=int:
        n=False
if n==True:
    B=set(map(int, input('dati elementele B =').split()))
    m=True
    for ele in B:
        if type(ele)!=int:
            m=False
    if m==True:
        print('intersectia multimilor=',A.intersection(B))
        print('reuniunea multimilor=',A.union(B))
        print('diferenta multimilor A-B=',A.difference(B),'iar intersectia multimilor B-A=',B.difference(A))
    if m==False:
        print('eroare')
if n==False:
    print('eroare')