A=set(input('dati elementele A =').split())
n=True
for i in A:
    if ord(i)<65 or ord(i)>90:
        n=False
if n==True:
    B=set(input('dati elementele B = ').split())
    m=True
    for ele in B:
        if ord(ele)<65 or ord(ele)>90:
            m=False
    if m==True:
        print('intersectia multimilor=',A.intersection(B))
        print('reuniunea multimilor=',A.union(B))
        print('diferenta multimilor A-B=',A.difference(B),'iar intersectia multimilor B-A=',B.difference(A))
    else:
        print('eroare')
else:
    print('eroare')