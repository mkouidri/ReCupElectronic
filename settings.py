from tkinter import *
import customtkinter
import customtkinter as ctk
from PIL import Image, ImageTk
from choose_team import choose_team

# Définition des couleurs
bleu_fonce = '#7986cb'
blanc = '#FFFFFF'
gris_fonce = '#4a4a4a'

def settings(root):
    for widget in root.winfo_children():
        widget.destroy()

    change_team = customtkinter.CTkButton(
    root, 
    text="Changer d'équipe", 
    fg_color="transparent", 
    bg_color=bleu_fonce, 
    width=40, 
    height=40, 
    command=lambda: choose_team(root),
    )
    change_team.place(relx=0.05, rely=0.2)

    # map_image = Image.open("settings.png").resize((600, 300), Image.ANTIALIAS)
    # map_photo = ctk.CTkImage(light_image=map_image, size=(600, 300))
    # map_label = ctk.CTkLabel(map_frame, text="", image=map_photo)
    # map_label.place(relx=0.5, rely=0.5, anchor=CENTER)
