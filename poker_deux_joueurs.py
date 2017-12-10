#--------Questions qui viennent au fur et a mesure------#



#-----------------------------liste de shits a faire------------#

##retravailler SC, car mes proba combi ne sont pas les memes bizzarement... (2-3 heures)
##Travailler sur le dialogue (30 minutes)





#-----------librairies-------- #

import random
import time as tm


# ----------- Inputs --------- # 
FICHIER_PROBABILITE = "/pub/data/probabilites.txt" 
MAX_IT = 10**4 
MSG_PIOCHE1 = "Voici vos deux premières cartes: "
MSG_PIOCHE2 = "Voici les trois cartes du flop: "
MSG_PIOCHE3 = "Voici la carte du turn: "
MSG_PIOCHE4 = "Voici la carte de la river: "
MSG_RECAP_CARTES = "Vous avez donc à votre disposition les cartes suivantes:"
MSG_RECAP_CARTES_ORDI = "L'ordinateur a à sa disposition les cartes suivantes:"
MSG_QUESTION_MISE = "Voulez-vous miser quelque chose [O/N]?"
MSG_ERREUR_MISE = "Veuillez répondre par Oui ou par Non:"
MSG_PARI_MISE = "Sur quel résultat voulez-vous miser [p/dp/b/s/c/f/ca/sc] ?"
MSG_MISE_ORDI = "L'ordinateur a misé "
MSG_PARI_ORDI = " sur "
MSG_PARI_RIEN_ORDI = "L'ordinateur n'a rien parié."
MSG_ERREUR_PARI = "Veuillez entrer un résultat valable : p/dp/b/s/c/f/ca/sc ?" 
MSG_RESTE_MISE = "Combien voulez-vous miser?"
MSG_BITCOIN = "Ƀ"
MSG_ERREUR_MONTANT = "Veuillez entrer un montant entier positif inférieur à "
MSG_SOLDE = "Il vous reste "
MSG_SOLDE_ORDI = "L'ordinateur a "
MSG_CONTINUER = "Voulez-vous continuer à jouer [O/N]? "
MSG_FIN_1 = "Merci d'avoir joué. Vous repartez avec "
MSG_FIN_2 = " Ƀ. Bye"
MSG_GAIN_PARI_1 = "Votre pari "
MSG_GAIN_PARI_2 = " vous a rapporté "
MSG_GAIN_PARI_1_ORDI = "Le pari de l'ordinateur "
MSG_GAIN_PARI_2_ORDI = " lui a rapporté "
MSG_FIN_GAGNE = "Vous avez gagné. Bravo!"
MSG_FIN_PERDU = "Vous avez perdu. Dommage!"


#carte_to_string(carte) qui renvoit la chaine de caractères correspondant à carte. Carte est donc un tuple avec comme premier élément
#un nombre entre 1 et 13; comme deuxième élément un nombre de 1 à 4 qui correspondent respectivement à ["♥", "♦", "♣", "♠"]. 
#Par exemple, carte_to_string((5,1)) renvoit la chaine de caractères suivante : 5♥ 

def carte_to_string(carte):
    """Cree la chaine de caracteres correspondant a la carte."""
    symboles = [str(i+1) for i in range(10)] + ["V", "D", "R"]
    couleurs = ["♥", "♦", "♣", "♠"]
    res = symboles[carte[0] - 1] + couleurs[carte[1] - 1]
    return res

def creer_jeu():
    """Cree un jeu de cartes."""
    jeu = []
    for i in range(1,  14):
        for j in range(1, 5):
            jeu.append((i, j))
    return jeu

#le calcul des gains == nouvelle_m * (1/(p(misei)*i))
#dans cette fonction je veux savoir si le joueur a eu un succès ou non
# A chaque mise selon le pari

############################################################################
#                                                                          #
#                       Evaluation des mains                               #
#                                                                          #
############################################################################

def pair(cartes_joueur,cartes_devoile):
    resultat,i = 0,0
    dic={}
    
    for m,n in cartes_devoile:
        dic[m] = dic.get(m,0) + 1
    

    for g,h in dic.items():
        if( h>=2 ):
            i+=1
                
    if(i >= 1):
        resultat = 1

    return resultat

