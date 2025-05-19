from tkinter import *
import customtkinter
import customtkinter as ctk
from PIL import Image

customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("green")

root = customtkinter.CTk()

#Couleurs
bleu_clair = '#B4BEDF'
bleu_fonce = '#818EC2'
vert_clair = '#7ED957'
blanc = '#FFFFFF'
orange = '#ffb648'
vert = '#a4ffc2'
rouge = '#ff3939'

#Configuration de la page
# root.title("Re'cup App")
root.geometry('720x480')
root.overrideredirect(True)

root.configure(fg_color=bleu_clair)

def topBar(root, gps_state, sim_state, server_state):
    #----------------------------- Barre du haut --------------------------------
    
    # Frame bleu foncé en haut
    frame = customtkinter.CTkFrame(master=root, width=720, height=50, fg_color=bleu_fonce)
    frame.place(x=0, y=0)

    # SETTING
    settings_icon = customtkinter.CTkImage(Image.open("settings.png"), size=(40, 40))
    
    settings_button = customtkinter.CTkButton(
    root, 
    text="", 
    image=settings_icon, 
    fg_color="transparent", 
    bg_color=bleu_fonce, 
    width=40, 
    height=40, 
    command=lambda:settings(root)
    )
    settings_button.place(relx=0.02, rely=0.005)


    if gps_state == "ok":
        gps_icon = customtkinter.CTkImage(Image.open("icons/ok_gps_icon.png"), size=(40, 40))
        gps_state_icon = customtkinter.CTkLabel(root, text="", image=gps_icon, bg_color=bleu_fonce)
    elif gps_state == "waiting":
        gps_icon = customtkinter.CTkImage(Image.open("icons/wait_gps_icon.png"), size=(40, 40))
        gps_state_icon = customtkinter.CTkLabel(root, text="", image=gps_icon)
    else :
        gps_icon = customtkinter.CTkImage(Image.open("icons/bad_gps_icon.png"), size=(40, 40))
        gps_state_icon = customtkinter.CTkLabel(root, text="", image=gps_icon)
    gps_state_icon.place(relx=0.80, rely=0.01)

    if server_state == "ok":
        server_icon = customtkinter.CTkImage(Image.open("icons/ok_server_icon.png"), size=(40, 40))
        server_state_icon = customtkinter.CTkLabel(root, text="", image=server_icon, bg_color=bleu_fonce)
    elif server_state == "waiting":
        server_icon = customtkinter.CTkImage(Image.open("icons/wait_server_icon.png"), size=(40, 40))
        server_state_icon = customtkinter.CTkLabel(root, text="", image=server_icon)
    else :
        server_icon = customtkinter.CTkImage(Image.open("icons/bad_server_icon.png"), size=(40, 40))
        server_state_icon = customtkinter.CTkLabel(root, text="", image=server_icon)
    server_state_icon.place(relx=0.86, rely=0.01)

    if sim_state == "ok":
        sim_icon = customtkinter.CTkImage(Image.open("icons/ok_sim_icon.png"), size=(40, 40))
        sim_state_icon = customtkinter.CTkLabel(root, text="", image=sim_icon, bg_color=bleu_fonce)
    elif sim_state == "waiting":
        sim_icon = customtkinter.CTkImage(Image.open("icons/wait_sim_icon.png"), size=(40, 40))
        sim_state_icon = customtkinter.CTkLabel(root, text="", image=sim_icon)
    else :
        sim_icon = customtkinter.CTkImage(Image.open("icons/bad_sim_icon.png"), size=(40, 40))
        sim_state_icon = customtkinter.CTkLabel(root, text="", image=sim_icon)
    sim_state_icon.place(relx=0.92, rely=0.01)

    #-----------------------------------------------------------------------------

