from tkinter import simpledialog
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import Text
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import *

from numpy import delete

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
        #Entfernt saemtliche Warnungen in der Textbox
        info_text.config(state=tk.NORMAL)
        info_text.delete(1.0, tk.END)
        #Wandelt die K�rzel der csv Datei mit Hilfe von staaten_woerterbuch um
        if state in staaten_woerterbuch:
            Kuerzel = staaten_woerterbuch[state]

        #Bestimmt das Geschlecht
        if gender_ident == 1:
           gender = "F"
        else: 
           gender = "M"
         
        #Definiert die Jahre
        #Wenn das max Jahr > min Jahr oder andersrum, gibt es eine Fehlermeldung
        if yearMin >= yearMax:
            yearMin == yearMax - 1
            info_text.insert(tk.END, "The min year must not exceed the max year!")
        elif yearMax <= yearMin:
            yearMax = yearMin + 1
            info_text.insert(tk.END, "The max year must not go below the min year!")
            
        #Setzt das Jahr automatisch auf 2014 falls >= 2014  
        if yearMax > 2014: 
            yearMax = 2014
            info_text.insert(tk.END, "The year must not exceed 2014. It is automatically set to 2014.")
        
        #Setzt das Jahr automatisch auf 1910 falls <= 1910
        if yearMin < 1910:
            yearMin = 1910
            info_text.insert(tk.END,"The year must not go below 1910. It is automatically set to 1910.")
         
        
        
        #erzeugt die Zeitspanne f�r den Graphen
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
                info_text.insert(tk.END,"Year: " + split[2] + ", count: " + split[5] + "\n")
                xx.append(int(split[2]))
                xy.append(int(split[5]))
                maxCount = max(xy)
                minCount= min(xy)
        info_text.insert(tk.END,"Most people: " + str(maxCount) + "\n" + "Least people: " + str(minCount))
        print(xy)
        
        #Erstellt den Graphen nachdem der Knopf ged�rckt wurde
        graph_breite=4
        graph_hoehe=2
        fig, ax = plt.subplots(figsize=(graph_breite, graph_hoehe))
        ax.plot(xx, xy, linestyle='-')
        ax.set_xlabel('Year')
        ax.set_ylabel('Count')
        canvas = FigureCanvasTkAgg(fig, master=root)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.grid(row=8, column=2, rowspan=4)
             
        #Deaktiviert die Funktion in die Textbox schreiben zu k�nnen
        info_text.config(state=tk.DISABLED)
        


#Das allgemeine Layout
root = tk.Tk()
root.title("NameStats")
root.geometry("750x600")

#Die Textbox. tk.DISABLED sorgt daf�r, dass der Benutzer nicht in die Textbox schreiben kann
info_text = Text(root, height=5, width=40, wrap=tk.WORD)
info_text.grid(row=7, column=2, padx=10, pady=10)
info_text.config(state=tk.NORMAL)

#Die Widgets
label = tk.Label(root, text="NameStats", font=("Arial", 18))
name_label = tk.Label(root, text="Name: ")
name = tk.Entry(root)
staat = tk.StringVar(root)
staat.set(staaten_liste[0])
state_label = tk.Label(root, text="State: ")
dropdown = tk.OptionMenu(root, staat, *staaten_liste)
gender_label = tk.Label(root, text="Gender: ")
gender_label_F = tk.Label(root, text="F")
gender_label_M = tk.Label(root, text="M")
geschlecht = tk.Scale(root, from_=0, to=1, orient="horizontal", showvalue=0)
jahrMinLabel = tk.Label(root, text="Year Min: ")
jahrMin = tk.Spinbox(root, values=jahre, width=5)
jahrMaxLabel = tk.Label(root, text="Year Max: ")
jahrMax = tk.Spinbox(root, values=jahre, width=5)
button = tk.Button(root, text="Submit", command=eingabe)

#Die �berschrift
label.grid(row=0, column=2, padx=10, pady=10) 

#Das Namensfeld
name_label.grid(row=1, column=0)
name.grid(row=1, column=2, pady=10)
name.focus()

#Das States dropdown Men�
state_label.grid(row=2, column=0, pady=10)
dropdown.grid(row=2, column=2)

#Das Geschlecht
gender_label.grid(row=3, column=0)
gender_label_M.grid(row=3, column=1, ipadx=1)
geschlecht.grid(row=3, column=2, pady=10, padx=160)
gender_label_F.grid(row=3, column=3, ipadx=1)

#Die Auswahl der Jahre
jahrMinLabel.grid(row=5, column=0, padx=0, pady=10, ipadx="50")
jahrMin.grid(row=5, column=1)

jahrMax.grid(row=5, column=3)
jahrMaxLabel.grid(row=5, column=2)

#Der Submit Button
button.grid(row=6, column=2, pady=20)

# Starten der Tkinter-Hauptschleife
root.mainloop()