def doublePair(cartes_joueur,cartes_devoile):
    reultat,i = 0,0
    dic={}
    resultat,full = 0,0
    
    for m,n in cartes_devoile:
        dic[m] = dic.get(m,0) + 1


    for g,h in dic.items():
        if( h>=2 ):
            i+=1
                
    if(i >= 2 ):
        resultat = 1

    return resultat

def brelan(cartes_joueur,cartes_devoile):
    resultat,i = 0,1
    dic={}
    main=[]
    #je classe les cartes du jeu
    for m,n in cartes_devoile:
        dic[m] = dic.get(m,0)+1
        main.append(m)
        main.sort()

    for j in range(0, len(main)-1):
        
        if(main[j] == main[j+1]):
            i+=1

        elif(main[j] != main[j+1]):
            i=1
    
        if(i>=3):
            resultat = 1
    
    return resultat

def suite(cartes_joueur,cartes_devoile):
        #append mon jeu de carte joueur avec ddevoile
        carte_suite = []
        carte_suite_filter = []
        resultat,j=0,1
            
        for k in range(0,len(cartes_devoile)):
            carte_suite.append(cartes_devoile[k][0])
        carte_suite.sort()

        #il faut que je filtre les doublons

        for l in carte_suite:
            if(l not in carte_suite_filter):
                carte_suite_filter.append(l)
        
        for i in range(len(carte_suite_filter) - 1) :
            if ( carte_suite_filter[i+1] - carte_suite_filter[i]  != 1 and j<5) :
                j=1
                resultat = 0
            else :
                j+=1
                
        if(j>=5):
  
            resultat = 1

        
        return resultat


def couleur(cartes_joueur,cartes_devoile):
        carte_couleur = []
        dic = {}

        resultat = 0
        
        for i in range(0,len(cartes_devoile)):
            carte_couleur.append(cartes_devoile[i][1])
        
        for j in carte_couleur :
                dic[j] = dic.get(j,0) + 1 # rempli le dictionnaire

        for m,n in dic.items():
            if n >= 5 :
                resultat = 1
        return resultat


def full(cartes_joueur,cartes_devoile):

        dic={}
        main = []
        resultat=0
        for m,n in cartes_devoile :
            dic[m] = dic.get(m,0) + 1
     
        for g,h in dic.items():
            if( h>=3 ): main.append(h)
            if( h==2 ): main.append(h)
 

        if(len(main) >= 2 and 3 in main):resultat = 1

        return resultat


def carre(cartes_joueur,cartes_devoile):
    resultat = 0
    #prend toutes les cartes sur le jeux pour en faire les cartes du joeuur
##    for t in range(len(cartes_devoile)):
##        cartes_joueur.append(cartes_devoile[t])
##
    dic={}
    carre = 0
    resultat=0
    for m,n in cartes_devoile :
        dic[m] = dic.get(m,0) + 1

    for g,h in dic.items():
        if( h>=4 ): carre+=1

    if(carre==1):resultat = 1

    return resultat

def suiteColor(cartes_joueur,cartes_devoile):
    #/suite colorer (plus tough que je ne pensais) mais c<est la derniere a fixer
    #append mon jeu de carte joueur avec ddevoile
    carte_suite = []
    carte_suite_filter = []
    carte_couleur = []
    tmp=[]
    dic = {}
    vTmp,itera=0,0
    resultat,resultatTmp=0,0
    
    #prefiltrage de mon dictionnaire

    for i in range(0,len(cartes_devoile)):
        carte_couleur.append(cartes_devoile[i][1])



    for j in carte_couleur :
            dic[j] = dic.get(j,0) + 1 # rempli le dictionnaire

    for f,g in dic.items():
        if( g >= 5):
            vTmp = f
#boucle for qui me permet de recuperer les cartes avec la meme couleur 
    for i,j in cartes_devoile:
        if(j == vTmp):
            tmp.append((i,j))
#japplique le filtrage de suite
    for k in range(0,len(tmp)):
        carte_suite.append(tmp[k][0])

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
        resultat = 1

    return resultat