def settings(root):
    for widget in root.winfo_children():
        widget.destroy()

    change_team = customtkinter.CTkButton(
    root, 
    text="Changer d'équipe", 
    fg_color="transparent", 
    bg_color=bleu_fonce, 
    width=300, 
    height=80, 
    command=lambda: choose_team(root),
    font=("Helvetica", 30),
    )
    change_team.place(relx=0.05, rely=0.2)

    quit_app = customtkinter.CTkButton(
    root, 
    text="Quitter l'application", 
    fg_color="transparent", 
    bg_color=rouge, 
    width=300, 
    height=80, 
    command=lambda: root.destroy(),
    font=("Helvetica", 30),
    )
    quit_app.place(relx=0.05, rely=0.5)

    # map_image = Image.open("settings.png").resize((600, 300), Image.ANTIALIAS)
    # map_photo = ctk.CTkImage(light_image=map_image, size=(600, 300))
    # map_label = ctk.CTkLabel(map_frame, text="", image=map_photo)
    # map_label.place(relx=0.5, rely=0.5, anchor=CENTER)

def verifpage(root, gps_state, speed_state, sim_state, server_state):
    for widget in root.winfo_children():
        widget.destroy()

    topBar(root, "ok", "ok", "ok")

    # Bouton "Continuer"
    continue_button = customtkinter.CTkButton(
        root,
        text="Continuer",
        font=("Helvetica", 30),
        command=lambda: choose_team(root),
        fg_color=vert_clair,
        width=250,
        height=75,
    )
    continue_button.place(relx=0.5, rely=0.85, anchor=CENTER)

    # Chargement des icônes
    gps_icon = customtkinter.CTkImage(Image.open("gps_logo.png"), size=(60, 75))
    speed_icon = customtkinter.CTkImage(Image.open("gps_logo.png"), size=(60, 75))
    sim_icon = customtkinter.CTkImage(Image.open("gps_logo.png"), size=(60, 75))
    server_icon = customtkinter.CTkImage(Image.open("gps_logo.png"), size=(60, 75))


    # Texte principal
    title_label = customtkinter.CTkLabel(
        root,
        text="Vérification des capteurs :",
        font=("Helvetica", 29),
        bg_color=bleu_clair,
    )
    title_label.place(relx=0.5, rely=0.2, anchor=CENTER)

    # Placement des icônes et statuts
    # GPS
    gps_label = customtkinter.CTkLabel(root, text="GPS", font=("Helvetica", 23), image=gps_icon, compound="top")
    gps_label.place(relx=0.2, rely=0.35, anchor=CENTER)
    if gps_state == "ok":
        gps_status = customtkinter.CTkLabel(root, text="✔", font=("Helvetica", 50), text_color=vert_clair, bg_color=bleu_clair)
    elif gps_state == "waiting":
        gps_status = customtkinter.CTkLabel(root, text="...", font=("Helvetica", 50), text_color=orange, bg_color=bleu_clair)
    else :
        gps_status = customtkinter.CTkLabel(root, text="✖", font=("Helvetica", 50), text_color=rouge, bg_color=bleu_clair)
    gps_status.place(relx=0.2, rely=0.65, anchor=CENTER)

    # Vitesse
    speed_label = customtkinter.CTkLabel(root, text="Vitesse", font=("Helvetica", 23), image=speed_icon, compound="top")
    speed_label.place(relx=0.4, rely=0.35, anchor=CENTER)
    if speed_state == "ok":
        speed_status = customtkinter.CTkLabel(root, text="✔", font=("Helvetica", 50), text_color=vert_clair, bg_color=bleu_clair)
    elif speed_state == "waiting":
        speed_status = customtkinter.CTkLabel(root, text="...", font=("Helvetica", 50), text_color=orange, bg_color=bleu_clair)
    else :
        speed_status = customtkinter.CTkLabel(root, text="✖", font=("Helvetica", 50), text_color=rouge, bg_color=bleu_clair)
    speed_status.place(relx=0.4, rely=0.65, anchor=CENTER)

    # SIM
    sim_label = customtkinter.CTkLabel(root, text="SIM", font=("Helvetica", 23), image=sim_icon, compound="top")
    sim_label.place(relx=0.6, rely=0.35, anchor=CENTER)
    if sim_state == "ok":
        sim_status = customtkinter.CTkLabel(root, text="✔", font=("Helvetica", 50), text_color=vert_clair, bg_color=bleu_clair)
    elif sim_state == "waiting":
        sim_status = customtkinter.CTkLabel(root, text="...", font=("Helvetica", 50), text_color=orange, bg_color=bleu_clair)
    else :
        sim_status = customtkinter.CTkLabel(root, text="✖", font=("Helvetica", 50), text_color=rouge, bg_color=bleu_clair)
    sim_status.place(relx=0.6, rely=0.65, anchor=CENTER)

    # Serveur
    server_label = customtkinter.CTkLabel(root, text="Serveur", font=("Helvetica", 23), image=server_icon, compound="top")
    server_label.place(relx=0.8, rely=0.35, anchor=CENTER)
    if server_state == "ok":
        server_status = customtkinter.CTkLabel(root, text="✔", font=("Helvetica", 50), text_color=vert_clair, bg_color=bleu_clair)
    elif sim_state == "waiting":
        server_status = customtkinter.CTkLabel(root, text="...", font=("Helvetica", 50), text_color=orange, bg_color=bleu_clair)
    else :
        server_status = customtkinter.CTkLabel(root, text="✖", font=("Helvetica", 50), text_color=rouge, bg_color=bleu_clair)
    server_status.place(relx=0.8, rely=0.65, anchor=CENTER)

