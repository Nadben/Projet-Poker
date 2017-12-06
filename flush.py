import time as tm

cartes_joueur = []

cartes_devoile = [(8,3),(9,3),(6,3),(9,3),(10,4),(10,4),(4,2)]

#prend toutes les cartes sur le jeux pour en faire les cartes du joeuur
##for t in range(len(cartes_devoile)):
##    cartes_joueur.append(cartes_devoile[t])
##


#cleverest way to evaluate the players hand at any time !
#cartes full par exemple (3 cartes meme poids + 2 cartes meme poids)

dic = {}
main =[]

#je classe les cartes du jeu
for m,n in cartes_devoile:
    dic[m] = dic.get(m,0)+1
    main.append(m)
print(main)
main.sort()
print(main)

temp=[]
search = []
resultat=0
j=1

#recherche de 3 elements du meme poids,insertion de ses elements dans une liste --> main , fin
print(len(main))
for i in range(0,len(main)-1):
    if(main[i] == main[i+1]):  
        j+=1
        print(main[i], "==" ,main[i+1],"j = ",j)
    elif(main[i] != main[i+1]):
        j=1
    if(j>=3):resultat = 1

print(resultat)

        


print(temp)
print(search)
            

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