def succes(cartes_joueur,cartes_devoile,pari):

    resultat,i=0,0
    if pari == 'p':
        resultat = pair(cartes_joueur,cartes_devoile)
        
    elif pari == 'dp':
        resultat = doublePair(cartes_joueur,cartes_devoile)

    elif pari == 'b':
        resultat = brelan(cartes_joueur,cartes_devoile)
        
    elif pari == 's':
        resultat = suite(cartes_joueur,cartes_devoile)

    elif pari == 'c':
        resultat = couleur(cartes_joueur,cartes_devoile)
                            
    #le full (brelan + paire)
    elif pari == 'f':
        resultat = full(cartes_joueur,cartes_devoile)

    #le carre (4 cartes meme rang)
    elif pari == 'ca':
        resultat = carre(cartes_joueur,cartes_devoile)
        
    #suite colore (suite + couleur)
    elif pari == 'sc':
        resultat = suiteColor(cartes_joueur,cartes_devoile)
    
    return resultat

def calcul_des_gains(cartes_joueur,cartes_flop,nouvelle_mise,pari,i,old_mise,lst_pari):
    gain,prob,gain_reel = 0,0,0
    li = i
    infich = 'C:/Users/nadbe_000/Desktop/probabilites.txt'
    # ouverture du fichir pour chercher la probabilité de p
    f = open(infich,'r')
    s = f.readlines()

    sp_file = []
    sp_file2 = []
    
    #essayeer d'optimiser ce monstre inefficace 
    if (succes(cartes_joueur,cartes_flop,pari)):
        for lines in s:
            sp_file = lines.split(" ")
            if ( pari in sp_file):
                for i in sp_file[1] :
                    if i.isdigit() or i == '.' :
                        sp_file2.append(i)
    
 
        sp_file = "".join(sp_file2)
        #basically je peux pas convertir un type de str en int c'est infesable?
        a = float(sp_file)
        #print("type de b: ",type(a),"valeur de :",a, "type de li :",type(li),"valeur de li :",li)
        gain = nouvelle_mise //((a/100)*li)
 
 
        gain_reel = gain - nouvelle_mise
        
        lst_pari.append((pari,gain_reel,nouvelle_mise,gain))
        
        
        
    
    old_mise -= nouvelle_mise
    f.close() 
    return old_mise,gain,lst_pari
    


def flop(cartes):

    #j'ai passer le jeu de 7 cartes, je sais que je ne dois seulement afficher
    #les 3 cartes après celle des joueurs
    
    cartes_flop = []
    cartes_flop_string = []
    for i in range(2,5):
        cartes_flop.append(cartes[i])
    for j in cartes_flop:
        cartes_flop_string.append(carte_to_string(j))

    print(MSG_PIOCHE2," ".join(cartes_flop_string))

    return cartes[0:5]

def turn(cartes):
    cartes_turn = []
    cartes_turn_string = []
    cartes_turn.append(cartes[5])
    cartes_turn_string.append(carte_to_string(cartes_turn[0]))

    print(MSG_PIOCHE3,cartes_turn_string[0])

    return cartes[0:6]
    
def river(cartes):
    cartes_river = []
    cartes_river_string = []
    cartes_river.append(cartes[6])
    cartes_river_string.append(carte_to_string(cartes_river[0]))

    print(MSG_PIOCHE4,cartes_river_string[0])

    return cartes[0:7]




############################################################################
#                                                                          #
#                           joueur humain                                  #
#                                                                          #
############################################################################

def erreurMise(nouvelle_mise,mise):
    if (nouvelle_mise.isalnum() == True):
        if(nouvelle_mise.isdigit()):
  
            nouvelle_mise = float(nouvelle_mise)
            nouvelle_mise = int(nouvelle_mise)

            if(nouvelle_mise > mise):

                print(MSG_ERREUR_MONTANT,mise,MSG_BITCOIN,":",sep="",end = " ")
                nouvelle_mise = input()
                return erreurMise(nouvelle_mise,mise)
            elif(0<= nouvelle_mise <= mise):

                return nouvelle_mise

        
    elif(nouvelle_mise.isalnum() == False) :
        
        #print("le montant nest pas un digit")
        print(MSG_ERREUR_MONTANT,mise,MSG_BITCOIN,":",sep="",end = " ")
        nouvelle_mise = input()
        return erreurMise(nouvelle_mise,mise)

def erreurReponse():
    reponse = input()
    reponse = reponse.upper()
    while ( reponse != 'O' and reponse != 'N' ):
        print(MSG_ERREUR_MISE,end = " ")
        reponse = input()
        reponse = reponse.upper()
          
    return reponse

