#--------Questions qui viennent au fur et a mesure------#
# mes cartes que je tire sont tout le temps les mêmes, est-ce que c'est normale?
#Je crois que c'Est en fonction de mon seed , si mon seed est constant alors
#mon random est tout le temps initialiser a la meme chose (d'où le pseudo-random)

#dans cette fonction je veux savoir si le joueur a eu un succès ou non
# A chaque mise ? ex : premiere mise le joueur dis paire et je regarde
#s'il y a effectivemeent une paire dans le flop et ainsi de suite?


#-----------librairies-------- #

import random
import time as tm

# ----------- Inputs --------- # 
MSG_PIOCHE1 = "Voici vos deux premières cartes: "
MSG_PIOCHE2 = "Voici les trois cartes du flop: "
MSG_PIOCHE3 = "Voici la carte du turn: " 
MSG_PIOCHE4 = "Voici la carte de la river: "
MSG_RECAP_CARTES = "Vous avez donc à votre disposition les cartes suivantes:"
MSG_QUESTION_MISE = "Voulez-vous miser quelque chose [O/N]?"
MSG_ERREUR_MISE = "Veuillez répondre par Oui ou par Non:"
MSG_PARI_MISE = "Sur quel résultat voulez-vous miser [p/dp/b/s/c/f/ca/sc] ?"
MSG_ERREUR_PARI = "Veuillez entrer un résultat valable : p/dp/b/s/c/f/ca/sc ?"
MSG_RESTE_MISE = "Combien voulez-vous miser?"
MSG_BITCOIN = "Ƀ"
MSG_ERREUR_MONTANT = "Veuillez entrer un montant entier positif inférieur à "
MSG_SOLDE = "Il vous reste "
MSG_CONTINUER = "Voulez-vous continuer à jouer [O/N]? "
MSG_FIN_1 = "Merci d'avoir joué. Vous repartez avec "
MSG_FIN_2 = " Ƀ. Bye"
MSG_GAIN_PARI_1 = "Votre pari "
MSG_GAIN_PARI_2 = " vous a rapporté "
FICHIER_PROBABILITE = "/pub/data/probabilites.txt"



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


def succes(cartes_joueur,cartes_devoile,pari):

    resultat = 0
    i=0
    if pari == 'p':
        for j in range(0,2):
            for k in range(0,len(cartes_devoile)):
                if(cartes_joueur[j][0] == cartes_devoile[k][0]):
                    i+=1

                elif(cartes_joueur[0][0] == cartes_joueur[1][0]):
                    i+=1

        if(i >= 1):
            resultat = 1
            
        
    elif pari == 'dp':
        for j in range(0,2):
            for k in range(0,len(cartes_devoile)):
                if(cartes_joueur[j][0] == cartes_devoile[k][0]):
                    i+=1

                elif(cartes_joueur[0][0] == cartes_joueur[1][0]):
                    i+=1

        if(i >= 2 ):
            resultat = 1

    elif pari == 'b':
        for j in range(0,2):
            for k in range(0, len(cartes_devoile)):
                if(cartes_joueur[j][0] == cartes_devoile[k][0]):
                    i+=1

                elif(cartes_joueur[0][0] == cartes_joueur[1][0]):
                    i+=1
        if(i>=3):
            resultat = 1

    elif pari == 's':
        #append mon jeu de carte joueur avec ddevoile
        carte_suite = []
        for j in range(0,2):
            carte_suite.append(cartes_joueur[j][0])
            
        for k in range(0,len(cartes_devoile)):
            carte_suite.append(cartes_devoile[k][0])
            carte_suite.sort()
            for i in range(len(carte_suite) -1) :
                if ( carte_suite[i+1] - carte_suite[i]  != 1) : resultat = 0
                else : resultat = 1
                  
                

    elif pari == 'c':
        carte_couleur = []
        for i in range(0,2):
            carte_couleur.append(cartes_joueur[0][i])
        for j in range(0, len(carte_devoile)):
            carte_couleur.append(cartes_devoile[0][j])
        for k in range(len(carte_couleur)-1):
            if (carte_couleur[k+1] != carte_couleur[k]): resultat = 0
            else : resultat = 1

    
                            

    elif pari == 'f':
        

    #elif pari == 'ca':

    #elif pari == 'sc':  
            
    
    #else : resultat = 0

    return resultat

def calcul_des_gains(cartes_joueur,cartes_flop,nouvelle_mise,pari,i,old_mise):
    gain,prob = 0,0

    infich = 'C:/Users/nadbe_000/Desktop/probabilites.txt'
    # ouverture du fichir pour chercher la probabilité de p
    f = open(infich,'r')
    s = f.readlines()
    sp_file = []
    sp_file2 = []

    if (succes(cartes_joueur,cartes_flop,pari)):
        for lines in s:
            sp_file = lines.split(" ")
            if ( pari in sp_file):
                for i in sp_file[1] :
                    if i.isdigit() or i == '.' :
                        sp_file2.append(i)
    
 
        sp_file = "".join(sp_file2)                
        prob = float(sp_file)
        gain = nouvelle_mise * (1/(prob))# ici je dois rajouter le i em tour... probleme de type
        old_mise += gain                    

    else : old_mise -= nouvelle_mise
    f.close() 
    return old_mise



