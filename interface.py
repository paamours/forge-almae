import customtkinter as ctk
import csv
# Création d'une fenêtre customtkinter simple
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

app = ctk.CTk()
app.title("Fenêtre CustomTkinter")
app.geometry("400x250")

label = ctk.CTkLabel(app, text="Bienvenue dans la forge !", font=("Papyrus", 18, "bold"))
label.pack(pady=10)

def charger_equipements():
    equipements = []
    with open("BDD.csv", encoding="latin-1") as f:
        reader = csv.DictReader(f, delimiter=';')
        for row in reader:
            equipements.append(row)
    return equipements

liste_equipements = charger_equipements()
nom_equipements = [e['Nom'] for e in liste_equipements]

# Ajout d'une variable de type armurerie unique
armureries = sorted(set(e['Type Armuerie'] for e in liste_equipements))

# Callback pour filtrer les équipements selon le type sélectionné
def filtrer_equipements(event):
    type_selectionne = combo_type.get()
    equipements_filtres = [e for e in liste_equipements if e['Type Armuerie'] == type_selectionne]
    # Nettoyer le tableau précédent
    for widget in frame_tableau.winfo_children():
        widget.destroy()
    if equipements_filtres:
        colonnes = list(equipements_filtres[0].keys())
        # En-têtes
        for j, col in enumerate(colonnes):
            header = ctk.CTkLabel(frame_tableau, text=col, font=("Papyrus", 12, "bold"), text_color="#FFD700", bg_color="#232323")
            header.grid(row=0, column=j, padx=2, pady=2)
        # Lignes d'équipements
        for i, equip in enumerate(equipements_filtres, start=1):
            for j, col in enumerate(colonnes):
                val = equip[col]
                cell = ctk.CTkLabel(frame_tableau, text=val, font=("Papyrus", 11), text_color="#FFF8DC", bg_color="#232323")
                cell.grid(row=i, column=j, padx=2, pady=2)

# Menu déroulant pour le type d'armurerie
combo_type = ctk.CTkComboBox(app, values=armureries, font=("Papyrus", 14),command=filtrer_equipements)
combo_type.pack(pady=5)
combo_type.set(armureries[0])

# Tableau pour afficher les équipements filtrés
frame_tableau = ctk.CTkFrame(app, fg_color="#232323")
frame_tableau.pack(pady=10, fill="both", expand=True)



app.mainloop()
