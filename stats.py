import csv
# from creer_pdf import *
import ast
import copy
from os import listdir, getcwd
from os.path import isfile, join
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
    onlyfiles = [f for f in listdir(f"{getcwd()}\\{path}\\")]
    union = []
    for file in onlyfiles:
        f = lire_csv(f"{path}/{file}")
        union.append(f)
    print(union)
   # bd = lire_csv("resultats_classe/")

    
        
def demande(options):
    resultat = None
    while resultat is None:
        resultat = input("Reponse: ")
        if ( resultat in options):
            return resultat
        else:
            resultat = None

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
    "1" : "HGGSP",
    "2" : "HLP",
    "3" : "EPPCS",
    "4" : "LLCER",
    "5" : "SES",
    "6" : "SVT",
    "7" : "MATHS",
    "8" : "NSI",
    "9" : "PHYSIQUE-CHIMIE",
    "10" : "ARTS-PLASTIQUES",
    "11" : "BIOLOGIE-ÉCOLOGIE",
    "12" : "THÉÂTRE",
    "13" : "ARTS DU CIRQUE",

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
main()