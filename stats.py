from os import listdir, getcwd
import constants as const
from creer_pdf import creer_pdf_tableau1
import helpers as h
import chargement as charge
from os.path import isfile, join


def eleve_par_spe():
    """Fonction qui permet a sorter tous les eleves qui ont le spe x,
        L'utilisateur est premierement demande a faire une choix."""
    print("S'il vous plait selectionnez un matiere pour filtrer les eleves")
    print("Les spes possibles:")
    print("_" * 70)
    textOptions = ""
    numeroSpe = 0
    for alias,spe in const.optionsSpe.items():

        if(numeroSpe % 3 == 0):
            textOptions += f"\n{alias}: {spe}"
        else:
            textOptions += (" " * (30 - (len(spe) + (len(alias) + 3))) + f" {alias}: {spe}")
        numeroSpe+=1
    print(textOptions)
    resultatSpe = h.demande(const.optionsSpe)
    spe_choisie = const.optionsSpe[resultatSpe]

    eleves_filtre= h.purifier_liste_eleves(union, spe_choisie)

    fichiers_classes = {}
    eleves_et_moyennes = []

    for eleve in eleves_filtre:
        classe = "20" + h.retrouve_classe(eleve["Classe"])
        fichier_eleve_en_classe = []
        if(classe not in fichiers_classes):
            fichiers_classes[classe] = charge.lire_csv(f"resultats_classe/{classe}.csv")
        fichier_eleve_en_classe = trouver_eleve_par_nom(fichiers_classes[classe], eleve["Nom"])
        eleve_pret = enregistrement_moyennes(fichier_eleve_en_classe, spe_choisie)
        eleves_et_moyennes.append(eleve_pret)
    #print(eleves_et_moyennes)
    titre = f"eleves_de_voeux_{spe_choisie}.pdf"
    header = [const.qNom, const.qClasse, const.qMoyenneGlobale, \
              const.qMoyenneMatieresSpe] + const.dico_spe[spe_choisie]
    data = [header] + eleves_et_moyennes


    print(f"Sans Filtre: {len(union)} \
            | Avec Filtre Actif: {len(eleves_filtre)}")
    creer_pdf_tableau1(titre, \
                        f"Élèves de toutes les classes avec le voeu {spe_choisie}", data)
    print(f"Le PDF {titre} a ete bien enregistre!")
    return eleves_et_moyennes

def ratio_fg():
    """ Fonction qui permet savoir le ratio de fille:garcon parmi chaque spe.
        Les eleves qui quitte l'ecole ou ont eu l'avis de "Non" sont supprime de ce calcul.
    """
    resultat = {spe: [0, 0] for spe in const.dico_spe if spe not in const.exclu_spe}
    eleves_filtre = h.purifier_liste_eleves(union, None)
    for eleve in eleves_filtre:
        sexe = eleve[const.qSexe]
        for cle,valeur in eleve.items():
            if(cle in const.spes_cles and valeur not in const.exclu_spe):
                if(sexe == "MASCULIN"):
                    resultat[valeur][0] += 1
                elif (sexe == "FEMININ"):
                    resultat[valeur][1] += 1
    data = [["Spe", "Garcons", "Filles", "%Filles"]]
    for spe, (garcons, filles) in resultat.items():
        total = garcons + filles
        pct_filles = round((filles / total) * 100, 2) if total else 0
        data.append([spe, garcons, filles, pct_filles])
    creer_pdf_tableau1("ratio_fg.pdf", "Ratio Filles/Garcons par Specialite", data)
    return resultat

def nb_eleve_triplette():
    """ Fonction qui permet voir le nombre des eleves par triplette fait.
        Les eleves qui quitte l'ecole ou ont eu l'avis de "Non" sont supprime de ce calcul.
    """
    resultat = {}
    eleves_filtre = h.purifier_liste_eleves(union, None)
    for eleve in eleves_filtre:
        spe_liste = trier_trois([eleve["spe1"],eleve["spe2"],eleve["spe3"]])
        if(spe_liste not in resultat):
            resultat[spe_liste] = 1
        else:
            resultat[spe_liste] += 1
    data = [["Triplette","Nombre d'Eleves"]]
    for combo,valeur in resultat.items():
        data.append([", ".join(combo), str(valeur)])
    creer_pdf_tableau1("nombre_par_triplettes.pdf", "Le nombre des eleves pour chaque triplette cree", data)
    


