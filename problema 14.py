A=set(input('introduceti primul sir de caractere'))
B=set(input('introduceti  al doilea sir de caractere'))
print('x.caractere care se intilnesc cel putin in unul dintre siruri:',A.union(B))
print('y.caractere care apar in ambele siruri:',A.intersection(B))
print('z.caractere care apar in primul si nu apar in sirul al doilea:',A.difference(B))