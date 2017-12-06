
carte_suite = [(4, 4),(13, 1),(2, 4),(10, 4),(6, 4),(8, 2),(7, 4)]
c = []

for i in range(len(carte_suite)):
    c.append(carte_suite[i][1])

c.sort()
print(c)
dico = {}

cnt = 0
for j in c :
        dico[j] = dico.get(j,0) + 1 # rempli le dictionnaire 
print(dico)
for m,n in dico.items():
    
    if n >= 5 :
        print ("main suite de couleur")
        

