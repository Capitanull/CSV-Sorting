
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
    eleves_filtre= []
    for classe in union:
        for eleve in classe:
            for cle,valeur in eleve.items():
                if cle not in useless_domains:
                    if(cle in exclu_spe):
                        print(eleve)
                        break
                    else:
                        eleves_filtre.append(eleve)
                        break
    
    print(eleves_filtre)
   # bd = lire_csv("resultats_classe/")

useless_domains = ["Nom", "Prenom", "Classe", "Moyenne"]
exclu_spe = ["ARTS-PLASTIQUES"]
def demande(options):
    resultat = input("Reponse: ")
    if ( resultat in options):
        return resultat
    return demande(options)