def erreurPari():
    print(MSG_PARI_MISE)
    pari = input()
    pari = pari.upper()
    while(pari != 'P' and pari != 'DP' and pari != 'B' and pari != 'S' and pari != 'C' and pari != 'F' and pari != 'CA' and pari != 'SC'):
        print(MSG_ERREUR_PARI,end = " ")
        pari = input()
        pari = pari.upper()
    pari = pari.lower()

    return pari    

def mise_1(cartes,mise,deck,cartes_joueur,cartes_ordi,cartes_table,solde,lst_pari_ordi):
    i=1
    cartes_string = []
    #je veux avoir une liste avec la main du joueur en string 
    for j in range(0,2):
        cartes_string.append(carte_to_string(cartes_joueur[j]))

    print(MSG_PIOCHE1," ".join(cartes_string))    
    print(MSG_QUESTION_MISE,end = " ")

    reponse = erreurReponse()

    #pourquoi ma condition and marche ? Alors que or ne fait pas ce que c'est supposé faire...

    if (reponse == 'O'):

        pari = erreurPari()
        print(MSG_SOLDE,int(mise),MSG_BITCOIN,". ",MSG_RESTE_MISE,sep="",end=" ")
        nouvelle_mise = input()
        nouvelle_mise = erreurMise(nouvelle_mise,mise)
        #faire jouer l'ordinateur avant de piger les cartes du flop
        solde,gain_ordi,lst_pari_ordi = miseOrdinateur(deck,cartes_joueur,cartes_ordi,cartes_table,i,solde,lst_pari_ordi)
        cartes_flop = flop(cartes)

        
    elif (reponse == 'N' ):
        #on passe a letape suivante qui est flop et faire jouer ordi
        solde,gain_ordi,lst_pari_ordi = miseOrdinateur(deck,cartes_joueur,cartes_ordi,cartes_table,i,solde,lst_pari_ordi)
        cartes_flop = flop(cartes)
        nouvelle_mise = 0
        pari = ''

    return nouvelle_mise,pari,i,cartes_flop,mise,solde,gain_ordi,lst_pari_ordi 
    

def mise_2(cartes,mise,deck,cartes_joueur,cartes_ordi,cartes_table,i,solde,lst_pari_ordi):


    i=2
    cartes_string = []
    #je veux avoir une liste avec la main du joueur en string 
    for j in range(0,5):
        cartes_string.append(carte_to_string(cartes[j]))

    print(MSG_RECAP_CARTES," ".join(cartes_string[0:2]),"  "," ".join(cartes_string[2:5]))  
    print(MSG_QUESTION_MISE,end = " ")
    
    reponse = erreurReponse()

    if (reponse == 'O'):

        pari = erreurPari()
        
        print(MSG_SOLDE,int(mise),MSG_BITCOIN,". ",MSG_RESTE_MISE,sep="",end = " ")
        nouvelle_mise = input()
        nouvelle_mise = erreurMise(nouvelle_mise,mise)
        #faire jouer l'ordinateur avant de piger les cartes du turn
        solde,gain_ordi,lst_pari_ordi = miseOrdinateur(deck,cartes_joueur,cartes_ordi,cartes_table,i,solde,lst_pari_ordi)
        cartes_turn = turn(cartes)

        
    elif (reponse == 'N' ):
        #on passe a letape suivante qui est turn et faire jouer l'ordi
        solde,gain_ordi,lst_pari_ordi = miseOrdinateur(deck,cartes_joueur,cartes_ordi,cartes_table,i,solde,lst_pari_ordi)
        cartes_turn = turn(cartes)
        nouvelle_mise = 0
        pari = ''
    
    return nouvelle_mise,pari,i,cartes_turn,mise,solde,gain_ordi,lst_pari_ordi 





