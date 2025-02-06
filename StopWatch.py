import tkinter as Tkinter

counter = 0
running = False

def count(label):
    global counter
    if running:
        counter += 1
        label.config(text=str(counter))
        root.after(999, lambda: count(label))  # Appelle `count` après 1 seconde

def Start(label):
    global running
    running = True
    count(label)
    start['state'] = 'disabled'
    stop['state'] = 'normal'
    reset['state'] = 'normal'

def Stop():
    global running
    running = False
    start['state'] = 'normal'
    stop['state'] = 'disabled'
    reset['state'] = 'normal'

def Reset(label):
    global counter, running
    running = False
    counter = 0
    label.config(text="Ready to go !")
    start['state'] = 'normal'
    stop['state'] = 'disabled'
    reset['state'] = 'disabled'

root = Tkinter.Tk()
root.title("Stopwatch")

root.minsize(width=250, height=70)
label = Tkinter.Label(root, text="Welcome!", fg="black", font="Verdana 30 bold")
label.pack()

f = Tkinter.Frame(root)
start = Tkinter.Button(f, text='Start', width=6, command=lambda: Start(label))
stop = Tkinter.Button(f, text='Stop', width=6, state='disabled', command=Stop)
reset = Tkinter.Button(f, text='Reset', width=6, state='disabled', command=lambda: Reset(label))

f.pack(anchor='center', pady=5)
start.pack(side="left")
stop.pack(side="left")
reset.pack(side="left")

root.mainloop()