import tkinter as tk
def show():
    print(entry.get())
window = tk.Tk()
entry = tk.Entry(window) 
entry.pack()
button = tk.Button(window,text = "Submit",command=show)  
button.pack() 
window.mainloop()
 