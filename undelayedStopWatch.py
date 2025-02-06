import tkinter as Tkinter
import time

'''
Utilisation de time.perf_counter() au lieu de time.time() pour une meilleur performance
On met a jour le chronometre apres 10ms pour garantir une bonne fluidité
Gere le stop et le restart du chronometre
'''

running = False
start_time = 0
elapsed_time = 0

def update_timer():
    if running:
        current_time = time.perf_counter() - start_time
        label.config(text=f"{current_time:.2f} s")  # Affichage avec 2 décimales
        root.after(10, update_timer)

def start():
    global running, start_time
    if not running:
        start_time = time.perf_counter() - elapsed_time  # Reprend là où il s'est arrêté
        running = True
        update_timer()
        start_button['state'] = 'disabled'
        stop_button['state'] = 'normal'
        reset_button['state'] = 'normal'

def stop():
    global running, elapsed_time
    if running:
        running = False
        elapsed_time = time.perf_counter() - start_time  # Sauvegarde le temps écoulé
        start_button['state'] = 'normal'
        stop_button['state'] = 'disabled'
        reset_button['state'] = 'normal'

def reset():
    global running, start_time, elapsed_time
    running = False
    start_time = 0
    elapsed_time = 0
    label.config(text="0.00 s")
    start_button['state'] = 'normal'
    stop_button['state'] = 'disabled'
    reset_button['state'] = 'disabled'

# Création de la fenêtre Tkinter
root = Tkinter.Tk()
root.title("Chronomètre précis")

label = Tkinter.Label(root, text="0.00 s", fg="black", font="Verdana 30 bold")
label.pack()

frame = Tkinter.Frame(root)
start_button = Tkinter.Button(frame, text='Start', width=6, command=start)
stop_button = Tkinter.Button(frame, text='Stop', width=6, state='disabled', command=stop)
reset_button = Tkinter.Button(frame, text='Reset', width=6, state='disabled', command=reset)

frame.pack(anchor='center', pady=5)
start_button.pack(side="left")
stop_button.pack(side="left")
reset_button.pack(side="left")

root.mainloop()