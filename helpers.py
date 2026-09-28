import constants as const

def retrouve_classe(classe: str):
    """ Fonction simple, qui donne le chiffre de la classe du seconde,
        Si l'eleve est de la classe 2NDE 5, la fonction renvoie 5.
        On peut ajouter plusieurs cas comme les classes de premier et
        terminale si on veut.     
    """
    if ("2NDE " in classe):
        return classe[5]



def purifier_liste_eleves(liste_eleves: list, filtrage_spe, opt_exclu_spe=True)-> list:
    """Tres importante, elle nous permet sorter les eleves parmi les options suivantes:
        filtrage_spe -> Any mais la valeur reelle attendu est de str OU None.
        opt_exclu_spe -> booleen qui decide si on supprime les eleves avec un avis NON
    """
    resultat = []
    for eleve in liste_eleves:
        excluded = False
        filtered_spe_found = False
        for cle,spe in eleve.items():
            if cle not in const.useless_domains_voeux:
                if((opt_exclu_spe is True and spe in const.exclu_spe) or (cle == const.qAvis and spe == "Non")):
                    excluded = True
                    break
                if(spe == filtrage_spe or filtrage_spe is None):
                    filtered_spe_found = True
        if(excluded is False and filtered_spe_found):
            resultat.append(eleve)
    return resultat

def demande(options: list):
    """ Fonction recursive, Il demande une reponse valide parmi la liste "options" qu'on donne
        comme parametre.
    """
    resultat = input("Reponse: ").lower()
    if ( resultat in options):
        return resultat
    return demande(options)
