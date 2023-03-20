#Ce ci est un module comportant les fonctions necessaires pour la réalisaion du jeu
def saisir_nom():
    """Elle permet de saisir le nom du joueur"   """
    while True:
        nom_joueur = input("Veillez entrer votre nom: ")
        if nom_joueur.isdigit():
            print("Nom invalide")
        else: 
            return nom_joueur
            break


def saisir_lettre():
    """Fonction gère la saisir du joureur. Il renvoie une lettre  """
    while True:
        lettre_choisie = input("Veillez choisir une lettre: ").upper()
        longueur = len(lettre_choisie)
        if longueur!=1:
            print("Saisir invalide")
        else: 
            code = ord(lettre_choisie)
            if code >=65 and code<=90:
                return lettre_choisie
                break
            else:
                print(f"{lettre_choisie} is not a letter!")

def recherche(mot, lettre):
    """Cette fonction prend en entrer deux paramètre: mot et lettre
    et renvoi un liste de la position que l'élement occupe dans le mot ou none dans le cas contraire"""
    les_positions = []
    for i,j in enumerate(mot):
        if lettre == j:
            les_positions.append(i)
    if len(les_positions)!=0:
        return les_positions
    else:
        return None;

def traitement(mot_a_trouver,lettre,mot_trouver, score):
    """_summary_

    Args:
        mot_a_trouver (_chaine de caract_re): le mot existant
        lettre (caractère): une lettre majuscule que
        mot_trouver (chaine de caractere): le mot insuffissant
    """
    positions = recherche(mot_a_trouver,lettre)
    if positions == None:
        print(f" {lettre } ne se trouve pas dans le mot à trouver!")
        score -=1
        return mot_trouver,score
    else:    
        for i in positions:
            score +=1 
            mot_trouver[i]=lettre
        print(f"Bien jouer! Voici le mot {''.join(mot_trouver)}")
        return mot_trouver,score

def correspondance(mot_a_trouver, mot_trouver):
    """ Ielle prend à l'entré deux parametre: mot a trouver et mot touver et renvoie une True si les deux sont identique
    et False dans le cas contraire"""
    if mot_a_trouver == "".join(mot_trouver):
        return True
    else:
        return False