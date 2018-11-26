
import tkinter as tk

class Application(tk.Frame):

    def __init__(self, master=None):

       # Old method
       # tk.Frame.__init__(master)

       # New method
        super().__init__(master)
        self.master = master
        self.master.minsize(400,400)
        self.master.maxsize(400,400)
        self.pack()
        self.create_widgets()
        

    def create_widgets(self):
        #creating widgets button hello
        self.hello = tk.Button(self)
        self.hello["text"] = "Say hello!"
        self.hello["command"] = self.say_hello
        self.hello.pack(side="top")
        #creating widgets quit
        self.getout = tk.Button(self, text ="GETOUT", fg="red", command = self.master.destroy)
        self.getout.pack(side="bottom")

    def say_hello(self):
        print("HELLO! EVERYONE")


root = tk.Tk()
app = Application(master=root)

app.mainloop()

