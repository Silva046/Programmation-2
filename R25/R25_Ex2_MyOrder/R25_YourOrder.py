import customtkinter as ctk
import tkinter as tk
from tkinter import ttk

import os
from PIL import ImageTk, Image   


window = tk.Tk()
ta_commande = "Ta commande: \n"
choix_smarin =  tk.StringVar(value="steak")
size_smarin =  tk.StringVar(value="10")
choix_pizza =  tk.StringVar(value="nature")
size_pizza =  tk.StringVar(value="7")

prix_total = 0

#  VOIR ÉNONCÉ
def ajouter_smarin():
    global prix_total
    global ta_commande
    prix = 0
    if chk_smarin._check_state == True:
        if choix_smarin.get() == "steak" or choix_smarin.get() == "pepperoni" and size_smarin.get() == "10":
            prix_total += 14.99
            prix = 14.99
        elif choix_smarin.get() == "duchef" and size_smarin.get() == "10":
            prix_total += 15.99
            prix = 15.99
        elif choix_smarin.get() == "steak" or choix_smarin.get() == "pepperoni" and size_smarin.get() == "14":
            prix_total += 16.99
            prix = 16.99
        elif choix_smarin.get() == "duchef" and size_smarin.get() == "14":
            prix_total += 17.99
            prix = 17.99
        ta_commande += f"\nUn sous-marin {choix_smarin.get()} {size_smarin.get()}po: {prix}\n"
        #displayBox.insert("0.0", f"{ta_commande}\nUn sous-marin {choix_smarin.get()} {size_smarin.get()}po: {prix}\n    Pour un total de: ???")

#  VOIR ÉNONCÉ               
def ajouter_pizza():
    prix = 0
    global ta_commande
    global prix_total
    if chk_pizza._check_state == True:
        if choix_pizza.get() == "nature" or choix_pizza.get() == "végétarienne" and size_pizza.get() == "7":
            prix_total += 14.99
            prix = 14.99
        elif choix_pizza.get() == "toute garnie" and size_pizza.get() == "7":
            prix_total += 16.99
            prix = 16.99
        elif choix_pizza.get() == "nature" or choix_pizza.get() == "végétarienne" and size_pizza.get() == "14":
            prix_total += 16.99
            prix = 16.99
        elif choix_pizza.get() == "toute garnie" and size_pizza.get() == "14":
            prix_total += 18.99
            prix = 18.99
        ta_commande += f"\nUne pizza {choix_pizza.get()} {size_pizza.get()}po: {prix}"

#  VOIR ÉNONCÉ               
def ajouter():
    ajouter_smarin()
    ajouter_pizza()
    global ta_commande
    global prix_total

    displayBox.delete("0.0","end")
    ta_commande += f"\ntotal de {prix_total}$"
    displayBox.insert("0.0",ta_commande)
    
    

    
window.rowconfigure((0,1,2,3), weight=1, minsize=150)
window.columnconfigure((0,1), weight=1, minsize=75)

image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "images")
logo_image = ImageTk.PhotoImage(Image.open(os.path.join(image_path, "Logo.jpg")), size=(26, 26))
smarin_image = ImageTk.PhotoImage(Image.open(os.path.join(image_path, "sousmarin.jpg")), size=(16, 16))
pizza_image = ImageTk.PhotoImage(Image.open(os.path.join(image_path, "pizza.jpg")), size=(16, 16))

lbl_logo  = tk.Label(master=window, image=logo_image)
lbl_logo.grid(row=0,column=0,columnspan=2)

########  FRAME SOUS-MARIN
frm_sousmarin = tk.Frame(master=window,
                        relief=tk.RAISED,
                        borderwidth=1 )
frm_sousmarin.grid(row=1, column=0, padx=5, pady=0)

frm_order_smarin = tk.Frame(master=frm_sousmarin,
                            relief=tk.RAISED,
                            borderwidth=1 )
frm_order_smarin.grid(row=1, column=0, padx=5, pady=5)

chk_smarin = ctk.CTkCheckBox(master=frm_order_smarin,
                             text='Oui! Un sous-marin!', 
                             onvalue='1', offvalue='0')
chk_smarin.grid(row=0, column=0)

lbl_img_smarin  = tk.Label(master=frm_order_smarin, image=smarin_image, width="220", height="120")
lbl_img_smarin.grid(row=1, column=0 )

frm_smarin_choix = tk.Frame(master=window,
                            relief=tk.RAISED,
                            borderwidth=1 )
frm_smarin_choix.grid(row=1, column=1, padx=5, pady=5)


# Choix sous-marin
lbl_choixsmarin = ctk.CTkLabel(frm_smarin_choix, text="Choix")
lbl_choixsmarin.grid(row=0, column=0,sticky="w")