def flop(cartes):

    #j'ai passer le jeu de 7 cartes, je sais que je ne dois seulement afficher
    #les 3 cartes après celle des joueurs
    
    cartes_flop = []
    cartes_flop_string = []
    for i in range(2,5):
        cartes_flop.append(cartes[i])
    for j in cartes_flop:
        cartes_flop_string.append(carte_to_string(j))

    print(MSG_PIOCHE2,cartes_flop_string[0:3])

    return cartes_flop

def turn(cartes):
    cartes_turn = []
    cartes_turn_string = []
    cartes_turn.append(cartes[5])
    cartes_turn_string.append(carte_to_string(cartes_turn[0]))

    print(MSG_PIOCHE3,cartes_turn_string[0])

    return cartes[2:5]
    
def river(cartes):
    cartes_river = []
    cartes_river_string = []
    cartes_river.append(cartes[6])
    cartes_river_string.append(carte_to_string(cartes_river[0]))

    print(MSG_PIOCHE3,cartes_river_string[0])

    return cartes[0:6]



    

def mise_1(cartes,cartes_joueur,mise):
    
    i=1
    cartes_string = []
    #je veux avoir une liste avec la main du joueur en string 
    for i in range(0,2):
        cartes_string.append(carte_to_string(cartes_joueur[i]))

    print(MSG_PIOCHE1,cartes_string)
    
    reponse = input(MSG_QUESTION_MISE)
    reponse = reponse.upper()
    #pourquoi ma condition and marche ? Alors que or ne fait pas ce que c'est supposé faire...
    while ( reponse != 'O' and reponse != 'N' ):
        reponse = input(MSG_ERREUR_MISE)
        reponse = reponse.upper()
        
    if (reponse == 'O'):
        pari = input(MSG_PARI_MISE)
        print(MSG_SOLDE,mise,MSG_BITCOIN,MSG_RESTE_MISE,end="")
        nouvelle_mise = float(input())
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
    for i in range(0,5):
        cartes_string.append(carte_to_string(cartes[i]))

    print(MSG_RECAP_CARTES,cartes_string)
    
    reponse = input(MSG_QUESTION_MISE)
    reponse = reponse.upper()
    
    #pourquoi ma condition and marche ? Alors que or ne fait pas ce que c'est supposé faire...
    while ( reponse != 'O' and reponse != 'N' ):
        reponse = input(MSG_ERREUR_MISE)
        reponse = reponse.upper()
        
    if (reponse == 'O'):
        pari = input(MSG_PARI_MISE)
        print(MSG_SOLDE,mise,MSG_BITCOIN,MSG_RESTE_MISE,end="")
        nouvelle_mise = float(input())
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
    for i in range(0,6):
        cartes_string.append(carte_to_string(cartes[i]))

    print(MSG_RECAP_CARTES,cartes_string)
    
    reponse = input(MSG_QUESTION_MISE)
    reponse = reponse.upper()
    
    #pourquoi ma condition and marche ? Alors que or ne fait pas ce que c'est supposé faire...
    while ( reponse != 'O' and reponse != 'N' ):
        reponse = input(MSG_ERREUR_MISE)
        reponse = reponse.upper()
        
    if (reponse == 'O'):
        pari = input(MSG_PARI_MISE)
        print(MSG_SOLDE,mise,MSG_BITCOIN,MSG_RESTE_MISE,end="")
        nouvelle_mise = float(input())
        cartes_river = river(cartes)

        
    elif (reponse == 'N' ):
        #on passe a letape suivante qui est river
        cartes_river = river(cartes)
        nouvelle_mise = 0
        pari = ''
    
    return nouvelle_mise,pari,i,cartes_river,mise




# le s == un nombre deterministe pour initialiser le random
def poker_un_joueur(s):
    
    random.seed(s)

    #Je cree mon jeu de carte de 52 cartes
    deck = creer_jeu()

    #Dans cartes, les 7 cartes a pigé au hasard sont tirés dès le début
    cartes = random.sample(deck, 7)

    #je cree le jeu de carte de mon joueur à part
    cartes_joueur = []
    for i in range(0,2):
        cartes_joueur.append(cartes[i])
 
   
    #premiere mise du jeu + flop et calcul du gain
    mise = 100
    nouvelle_mise,pari,i,cartes_devoile,old_mise = mise_1(cartes,cartes_joueur,mise)
    gain = calcul_des_gains(cartes_joueur,cartes_devoile,nouvelle_mise,pari,i,old_mise)

    nouvelle_mise,pari,i,cartes_devoile,old_mise = mise_2(cartes,cartes_joueur,gain)
    gain = calcul_des_gains(cartes_joueur,cartes_devoile,nouvelle_mise,pari,i,gain)

    nouvelle_mise,pari,i,cartes_devoile,old_mise = mise_3(cartes,cartes_joueur,gain)
    gain = calcul_des_gains(cartes_joueur,cartes_devoile,nouvelle_mise,pari,i,gain)
   

    print(MSG_FIN_1, gain , MSG_FIN_2)
    


s = 20000
poker_un_joueur(s)









    
    
