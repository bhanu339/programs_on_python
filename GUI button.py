import tkinter as tk
def click():
    print("hello guys")
window = tk.Tk()
button = tk.Button(window, text = "Click Me",command = click)   
button.pack()
window.mainloop() 
    