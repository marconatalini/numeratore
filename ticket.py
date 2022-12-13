import tkinter as tk
from database import DB

class App(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack(padx=100, pady=100)

        self.entrythingy = tk.Entry()
        self.entrythingy.pack()

        # Create the application variable.
        self.contents = tk.StringVar()
        # Set it to some value.
        self.contents.set("this is a variable")
        # Tell the entry widget to watch this variable.
        self.entrythingy["textvariable"] = self.contents

        # Define a callback for when the user hits return.
        # It prints the current value of the variable.
        self.entrythingy.bind('<Key-Return>',self.print_contents)

        self.entrythingy.bind('<Key-F3>', self.get_numero)


    def print_contents(self, event):
        print("Hi. The current entry content is:",
              self.contents.get())

    def get_numero(self, event):
        db = DB()
        numero = f"{db.get_next_numero_alluminio()}_0"
        self.contents.set(numero)


root = tk.Tk()
myapp = App(root)
myapp.mainloop()