hggsp = "HGGSP"
hlp = "HLP"
eppcs = "EPPCS"
llcer = "LLCER"
ses = "SES"
svt = "SVT"
maths = "MATHS"
nsi = "NSI"
pc = "PHYSIQUE-CHIMIE"
arts = "ARTS-PLASTIQUES"
bio = "BIOLOGIE-ÉCOLOGIE"
thea = "THEATRE"
cirq = "ARTS DU CIRQUE"
engi = "SCIENCES-INGENIEUR"

qNom = "Nom"
qClasse = "Classe"
qMoyenne = "Moyenne"
qMoyenneMatieresSpe = "Moyenne Matieres Spe"
qMoyenneGlobale = "Moyenne Total"
qAvis = "Avis"
qSexe = "Sexe"

useless_domains_voeux = ["INE", "Classe", "Nom", "Prenom", "Sexe"]

spes_cles = ["spe1", "spe2", "spe3"]






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
}

dico_spe = {
    hggsp: ["FRANCAIS", "MATHS", "HG"],
    hlp: ["FRANCAIS", "MATHS", "HG"],
    eppcs: ["FRANCAIS", "MATHS", "SVT", "SES", "EPS"],
    llcer: ["FRANCAIS", "MATHS", "ANGLAIS"],
    ses: ["FRANCAIS", "MATHS", "SES"],
    svt: ["FRANCAIS", "MATHS", "SVT"],
    maths: ["FRANCAIS", "MATHS"],
    nsi: ["FRANCAIS", "MATHS"],
    pc: ["FRANCAIS", "MATHS", "PC"],
    arts: ["FRANCAIS"],
    bio: ["FRANCAIS"],
    engi: ["FRANCAIS"],
    thea: ["FRANCAIS"],
    cirq: ["FRANCAIS"]}

exclu_spe = [arts,bio,cirq,thea,engi]