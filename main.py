
import helpers as h
import stats


def main():
    """Initialisation principale, appelle main pour consistance et pratiques communs"""
    menu()



def menu():
    """La fonction qui lance tous les options pour l'utilisateur."""
    print("Bonjour, bien venu sur la platforme de filtrage des eleves!")
    while(True):
        
        for key,option in optionsMenu.items():
            print(f"{key}: {option[0]}")
        print("_" * 70)
        resultat = h.demande(optionsMenu.keys())
        optionsMenu[resultat][1]()




optionsMenu = {
"1" : ("Donner tous les eleves d'un spe specifie", stats.eleve_par_spe ),
"2" : ("Generer le fichier de pourcentage garcon/filles par spe", stats.ratio_fg),
"3" : ("Generer le nombre de triplettes par combinaison de spe", stats.nb_eleve_triplette),
"4" : ("Savoir la pourcentage des eleves qui ont fait des voeux parmi la totale", stats.part_voeux),
"5" : ("Savoir la pourcentage de voeux ayant reçu un avis favorable du \
conseil de classe", stats.part_premiere),
"6" : ("Quitte", exit)
} 

main()