def mise_3(cartes,mise,deck,cartes_joueur,cartes_ordi,cartes_table,i,solde,lst_pari_ordi):
    i=3
    
    cartes_string = []
    #je veux avoir une liste avec la main du joueur en string 
    for j in range(0,6):
        cartes_string.append(carte_to_string(cartes[j]))

    print(MSG_RECAP_CARTES," ".join(cartes_string[0:2]),"  "," ".join(cartes_string[2:6]))    
    print(MSG_QUESTION_MISE, end = " ")
    
    reponse = erreurReponse()

    if (reponse == 'O'):
        
        pari = erreurPari()
        
        print(MSG_SOLDE,int(mise),MSG_BITCOIN,". ",MSG_RESTE_MISE,sep="",end = " ")
        nouvelle_mise = input()
        nouvelle_mise = erreurMise(nouvelle_mise,mise)
        #faire jouer l'ordinateur avant de piger les cartes de la riviere
        solde,gain_ordi,lst_pari_ordi = miseOrdinateur(deck,cartes_joueur,cartes_ordi,cartes_table,i,solde,lst_pari_ordi)
        cartes_river = river(cartes)

    
            
    elif (reponse == 'N' ):
        #on passe a letape suivante qui est river et faire jouer l'ordinateur avec de piger les cartes
        solde,gain_ordi,lst_pari_ordi = miseOrdinateur(deck,cartes_joueur,cartes_ordi,cartes_table,i,solde,lst_pari_ordi)
        cartes_river = river(cartes)
        nouvelle_mise = 0
        pari = ''
    
    return nouvelle_mise,pari,i,cartes_river,mise,solde,gain_ordi,lst_pari_ordi 



############################################################################
#                                                                          #
#                               SKYNET                                     #
#                                                                          #
############################################################################


def calcul_des_gains_ordi(cartes_joueur,cartes,nouvelle_mise,pari,i,old_mise,lst_pari_ordi):
    gain,prob,gain_reel = 0,0,0
    li = i
    infich = 'C:/Users/nadbe_000/Desktop/probabilites.txt'
    # ouverture du fichir pour chercher la probabilité de p
    f = open(infich,'r')
    s = f.readlines()

    sp_file = []
    sp_file2 = []
    
    #essayeer d'optimiser ce monstre inefficace 
    if (succes(cartes_joueur,cartes,pari)):
        for lines in s:
            sp_file = lines.split(" ")
            if ( pari in sp_file):
                for i in sp_file[1] :
                    if i.isdigit() or i == '.' :
                        sp_file2.append(i)
    
 
        sp_file = "".join(sp_file2)
        #basically je peux pas convertir un type de str en int c'est infesable?
        a = float(sp_file)
        #print("type de b: ",type(a),"valeur de :",a, "type de li :",type(li),"valeur de li :",li)
        gain = nouvelle_mise //((a/100)*li)
 
 
        gain_reel = gain - nouvelle_mise
        lst_pari_ordi.append((pari,gain_reel,nouvelle_mise,gain))
        
    old_mise -= nouvelle_mise
    f.close() 
    return old_mise,gain,lst_pari_ordi
    



def calculMise(index,combinaison,solde):

    montant = min(solde,max(1,int(solde*(combinaison[0][index]/MAX_IT))))
    return montant

def calculEsperance(combinaison,tour):
    resultat = 1
    prob = [79.0119,26.7607,7.7692,4.3718,3.0154,2.6563,0.1704,0.0283]
    ratioCombi = []
    for i in range(len(combinaison)):
        for j in range( 0,8):
            ratioCombi.append((combinaison[i][j]/MAX_IT)/((prob[j]/100)*tour))
    print("proba combi :",ratioCombi)
    if (max(ratioCombi) < 1) :
        resultat = 0

    return combinaison[0][ratioCombi.index(max(ratioCombi))],ratioCombi.index(max(ratioCombi)),resultat
    
def capturePari(index):
    pari = ['p','dp','b','s','c','f','ca','sc']
    return pari[index]