def choose_team(root):
    for widget in root.winfo_children():
        widget.destroy()

    topBar(root,"ok", "ok", "ok")

    # Titre principal
    title_label = customtkinter.CTkLabel(
        root,
        text="Choix de l'équipe :",
        font=("Helvetica", 24),
        text_color=blanc
    )
    title_label.place(relx=0.5, rely=0.2, anchor=CENTER)

    # Menu déroulant pour le choix de l'équipe
    team_var = StringVar(value="LegoGo")  # Valeur par défaut
    team_menu = customtkinter.CTkOptionMenu(
        root,
        variable=team_var,
        values=["LegoGo", "ESIEAbot", "Eausecours", "4","5","6","7","8"],
        font=("Helvetica", 20),
        width=300,
        height=50,
        fg_color=blanc,
        button_color=bleu_fonce,
        dropdown_fg_color=blanc,
        dropdown_text_color="black",
        dropdown_font=("Helvetica", 26),  # Taille du texte dans le menu déroulant
        text_color="black"
    )
    team_menu.place(relx=0.5, rely=0.4, anchor=CENTER)

    # Bouton "Valider"
    validate_button = customtkinter.CTkButton(
        root,
        text="Valider",
        font=("Helvetica", 30),
        command= lambda : inrace(root, team_var.get()),#root.destroy,#verifpage(root, "ok","ok","ok","ok" ),#print(f"Équipe sélectionnée : {team_var.get()}"),
        fg_color=vert_clair,
        width=250,
        height=75,
    )
    validate_button.place(relx=0.5, rely=0.7, anchor=CENTER)

def inrace(root, nameTeam):
    for widget in root.winfo_children():
        widget.destroy()

    topBar(root, "ok", "ok", "ok")

    # Nom de l'équipe
    team_name_label = ctk.CTkLabel(
        root,
        text="Equipe : " + nameTeam,
        font=("Helvetica", 32),
        text_color=blanc
    )
    team_name_label.place(relx=0.5, rely=0.2, anchor=CENTER)

    # Conteneur de vitesse
    speed_frame = ctk.CTkFrame(root, fg_color=bleu_fonce, corner_radius=100, width=200, height=200)
    speed_frame.place(relx=0.05, rely=0.35)

    speed_label = ctk.CTkLabel(
        speed_frame,
        text="13",
        font=("Helvetica", 60),
        text_color=blanc
    )
    speed_label.place(relx=0.5, rely=0.4, anchor=CENTER)

    unit_label = ctk.CTkLabel(
        speed_frame,
        text="km/h",
        font=("Helvetica", 30),
        text_color=blanc
    )
    unit_label.place(relx=0.5, rely=0.7, anchor=CENTER)

    # Conteneur de la carte
    map_frame = ctk.CTkFrame(root, fg_color=blanc, corner_radius=15, width=350, height=220)
    map_frame.place(relx=0.7, rely=0.55, anchor=CENTER)

    # map_image = Image.open("settings.png").resize((600, 300), Image.ANTIALIAS)
    # map_photo = ctk.CTkImage(light_image=map_image, size=(600, 300))
    # map_label = ctk.CTkLabel(map_frame, text="", image=map_photo)
    # map_label.place(relx=0.5, rely=0.5, anchor=CENTER)

verifpage(root, "ok", "ok", "ok", "ok")

root.mainloop()