def part_voeux():
    """ Fonction qui affiche le pourcentage des eleves
        qui ont fait des voeux parmi l'ensemble des eleves de seconde.
        Absolument TOUS les eleves sont compris."""
    
    voeux_totales = len(union)
    path = "resultats_classe"
    onlyfiles = [f for f in listdir(join(getcwd(), path))]
    toutes_eleves_seconde = []
    for file in onlyfiles:
        classe = charge.lire_csv(f"{path}/{file}")
        for eleve in classe:
            toutes_eleves_seconde.append(eleve)
    #print(toutes_eleves_seconde)
    eleves_totales = len(toutes_eleves_seconde)
    pourcentage = round(((voeux_totales / eleves_totales) * 100),2)
    print(f"Le pourcentage des eleves qui ont fait des voeux pour le premier est: {pourcentage}%")
    return pourcentage

def part_premiere():
    """Fonction qui affiche et renvoie le pourcentage de voeux ayant recu
        un avis favorable ("Oui") du conseil de classe.
    """
    eleves_filtre = h.purifier_liste_eleves(union, None, opt_exclu_spe=False)
    pourcentage = round((len(eleves_filtre) / len(union) * 100),2)
    print(f"Le pourcentage de voeux ayant reçu un avis favorable du \
conseil de classe est: {pourcentage}%")
    return pourcentage
    
def trier_trois(liste_spe):
    """Un tri qui permet de trier les 3 spe en ordre croissante.
        Un vrai outil pour la prevention des dupliquees de triplettes de spes
    """
    for i in range(len(liste_spe)):
        for j in range(len(liste_spe) - 1 -i):
            if(liste_spe[j] > liste_spe[j+1]):
                liste_spe[j+1],liste_spe[j] = liste_spe[j], liste_spe[j+1]
    return tuple(liste_spe)





def trouver_eleve_par_nom(classe: list, eleve_nom: str)-> list:
    """Les eleves qu'on trouve dans brut.csv, on peut chercher leurs moyennes et notes.
        Dans ce contexte on utilise le nom d'eleve (eleve_nom) comme un cle candidate.
    """
    for eleve in classe:
        if(eleve_nom in eleve[const.qNom] or eleve[const.qNom] in eleve_nom):
            return eleve
    return None

def enregistrement_moyennes(f_eleve: dict, spe: str)-> dict:
    """La fonction rendre propre l'enregistrement de l'eleve, en le transformant dans un format: 
        eleve = [Nom,Classe,Moyenne Total,Moyenne_Matieres Spe, + Tous les matieres du spe.]
        On prend les voeux et on fait une recherche pour trouver les 
        enregistrements respectifs aux eleves pour bien mettre les matieres importants.
    """
    matieres_demandes = const.dico_spe[spe]
    eleve_resultat = [f_eleve[const.qNom], f_eleve[const.qClasse],  f_eleve[const.qMoyenne]]
    moyennes = []

    for cle,valeur in f_eleve.items():
        if(cle in matieres_demandes):
            try:
                moyenne_matiere = float(valeur.replace(",", "."))
                if(moyenne_matiere == -1.0):
                    continue
                moyennes.append(moyenne_matiere)
                
            except ValueError:
                pass
    if(len(moyennes) >= 2):
        eleve_resultat.append(round(sum(moyennes) / len(moyennes), 2))
    else:
        eleve_resultat.append("")
   
    for moyenne in moyennes:
        eleve_resultat.append(moyenne)
    #print(f"Result {eleve_resultat}")
    return eleve_resultat
   # bd = lire_csv("resultats_classe/")







union = charge.lire_csv("resultats_classe/brut.csv")