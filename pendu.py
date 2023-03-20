"""  TP: Un bon vieux pendu  """
import os
import donnees
import fonctions
import random

vie = donnees.notre_de_vie
dictionnaire = donnees.boite_mot
score = 0
mot_cacher = random.choice(dictionnaire)# Le mot que le joueur doit trouver
mon_mot = ["*" for i in range(len(mot_cacher))] #Initialisation du mot qu'il a trouver

joueur = fonctions.saisir_nom()  #Saisir du nom du joureur
while vie>=1:
    lettre = fonctions.saisir_lettre() #Saisir de la lettre par le joueur
    mon_mot,score_finale = fonctions.traitement(mot_cacher, lettre, mon_mot,score) 
    validation = fonctions.correspondance(mot_cacher, mon_mot)
    score= score_finale
    if validation :
        print(f"Super vous avez réussi à trouver le mot {mot_cacher}. Votre score est {score}")
        break
    else: 
        vie -=1
    
    if vie == 0:
        print(f"Partie terminer! le moment à trouver est : {mot_cacher}")    

fichier = "E:/AUTO_FORMATION/PYTHON/ApprendrePython/FICHIER/scores"
try:
    with open( fichier, "a") as scores_file:
        mon_score = {joueur : score}
        scores_file.write(f"{mon_score}\n")
        scores_file.close()
        
except FileNotFoundError:
    print(f"Le chemin {fichier} est incorrecte")


os.system("pause")    