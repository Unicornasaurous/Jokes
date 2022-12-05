import tkinter as tk 
from random import choice, randint
root = tk.Tk()
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)
root.config(bg="black")
insult = tk.StringVar()
def insult_self():
    insults=("You're nothing...", "You dont deserve love", "Your family hates you", "You're not good enough.", "You smell like trash... cause you are.")
    insult.set(choice(insults))
    insult_window = tk.Toplevel(root)
    x = root.winfo_x()
    y = root.winfo_y()
    insult_window.geometry("+%d+%d" %(x+randint(100, 400),y+randint(100, 1500)))
    insult_label = tk.Label(insult_window, textvariable=insult, bg="pink").pack()
    root.after(1500, insult_window.withdraw)

suffering_button = tk.Button(root, text="Hit for self deprecation", command=insult_self, bg="pink").grid()
    
root.mainloop()
    

