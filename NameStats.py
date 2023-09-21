from tkinter import simpledialog
import matplotlib.pyplot as plt
import tkinter as tk
import tkinter as ttk
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

jahre = list(range(1910, 2015))


def eingabe():
    username = name.get()
    state = staat.get()
    gender_ident = geschlecht.get()
    gender = "x"    
    yearMin = int(jahrMin.get())
    yearMax = int(jahrMax.get())
    yearRange = []
    count = 0

    xx = []
    xy = []

    with open("names.csv", "r") as file:  
        #ID, Name, Jahr, Geschlecht, Staat, Anzahl
        #Wandelt die Kürzel der csv Datei mit Hilfe von staaten_woerterbuch um
        if state in staaten_woerterbuch:
            Kuerzel = staaten_woerterbuch[state]
        
        #Bestimmt das Geschlecht
        if gender_ident == 1:
           gender = "F"
        else: 
           gender = "M"
         
        #Definiert die Jahre
        #Setzt das Jahr automatisch auf 2014 falls >= 2014
        if yearMax > 2014: 
            yearMax = 2014
            print("Das Jahr darf 2014 nicht ueberschreiten")
        
        #Setzt das Jahr automatisch auf 1910 falls <= 1910
        if yearMin < 1910:
            yearMin = 1910
            print("Das Jahr darf 1910 nicht unterschreiten")
        
        #erzeugt die Zeitspanne für den Graphen
        yearRange = list(range(yearMin, yearMax + 1))
         
        print("Name: " + username)
        print("Staat: " + state)
        print("Geschlecht: " + gender)
        print("Min Jahr: " + str(yearMin))
        print("Max Jahr: " + str(yearMax))
        print("Range: " + str(yearRange))
        
        for line in file:
            split = line.strip().split(",")   
            if split[1] == username and split[3] == gender and split[2] >= str(yearMin) and split[2] <= str(yearMax) and split[4] == Kuerzel:
                print("Gesamt: " + split[1] + " im Jahr " + split[2] + " " + split[5] + "000 Personen")
                xx.append(split[2])
                xy.append(split[5])
        print(xx)
        print(xy)

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

#Der Geschlecht Slider
geschlecht = tk.Scale(root, from_=0, to=1, orient="horizontal")
geschlecht.pack()

#Das minimale Jahr
jahrMinLabel = tk.Label(root, text="Min")
jahrMinLabel.pack()
jahrMin = ttk.Spinbox(root, values=jahre)
jahrMin.pack()

#Das minimale Jahr
jahrMaxLabel = tk.Label(root, text="Max")
jahrMaxLabel.pack()
jahrMax = ttk.Spinbox(root, values=jahre)
jahrMax.pack()

#Der Confirm Button. Er soll die Eingabe nur genehmigen, wenn alles weitere funktionert
button = tk.Button(root, text="Submit", command=eingabe)
button.pack()

root.mainloop()



