
carte_suite = [1,2,3,4,5]
carte_suite.sort()
for i in range(len(carte_suite) -1) :   
    if ( carte_suite[i+1] - carte_suite[i]  != 1) : resultat = 0
    else : resultat = 1
print(resultat)
