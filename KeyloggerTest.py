
###########################
# Dieser Code wurde von   #
# Glenn Konan Mac carthy  #
# Geschrieben und zur     #
# verfuegung gestellt.    #
###########################





import random
from tkinter import *
from tkinter import font
import pyperclip

 #  Tkinter defeniereung


def new_func():
    root = Tk()
    return root

 #  Titel und fenster ----------------------------------------------------------------

root = new_func()
root.title('Passwort Generator 3000 nach BSI') #  Titel
root.geometry('575x250') #  Groesse des Fensters

 #  Variabeln fuer die Passwort generierung

abc = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
nummern = '0123456789'
symbole = '!@#$%^&*_-+=[]()'

chars = abc + nummern + symbole
sp = "  "
sp1 = "  |  "
sp2 = "\n"

 #  Text ueber den entry boxen

label_chars = Label(root, text= "Bitte tragen sie ihre wunsch-laenge des passwortes in das erste Feld ein", font=('Calibri', 12)).pack(padx=10)
#label_mid = Label(root, text= "Die BSI Empfohlene Passwort laenge betraegt 36", font=('Calibri', 12)).pack(padx=10))
usage_chars = Label(root, text= "Bitte tragen sie den zweck oder eine Notiz fuer das Passwort in das zweite Feld ein", font=('Calibri', 12)).pack(ipady=20)
 
 #  Entry boxen (input)

char_length = Entry(root, font= ("Arial", 14))
char_usage = Entry(root, font= ("Arial", 14))
pw_output = Entry(root, font=("Norasi", 14))
#pw_output.config(state="readonly")

 # Start text /beispiel Text in den Entry boxen

char_length.insert(0,"z.b. 36...") #  0 steht fr die position
char_usage.insert(0, "z.b. Youtube")

 #  beim clicken auf das Eingabefeld wird das beispiel geloescht

def click(event):
   char_length.configure(state=NORMAL) #  Configure laesst einen den "State" des Objektes bestimmen
   char_length.delete(0, END) #  Loeschen des Entry textes
   char_length.unbind('<Button-1>', clicked)

clicked = char_length.bind('<Button-1>', click)

 #  noch ohne funktion ------------------------------------------------------------------------------------------------------------------------------------
def click2(event2):
   char_usage.configure(state=NORMAL)
   char_usage.delete(0, END)
   char_usage.unbind('<Button-1>', clicked2)

clicked2 = char_usage.bind('<Button-1>', click2)
 #  ------------------------------------------------------------------------------------------------------------------------------------
 
 #  Definierung der position padx X-achse pady Y-achse

char_length.pack(padx=10)
char_usage.pack(padx=40)

 # generieren des Passwortes Via Entry angegebene laenge

def generate_password():
    length = char_length.get()
    password = "".join(random.sample(chars, int(length)))
    label_password.config(state="normal", text= 'Generiertes Passwort: ' + password) #
    note = char_usage.get() + ":"
    with open("saves.txt", "a") as f: #  oeffnet die angegenene Text datei und speichert das Generierte passwort
        f.write(str(note )) #  muss in einzelne Zeilen geschrieben werden
        f.write(sp)
        f.write(password)
        f.write(sp1)
        f.write(sp2)
        print("\n",password, "\n", "Kopieren sie das oben angezigte Passwort.", "\n") #  work-around zum Kopieren des passwortes ausgabe im terminal
    copy = pyperclip.copy(password)



Button(root, text="Passwort generieren", command=generate_password, font=('Calibri', 12)).pack(padx=10)
label_password = Label(root, font=('Norasi', 12))
label_password.pack()

root.mainloop()