def miseOrdinateur(deck,cartes_joueur,cartes_ordi,cartes_table,tour,solde,lst_pari_ordi):
    pari = ''
    #creation de la liste de cartes inconnues et connues
    
    jeu = []
    cartes = []
    cartes_inconnues = []
    cartes_connues = []

    
    if(tour==1):
        #print("cartes de la table inconnue : ",cartes_table[0:],"cartes joueur",cartes_joueur)
        #assignation du deck et cartes_j et cartes_tables inconnue a cartes_inconnues
        cartes_inconnues = deck + cartes_joueur + cartes_table[0:]
        #au premier tour, il n'y a pas de cartes connues sur la table sauf celle de l'ordi
        cartes_connues = cartes_ordi
        #print("carte connue de l ordi: ",cartes_connues)
        j=5
        
    elif(tour==2):
        #print("cartes de la table inconnue : ",cartes_table[3:],"cartes joueur",cartes_joueur)
        #assignation du deck et cartes_j et cartes_tables inconnue a cartes_inconnues
        cartes_inconnues = deck + cartes_joueur + cartes_table[3:]
        #print("cartes de la table connue : ",cartes_table[:3],"cartes joueur",cartes_joueur)
        #au deuxieme tour les cartes connues sont les 3 dernières cartes de la table 
        cartes_connues = cartes_ordi + cartes_table[:3]
        #print("carte connue de l ordi: ",cartes_connues)
        j=2

    elif(tour==3):
        #print("cartes de la table inconnue : ",cartes_table[4:],"cartes joueur",cartes_joueur)
        #assignation du deck et cartes_j et cartes_tables inconnue a cartes_inconnues
        cartes_inconnues = deck + cartes_joueur + cartes_table[4:]
        #print("cartes de la table connue : ",cartes_table[:4],"cartes joueur",cartes_joueur)
        #Finalement une seule carte n'est pas connue et c'est la premiere
        cartes_connues = cartes_ordi + cartes_table[:4]
        #print("carte connue de l ordi: ",cartes_connues)
        j=1
    

    combinaison = []
    p,dp,b,c,f,ca,sc,s=0,0,0,0,0,0,0,0
    for i in range(MAX_IT):
        jeu = cartes_connues + random.sample(cartes_inconnues,j)
        
        resultat = pair(cartes_ordi,jeu)
        if(resultat):
            p+=1
        
        resultat = doublePair(cartes_ordi,jeu)
        if(resultat):
            dp+=1        

        resultat = brelan(cartes_ordi,jeu)
        if(resultat):
            b+=1        

        resultat = suite(cartes_ordi,jeu)
        if(resultat):
            s+=1

        resultat = couleur(cartes_ordi,jeu)
        if(resultat):
            c+=1                            
        #le full (brelan + paire)
        resultat = full(cartes_ordi,jeu)
        if(resultat):
            f+=1
        #le carre (4 cartes meme rang)
        resultat = carre(cartes_ordi,jeu)
        if(resultat):
            ca+=1        
        #suite colore (suite + couleur)
        resultat = suiteColor(cartes_ordi,jeu)
        if(resultat):
            sc+=1

    combinaison.append((p,dp,b,s,c,f,ca,sc))
    #combinaison.append((p/MAX_IT,dp/MAX_IT,b/MAX_IT,s/MAX_IT,c/MAX_IT,f/MAX_IT,ca/MAX_IT,sc/MAX_IT))
    print(combinaison)
    maxEsperance,index,resultat = calculEsperance(combinaison,tour)
    #print("resultat :", index)
    cartes = cartes_ordi + cartes_table
    if(resultat == 1):
        montant = calculMise(index,combinaison,solde)
        pari = capturePari(index)
        print(MSG_MISE_ORDI, montant,MSG_PARI_ORDI,pari)
        solde,gain_ordi,lst_pari_ordi = calcul_des_gains_ordi(cartes_ordi,cartes,montant,pari,tour,solde,lst_pari_ordi)

  
    else :
        print(MSG_PARI_RIEN_ORDI)
        gain_ordi = 0
 


    return solde,gain_ordi,lst_pari_ordi

##def rejouer():
##    
    
