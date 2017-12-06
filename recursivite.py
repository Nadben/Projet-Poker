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
MSG_CONTINUER = "Voulez-vous continuer à jouer [O/N]?"
MSG_FIN_1 = "Merci d'avoir joué. Vous repartez avec "
MSG_FIN_2 = " Ƀ. Bye"
MSG_GAIN_PARI_1 = "Votre pari "
MSG_GAIN_PARI_2 = " vous a rapporté "
FICHIER_PROBABILITE = "/pub/data/probabilites.txt"



def erreurMise(nouvelle_mise,mise):
    print(nouvelle_mise, mise)   
    print(nouvelle_mise.isalnum())
    if (nouvelle_mise.isalnum() == True):
        if(nouvelle_mise.isdigit()):
            print("le montant est un digit")
            nouvelle_mise = float(nouvelle_mise)
            nouvelle_mise = int(nouvelle_mise)
            print("yolo")
            if(nouvelle_mise >= mise):
                #probablement un petit probleme ici...
                print("trop grand")
                print(MSG_ERREUR_MONTANT,mise,end = "")
                nouvelle_mise = input()
                erreurMise(nouvelle_mise,mise)
            elif(0<= nouvelle_mise <= mise):
                print("le montant est fucking correcte je sors chow")
                return nouvelle_mise

        
    elif(nouvelle_mise.isalnum() == False) :
        
        print("le montant nest pas un digit")
        print(MSG_ERREUR_MONTANT,mise,end = "")
        nouvelle_mise = input()
        erreurMise(nouvelle_mise,mise)

    #return nouvelle_mise

mise=100
nouvelle_mise = input()
nouvelle_mise = erreurMise(nouvelle_mise,mise)
tm.sleep(2)
print(nouvelle_mise)
