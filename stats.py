import csv
# from creer_pdf import *
import ast
import copy
from os import listdir, getcwd
from os.path import isfile, join
from constants import *
fichier_travail = None

def lire_csv(filepath, delimiter= " ", encoding = "latin-1"):
    with open(filepath, newline='', encoding= encoding) as f:
        reader = csv.DictReader(f, delimiter=delimiter)
        return list(reader)

def csv_to_list_of_dicts(filepath, delimiter=' ', encoding='latin-1'):
    with open(filepath, newline='', encoding=encoding) as f:
        reader = csv.DictReader(f, delimiter=delimiter)
        return list(reader)
    
def list_of_dicts_to_csv(data, filepath, delimiter=' ', encoding='latin-1'):
    if not data:
        return
    with open(filepath, 'w', newline='', encoding=encoding) as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys(), delimiter=delimiter)
        writer.writeheader()
        writer.writerows(data)





def main():
    fichier_travail = None
    menu()

def eleve_par_spe():
    print("S'il vous plait selectionnez un matiere pour filtrer les eleves")
    print("options:")
    textOptions = ""
    numeroSpe = 0
    for alias,spe in optionsSpe.items():
        numeroSpe+=1
        if(numeroSpe == 1):
            textOptions += f"{alias}: {spe}"
        if(numeroSpe % 3 == 0):
            textOptions += f"\n{alias}: {spe}"
        else:
            textOptions += (" " * (30 - (len(spe) + (len(alias) + 3))) + f" {alias}: {spe}")
    print(textOptions)
    resultatSpe = demande(optionsSpe)

    ## EXECUTION DE LA FONCTION REELLE
    path = "resultats_classe"
    
    union = lire_csv("resultats_classe/brut.csv")
    
    
    eleves_filtre= []
    for eleve in union:
        excluded = False
        filtered_spe_found = False
        for cle,spe in eleve.items():
            if cle not in useless_domains_voeux:
                if(spe in exclu_spe):
                    excluded = True
                    break
                if(spe == optionsSpe[resultatSpe]):
                    filtered_spe_found = True
        if(excluded is False and filtered_spe_found):
            eleves_filtre.append(eleve)
        else:
            print(f"EXCLUDED: {eleve}")
    print(f"BEFORE EXCLUSION: {len(union)} \
        AFTER EXCLUSION: {len(eleves_filtre)}")
    fichiers_classes = []
    eleves_et_moyennes = []
    for eleve in eleves_filtre:
        classe = "20" + retrouve_classe(eleve["Classe"])
        fichier_eleve = []
        if(classe not in fichiers_classes):
            union = lire_csv(f"resultats_classe/{classe}.csv")
            fichier_eleve = union["Nom"] #! FINISH THIS
        for cle,spe in eleve.items():
            if cle not in useless_domains_voeux:

                
            
   # bd = lire_csv("resultats_classe/")

useless_domains = ["Nom", "Prenom", "Classe", "Moyenne"]
useless_domains_voeux = ["INE", "Classe", "Nom", "Prenom", "Sexe"]
exclu_spe = [arts,bio,cirq,thea,engi]
def demande(options):
    resultat = input("Reponse: ")
    if ( resultat in options):
        return resultat
    return demande(options)

def menu():
    print("Bonjour, bien venu sur la platforme de filtrage des eleves!")
    for key,option in optionsMenu.items():
        print(f"{key}: {option}")
    print("-" * 20)
    resultat = demande(optionsMenu.keys())
    
    optionsMenu[resultat][1]()

optionsMenu = {
"1" : ("Donner tous les eleves d'un spe specifie", eleve_par_spe ),
"2" : "Nothing yet"
}


optionsSpe = {
    "1" : hggsp,
    "2" : hlp,
    "3" : eppcs,
    "4" : llcer,
    "5" : ses,
    "6" : svt,
    "7" : maths,
    "8" : nsi,
    "9" : pc,
    "10" : arts,
    "11" : bio,
    "12" : thea,
    "13" : cirq,
}

dico_spe = {
    "HGGSP" : ["FRANCAIS", "MATHS", "HG"],
    "HLP" : ["FRANCAIS", "MATHS","HG"],
    "EPPCS" : ["FRANCAIS", "MATHS","SVT" , "SES", "EPS"],
    "LLCER" : ["FRANCAIS", "MATHS","ANGLAIS"],
    "SES" : ["FRANCAIS", "MATHS","SES"],
    "SVT" : ["FRANCAIS", "MATHS","SVT"],
    "MATHS" : ["FRANCAIS", "MATHS"],
    "NSI" : ["FRANCAIS", "MATHS"],
    "PHYSIQUE-CHIMIE" : ["FRANCAIS", "MATHS","PC"],
    "ARTS-PLASTIQUES" : ["FRANCAIS"],
    "BIOLOGIE-ÉCOLOGIE" : ["FRANCAIS"],
    "SCIENCES-INGENIEUR" : ["FRANCAIS"],
    "THÉÂTRE" : ["FRANCAIS"],
    "ARTS DU CIRQUE" : ["FRANCAIS"]}

def retrouve_classe(classe: str):
    if ("2NDE " in classe):
        return classe[5]
main()