# le s == un nombre deterministe pour initialiser le random
def poker_contre_ordi(s):

    
    random.seed(s)
    

    #Je cree mon jeu de carte de 52 cartes
    deck = creer_jeu()
    
    #shuffle le deck
    random.shuffle(deck)

    #Dans cartes, les 7 cartes a pigé au hasard sont tirés dès le début
    #creation des jeux de mes 2 joueurs ordi et joueur humain plus creation des cartes sur la table
    cartes_joueur = [deck.pop(),deck.pop()]
    cartes_ordi = [deck.pop(),deck.pop()]
    cartes_table = [deck.pop() for i in range(5)]

    #je cree le jeu de carte de mon joueur avec les cartes sur la table à part ainsi que celle de l'ordi (pour me faciliter la tache plus tard)
    cartes = cartes_joueur + cartes_table
    cartes_2 = cartes_ordi + cartes_table
   
    #premiere mise du jeu + flop et calcul du gain
    nouvelle_mise,reponse= 100,'O'
    g=0
    #cree la liste des paris
    lst_pari_ordi = []
    lst_pari = []
    solde = 100
    while(reponse != 'N'):
 
        nouvelle_mise,pari,i,cartes_devoile,old_mise,solde_ordi,gain_ordi,lst_pari_ordi  = mise_1(cartes,nouvelle_mise,deck,cartes_joueur,cartes_ordi,cartes_table,solde,lst_pari_ordi)
        gain,g,lst_pari = calcul_des_gains(cartes_joueur,cartes,nouvelle_mise,pari,i,old_mise,lst_pari)

        
        nouvelle_mise,pari,i,cartes_devoile,old_mise,solde_ordi,gain_ordi,lst_pari_ordi  = mise_2(cartes,gain,deck,cartes_joueur,cartes_ordi,cartes_table,i,solde_ordi,lst_pari_ordi)
        gain,g,lst_pari = calcul_des_gains(cartes_joueur,cartes,nouvelle_mise,pari,i,gain,lst_pari)

        nouvelle_mise,pari,i,cartes_devoile,old_mise,solde_ordi,gain_ordi,lst_pari_ordi  = mise_3(cartes,gain,deck,cartes_joueur,cartes_ordi,cartes_table,i,solde_ordi,lst_pari_ordi)
        gain,g,lst_pari = calcul_des_gains(cartes_joueur,cartes,nouvelle_mise,pari,i,gain,lst_pari)

        cartes_string = []
        cartes_string_ordi = []
        for j in range(0,7):
            cartes_string.append(carte_to_string(cartes[j]))
            cartes_string_ordi.append(carte_to_string(cartes_2[j]))

            
        
        print(MSG_RECAP_CARTES," ".join(cartes_string[0:2]),"  "," ".join(cartes_string[2:7]))
        print(MSG_RECAP_CARTES_ORDI," ".join(cartes_string_ordi[0:2]),"  "," ".join(cartes_string_ordi[2:7]))

        

        ##calcul des gains du joueur
        for i,j,k,l in lst_pari :
            print(MSG_GAIN_PARI_1,i,":", int(k), MSG_GAIN_PARI_2, int(j),MSG_BITCOIN,sep="")

        l = sum(l for i,j,k,l in lst_pari)

        if(l):
            gain += l

        ##calcul des gains de l'ordi, meme approche

        for i,j,k,l in lst_pari_ordi :
            print(MSG_GAIN_PARI_1_ORDI,i,":", int(k), MSG_GAIN_PARI_2_ORDI, int(j),MSG_BITCOIN,sep="")

        l = sum(l for i,j,k,l in lst_pari_ordi)

        if(l):
            solde_ordi += l

        if(int(gain) <= 0):
            break;

        
        print(MSG_SOLDE,int(gain),MSG_BITCOIN,sep="")
        print(MSG_SOLDE_ORDI,int(solde_ordi),MSG_BITCOIN,   "\n",sep="")


        print(MSG_CONTINUER)
        reponse = input()
        reponse = reponse.upper()
    
        while ( reponse != 'O' and reponse != 'N' ):
            reponse = input(MSG_ERREUR_MISE)
            reponse = reponse.upper()
        
        #je reshuffle s'il desire continuer a jouer#
        if(reponse == 'O'):
            nouvelle_mise = gain #je dois attribuer gain a nouvelle_mise si on rejoue, car gain == old_mise en realite
            solde = solde_ordi
            lst_pari = []#la liste des paris doit etre resetter a 0
            lst_pari_ordi = [] #liste des paris ordi reset
            
            #nouveau deck

            newDeck = cartes_table + cartes_joueur + cartes_table
            random.shuffle(newDeck)

            cartes_joueur = [newDeck.pop(),newDeck.pop()]
            cartes_ordi = [newDeck.pop(),newDeck.pop()]
            cartes_table = [newDeck.pop() for i in range(5)]

            #je cree le jeu de carte de mon joueur avec les cartes sur la table à part ainsi que celle de l'ordi (pour me faciliter la tache plus tard)
            cartes = cartes_joueur + cartes_table
            cartes_2 = cartes_ordi + cartes_table
           


        elif(reponse == 'N'):
            if(int(solde_ordi) > int(gain)):
                print(MSG_FIN_PERDU)
            else : print(MSG_FIN_GAGNE)


s=2732
#s=2000
poker_contre_ordi(s)


    
    