smarin_steak = ttk.Radiobutton(frm_smarin_choix, text='Steak', variable=choix_smarin, value='steak')
smarin_pepperoni = ttk.Radiobutton(frm_smarin_choix, text='Pepperoni', variable=choix_smarin, value='pepperoni')
smarin_duchef = ttk.Radiobutton(frm_smarin_choix, text='Du Chef', variable=choix_smarin, value='duchef')
smarin_steak.grid(row=1, column=0,padx=2,pady=2,sticky="w")
smarin_pepperoni.grid(row=2, column=0,padx=2,pady=2,sticky="w")
smarin_duchef.grid(row=3, column=0,padx=2,pady=2,sticky="w")
# Choix sous-marin grandeur
lbl_choixsmarin_size = ctk.CTkLabel(frm_smarin_choix,
                                    text="Grandeur")
lbl_choixsmarin_size.grid(row=4, column=0,sticky="w")

smarin10po = ttk.Radiobutton(frm_smarin_choix, text='10"', variable=size_smarin, value='10')
smarin14po = ttk.Radiobutton(frm_smarin_choix, text='14"', variable=size_smarin, value='14')
smarin10po.grid(row=5, column=0,padx=2,pady=2,sticky="w")
smarin14po.grid(row=6, column=0,padx=2,sticky="w")

btn_voir_ajout_smarin = ttk.Button(frm_sousmarin, text="Ajouter", command=ajouter)
btn_voir_ajout_smarin.grid(column=2, row=3, sticky='w') 


###########   FRAME PIZZA
frm_pizza = tk.Frame(   master=window,
                        relief=tk.RAISED,
                        borderwidth=1 )
frm_pizza.grid(row=2, column=0, padx=5, pady=0)

frm_order_pizza = tk.Frame( master=frm_pizza,
                            relief=tk.RAISED,
                            borderwidth=1 )
frm_order_pizza.grid(row=1, column=0, padx=5, pady=5)


chk_pizza = ctk.CTkCheckBox(master=frm_order_pizza, 
                            text='Oui! Une pizza!', 
                            onvalue='1', offvalue='0')
chk_pizza.grid(row=0, column=0)

lbl_img_pizza  = tk.Label(master=frm_order_pizza, image=pizza_image, width="220", height="120")
lbl_img_pizza.grid(row=1, column=0 )

frm_pizza_choix = tk.Frame( master=window,
                            relief=tk.RAISED,
                            borderwidth=1 )
frm_pizza_choix.grid(row=2, column=1, padx=5, pady=5)

# Choix pizza
lbl_choixpizza = ctk.CTkLabel(frm_pizza_choix, text="Choix")
lbl_choixpizza.grid(row=0, column=0,sticky="w")

pizza_nature = ttk.Radiobutton(frm_pizza_choix, text='Nature', variable=choix_pizza, value='nature')
pizza_vege = ttk.Radiobutton(frm_pizza_choix, text='Végétarienne', variable=choix_pizza, value='végétarienne')
pizza_garnie = ttk.Radiobutton(frm_pizza_choix, text='Toute garnie', variable=choix_pizza, value='toute garnie')
pizza_nature.grid(row=1, column=0,padx=2,pady=2,sticky="w")
pizza_vege.grid(row=2, column=0,padx=2,pady=2,sticky="w")
pizza_garnie.grid(row=3, column=0,padx=2,pady=2,sticky="w")

# Choix grandeur pizza
lbl_choixpizza_size = ctk.CTkLabel(frm_pizza_choix, text="Grandeur")
lbl_choixpizza_size.grid(row=4, column=0,sticky="w")

pizza7po = ttk.Radiobutton(frm_pizza_choix, text='7"', variable=size_pizza, value='7')
pizza14po = ttk.Radiobutton(frm_pizza_choix, text='14"', variable=size_pizza, value='14')
pizza7po.grid(row=5, column=0,padx=2,pady=2,sticky="w")
pizza14po.grid(row=6, column=0,padx=2,sticky="w")

btn_voir_ajout_pizza = ttk.Button(frm_pizza, text="Ajouter", command=ajouter)
btn_voir_ajout_pizza.grid(column=2, row=3, sticky='w') 


##   FRAME VOIR LA COMMANDE
frm_voirCommande = tk.Frame(master=window,
                            relief=tk.RAISED,
                            borderwidth=1 )
frm_voirCommande.grid(row=3, column=0, columnspan=2, padx=5, pady=5)


# Text Box
displayBox = ctk.CTkTextbox(master=frm_voirCommande, width=400, height=200, border_width=2)
displayBox.grid(row=1, column=0, sticky="nsew", pady=0)


window.mainloop()