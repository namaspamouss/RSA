#coding:utf-8
from tkinter import *
from rsa_m import *

class App(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.bouton = Button(self)
        self.bouton["text"] = "clic me"
        self.bouton["command"] = print_something()
        self.bouton.pack(side=LEFT)

        self.bouton2 = Button(self)
        self.bouton2["text"] = "quitter"
        self.bouton2["command"] = self.quit
        self.bouton2.pack(side=LEFT)




app = Tk()
app.geometry("400x400")
app = App(master=app)
app.mainloop()