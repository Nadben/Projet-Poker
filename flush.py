import time as tm

cartes_joueur = []

cartes_devoile = [(8,3),(9,2),(11,1),(10,3),(12,3),(1,4),(8,2)]

#prend toutes les cartes sur le jeux pour en faire les cartes du joeuur
##for t in range(len(cartes_devoile)):
##    cartes_joueur.append(cartes_devoile[t])
##


#cleverest way to evaluate the players hand at any time !
#cartes full par exemple (3 cartes meme poids + 2 cartes meme poids)

##
##dic={}
##main = []
##resultat=0
##for m,n in cartes_devoile :
##    dic[m] = dic.get(m,0) + 1
##
##
##print(dic)
##for g,h in dic.items():
##    if( h>=3 ):
##        print(h)
##        main.append(h)
##    if( h==2 ):
##        print(h)
##        main.append(h)
##
##print(main)
##if(len(main) >= 2 and 3 in main ):resultat = 1
##
##print(resultat)
##
##



#/suite colorer (plus tough que je ne pensais) mais c<est la derniere a fixer
#append mon jeu de carte joueur avec ddevoile
carte_suite = []
carte_suite_filter = []
carte_couleur = []
dic = {}
resultat,resultatTmp=0,0
i=0
x=0

index = []
tmp=[]


#prefiltrage de mon dictionnaire


for i in range(0,len(cartes_devoile)):
    carte_couleur.append(cartes_devoile[i][1])


vTmp,itera=0,0

for j in carte_couleur :
        dic[j] = dic.get(j,0) + 1 # rempli le dictionnaire
#je regarde si jai au moins 5 cartes de la meme couleur
for f,g in dic.items():
    print(g)
    if( g >= 5):
        vTmp = f
#si jai 5 cartes de la meme couleur je rempli une liste de tuple temporaire avec la valeur vTmp qui correspond a la valeur ou il y a plus de 5 occurences
for i,j in cartes_devoile:
    if(j == vTmp):
        tmp.append((i,j))

print(tmp)
    
for k in range(0,len(cartes_devoile)):
    carte_suite.append(cartes_devoile[k][0])

carte_suite.sort()
#il faut que je filtre les doublons

for l in carte_suite:
    if(l not in carte_suite_filter):
        carte_suite_filter.append(l)

j=1
for i in range(len(carte_suite_filter) - 1) :
    if ( carte_suite_filter[i+1] - carte_suite_filter[i]  != 1 and j<5) :
        j=1
        resultat = 0
    else :
        j+=1

if(j>=5):
    resultatTmp = 1
#si jai une suite
j=0


print(resultatTmp,tmp,carte_suite_filter)
if(resultatTmp):
    for i in carte_suite_filter:
        for k,j in tmp:
            if(k==i):
                itera+=1
    #si jai une couleur
    if(itera >=5):
        resultat=1
print(resultat)

##if(j>=5):
##
##    for k,m in dic.items():
##        if(m>=5):
##            print(k)
##            for y in range(lent(cartes_devoile)
## 
##    for p in carte_suite_filter:
##        for poids,r in cartes_devoile:
##            if(p==poids):
##                couleur.append(r)
##    print(couleur)
##
##    if(x >= 5):
##        resultat = 1
##
##print(resultat)
#for carte_suite_filter


##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
##
###je classe les cartes du jeu
##for m,n in cartes_devoile:
##    dic[m] = dic.get(m,0)+1
##    main.append(m)
##print(main)
##main.sort()
##print(main)
##
##temp=[]
##search = []
##resultat=0
##j=1
##
###recherche de 3 elements du meme poids,insertion de ses elements dans une liste --> main , fin
##print(len(main))
##for i in range(0,len(main)-1):
##    if(main[i] == main[i+1]):  
##        j+=1
##        print(main[i], "==" ,main[i+1],"j = ",j)
##    elif(main[i] != main[i+1]):
##        j=1
##    if(j>=3):resultat = 1
##
##print(resultat)
##
##        
##
##
##print(temp)
##print(search)
##            

#recherche de 2 elements du meme poids,insertion de ses elements dans une liste -->main, fin

#for m,n in dic:
   # if ():
    #    cartes_joueur.append((m,n))
#print(cartes_joueur)



#Brelan full
##
##dic={}
##full = 0
##resultat=0
##for m,n in cartes_joueur :
##    dic[m] = dic.get(m,0) + 1
##print(dic)
##
##for g,h in dic.items():
##
##    if( h>=3 ): full+=1
##    if( h>=2 ): full+=1
##
##if(full==2):resultat = 1
##
##
##print(resultat)
##tm.sleep(2)
###couleur
##
##dic1={}
##
##
##resultat=0
##for m,n in cartes_joueur :
##    dic1[n] = dic1.get(n,0) + 1
##
##for g,h in dic1.items():
##    if(h>=5): resultat = 1
##
##
##print(resultat)
##tm.sleep(2)
##
##
###carre
##dic={}
##carre = 0
##resultat=0
##for m,n in cartes_joueur :
##    dic[m] = dic.get(m,0) + 1
##
##for g,h in dic.items():
##    if( h==4 ): carre+=1
##
##
##if(carre==1):resultat = 1
##
##print(resultat)
##
##tm.sleep(2)
##
###suite coloree (suite avec meme couleur)
##    
##
##
##
###cartes_puiss = []
###pari = 'f'
###l=1
##
###if pari == 'f':
## #   for i in range(len(cartes_devoile)):      
##  #      cartes_puiss.append(cartes_devoile[i][1])
##
##   # print(cartes_puiss)
##    #for j in range(len(cartes_puiss)):
##
##     #   print(cartes_joueur[0][1],'=',cartes_puiss[j])
##        
##      #  if cartes_joueur[0][1] == cartes_puiss[j]:
##       #     l+=1
##        #    print(l)
##        
####        elif cartes_joueur[1][1] == cartes_puiss[j] :
####            l+=1
####            
####    if cartes_joueur[0][1] == cartes_joueur[1][1] :
####        l+=1
####    print(l)
####
####    if l>=5 : print("j'ai une flush")
####
####    else : print("j'n'ai pas de flush")
##            
##    #hello = cartes_puiss.count(cartes_joueur[0][1])
##    #hello2 = cartes_puiss.count(cartes_joueur[1][1])
##   
##    #print(hello,hello2,hello3)
##         
##         
##        
##       
##    #print(i)
##    #if(i >=5 ): print("wassup") 
##
