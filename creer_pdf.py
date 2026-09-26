import os


def creer_pdf_tableau1(nom_fichier, titre, data):
    from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
    from reportlab.lib import colors
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.styles import getSampleStyleSheet
    from reportlab.lib.enums import TA_CENTER

    #? Dossier de sortie, fonction modifie
    dossier_exports = "exports"
    os.makedirs(dossier_exports, exist_ok=True)
    chemin_complet = os.path.join(dossier_exports, nom_fichier)
    
    # Création du document
    doc = SimpleDocTemplate(chemin_complet, pagesize=A4)
    #? -------- Fin modification ---------
    elements = []

    # Styles
    styles = getSampleStyleSheet()
    style_titre = styles["Heading1"]
    style_titre.alignment = TA_CENTER

    # Ajout du titre
    elements.append(Paragraph(titre, style_titre))
    elements.append(Spacer(1, 20))

    # Création du tableau
    table = Table(data)

    # Style du tableau
    table.setStyle(TableStyle([
        ("GRID", (0, 0), (-1, -1), 1, colors.black),
        ("BACKGROUND", (0, 0), (-1, 0), colors.grey),  # header
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
    ]))

    # Centrage du tableau
    table.hAlign = "CENTER"

    elements.append(table)

    # Construction du PDF
    doc.build(elements)





creer_pdf_tableau1("nom_fichier.pdf", "titre", [["a", "b", "c"],[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15],[16,17,18],[19,20,21],[22,23,24],[25,26,27],[28,29,30]])
