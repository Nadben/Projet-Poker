#--------Questions qui viennent au fur et a mesure------#



#-----------------------------liste de shits a faire------------#

##mettre les messages "votre pari a rapporte X Bitcoin " a la fin du programme.... fait, mais a retravailler
##gerer les erreurs utilisateurs (inferiorite a la mise du moment)
##nous ne pouvons jamais miser plus que la mise elle-meme et a chaque tour ce quon a miser est reduit de la mise
##faire en sorte que si une mise est vrai au ieme tour son pari soit comptabiliser
##restructurer le code (pour tp 2)





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
        resultat,j=0,1
            
        for k in range(0,len(cartes_devoile)):
            carte_suite.append(cartes_devoile[k][0])
        carte_suite.sort()
        for i in range(len(carte_suite) - 1) :
            if ( carte_suite[i+1] - carte_suite[i]  != 1) : resultat = 0
            else :
                j+=1

        if(j>=5): resultat = 1

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
            if( h>=3 ): main.append(g)
            if( h==2 ): main.append(g)
 

        if(len(main) >= 2 ):resultat = 1

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
        if(suite(cartes_joueur,cartes_devoile) and couleur(cartes_joueur,cartes_devoile)):
            resultat = 1

    

    return resultat

def calcul_des_gains(cartes_joueur,cartes_flop,nouvelle_mise,pari,i,old_mise,lst_pari):
    gain,prob,gain_reel = 0,0,0
    li = i
    infich = FICHIER_PROBABILITE
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

def mise_1(cartes,cartes_joueur,mise):
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
        
        cartes_flop = flop(cartes)

        
    elif (reponse == 'N' ):
        #on passe a letape suivante qui est flop
        cartes_flop = flop(cartes)
        nouvelle_mise = 0
        pari = ''
    
    return nouvelle_mise,pari,i,cartes_flop,mise
    

def mise_2(cartes,cartes_joueur,mise):


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
        
        cartes_turn = turn(cartes)

        
    elif (reponse == 'N' ):
        #on passe a letape suivante qui est turn
        cartes_turn = turn(cartes)
        nouvelle_mise = 0
        pari = ''
    
    return nouvelle_mise,pari,i,cartes_turn,mise





def mise_3(cartes,cartes_joueur,mise):
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
        
        cartes_river = river(cartes)

        
    elif (reponse == 'N' ):
        #on passe a letape suivante qui est river
        cartes_river = river(cartes)
        nouvelle_mise = 0
        pari = ''
    
    return nouvelle_mise,pari,i,cartes_river,mise


def calculMise(a,solde):
    print(a,solde)
    tm.sleep(5)
    montant = min(solde,max(1,int(solde*a)))
    return montant


def calculEsperance(combinaison,tour):
    resultat = 0
    prob = [79.0119,26.7607,7.7692,4.3718,3.0154,2.6563,0.1704,0.0283]
    ratioCombi = []
    for i in range(len(combinaison)):
        for j in range(0,8):
            ratioCombi.append(combinaison[i][j]/prob[i]*tour)

    if max(ratioCombi) < 1 :
        resultat = 1
    
    return combinaison[0][ratioCombi.index(max(ratioCombi))],resultat
    


def miseOrdinateur(deck,cartes_joueur,cartes_ordi,cartes_table,i,j,tour,solde):

    if(tour==1):
        i+=3
        j-=3
    elif(tour==2):
        i+=1
        j-=1
    elif(tour==3):
        i+=1
        j-=1
    
    
    #creation de la liste de cartes inconnues et connues
    jeu = []
    cartes_inconnues = []
    cartes_connues = []
    #assignation du deck et cartes_j et cartes_tables inconnue a cartes_inconnues

    cartes_inconnues = deck + cartes_joueur + cartes_table[:j]
    #assignation des cartes connues et cartes sur tables devoile a cartes_connues

    cartes_connues = cartes_ordi + cartes_table[j:]
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
        resultat = (suite(cartes_ordi,jeu) and couleur(cartes_joueur,jeu))
        if(resultat):
            sc+=1         

    
    combinaison.append((p/MAX_IT,dp/MAX_IT,b/MAX_IT,s/MAX_IT,c/MAX_IT,f/MAX_IT,ca/MAX_IT,sc/MAX_IT))
    a,resultat = calculEsperance(combinaison,tour)

    if(resultat == 0):
        print("Computer will skip the turn")
    else :
        montant = calculMise(a,solde)
        print(montant)
 

    tm.sleep(5000)

    #return combinaison
    
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

    #je cree le jeu de carte de mon joueur avec les cartes sur la table à part
    
    cartes = cartes_table + cartes_joueur
 
   
    #premiere mise du jeu + flop et calcul du gain
    nouvelle_mise,reponse= 100,'O'
    g,j,k=0,5,0
    #cree la liste des paris
    lst_pari = []
    
    while(reponse != 'N'):
 
        nouvelle_mise,pari,i,cartes_devoile,old_mise = mise_1(cartes,cartes_joueur,nouvelle_mise)
        miseOrdinateur(deck,cartes_joueur,cartes_ordi,cartes_table,k,j,i)
        gain,g,lst_pari = calcul_des_gains(cartes_joueur,cartes,nouvelle_mise,pari,i,old_mise,lst_pari)

        
        nouvelle_mise,pari,i,cartes_devoile,old_mise = mise_2(cartes,cartes,gain)
        gain,g,lst_pari = calcul_des_gains(cartes_joueur,cartes,nouvelle_mise,pari,i,gain,lst_pari)

        nouvelle_mise,pari,i,cartes_devoile,old_mise = mise_3(cartes,cartes,gain)
        gain,g,lst_pari = calcul_des_gains(cartes_joueur,cartes,nouvelle_mise,pari,i,gain,lst_pari)

        cartes_string = []
        for j in range(0,7):
            cartes_string.append(carte_to_string(cartes[j]))
        
        print(MSG_RECAP_CARTES," ".join(cartes_string[0:2]),"  "," ".join(cartes_string[2:7]))
        
        for i,j,k,l in lst_pari :
            
            print(MSG_GAIN_PARI_1,i,":", int(k), MSG_GAIN_PARI_2, int(j),MSG_BITCOIN,sep="")

        l = sum(l for i,j,k,l in lst_pari)

        if(l):
            gain += l

        if(int(gain) <= 0):
            break;        
      
        print(MSG_SOLDE,int(gain),MSG_BITCOIN,   "\n",sep="")
        print(MSG_CONTINUER)
        reponse = input()
        reponse = reponse.upper()
    
        while ( reponse != 'O' and reponse != 'N' ):
            reponse = input(MSG_ERREUR_MISE)
            reponse = reponse.upper()
        
        #je reshuffle s'il desire continuer a jouer#
        if(reponse == 'O'):
            nouvelle_mise = gain #je dois attribuer gain a nouvelle_mise si on rejoue, car gain == old_mise en realite    
            lst_pari = []#la liste des paris doit etre resetter a 0
            cartes = random.sample(deck, 7)

            cartes_joueur = []
            for i in range(0,2):
                cartes_joueur.append(cartes[i])

        elif(reponse == 'N'):
            print(MSG_FIN_1, int(gain),MSG_FIN_2,sep="")



s=2000

poker_contre_ordi(s)


    
    
