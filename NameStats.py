from tkinter import simpledialog
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import *

staaten_liste = ["Alabama", "Alaska", "Arizona", "Arkansas", "California",
    "Colorado", "Connecticut", "Delaware", "Florida", "Georgia",
    "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa",
    "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland",
    "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri",
    "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey",
    "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio",
    "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina",
    "South Dakota", "Tennessee", "Texas", "Utah", "Vermont",
    "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"]

staaten_woerterbuch = {
    "Alabama": "AL",
    "Alaska": "AK",
    "Arizona": "AZ",
    "Arkansas": "AR",
    "California": "CA",
    "Colorado": "CO",
    "Connecticut": "CT",
    "Delaware": "DE",
    "Florida": "FL",
    "Georgia": "GA",
    "Hawaii": "HI",
    "Idaho": "ID",
    "Illinois": "IL",
    "Indiana": "IN",
    "Iowa": "IA",
    "Kansas": "KS",
    "Kentucky": "KY",
    "Louisiana": "LA",
    "Maine": "ME",
    "Maryland": "MD",
    "Massachusetts": "MA",
    "Michigan": "MI",
    "Minnesota": "MN",
    "Mississippi": "MS",
    "Missouri": "MO",
    "Montana": "MT",
    "Nebraska": "NE",
    "Nevada": "NV",
    "New Hampshire": "NH",
    "New Jersey": "NJ",
    "New Mexico": "NM",
    "New York": "NY",
    "North Carolina": "NC",
    "North Dakota": "ND",
    "Ohio": "OH",
    "Oklahoma": "OK",
    "Oregon": "OR",
    "Pennsylvania": "PA",
    "Rhode Island": "RI",
    "South Carolina": "SC",
    "South Dakota": "SD",
    "Tennessee": "TN",
    "Texas": "TX",
    "Utah": "UT",
    "Vermont": "VT",
    "Virginia": "VA",
    "Washington": "WA",
    "West Virginia": "WV",
    "Wisconsin": "WI",
    "Wyoming": "WY"
}




def eingabe():
    username = name.get()
    state = staat.get()
    #gender = gender.get()
    #Year = year.get() 
    anzahl = 0

    xx = []
    xy = []
    


    with open("names.csv", "r") as file:  
        #Wandelt die Kürzel der csv Datei mit Hilfe von staaten_woerterbuch um
        if state in staaten_woerterbuch:
            Kuerzel = staaten_woerterbuch[state]
        else:
            print(state)   
        
        for line in file:
            split = line.strip().split(",")
            

            #Die Koordinaten werden erstellt
            if split[1] == username and split[4] == Kuerzel:
             #xx.append(split[2])
             #xy.append(split[5])
    
             anzahl += 1
    print(anzahl)
                

#Das GUI 
root = tk.Tk()
root.geometry("800x500")
root.title("NameStats")

#Die Überschrift
label = tk.Label(root, text="NameStats", font=('Arial', 18))
label.pack(padx=20, pady=20)

#Das Textfeld für den Namen
name = tk.Entry(root)
name.pack()
name.focus()

#Das "States" Dropdown Menü. staat bestimmt die Standardoption
staat = tk.StringVar(root)
staat.set(staaten_liste[0])

dropdown = tk.OptionMenu(root, staat, *staaten_liste)
dropdown.pack()


#Der Confirm Button. Er soll die Eingabe nur genehmigen, wenn alles weitere funktionert
button = tk.Button(root, text="Submit", command=eingabe)
button.pack()

root.mainloop()



