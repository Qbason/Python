import tkinter 
import gamefortwo
import gameforone



class Application(tkinter.Frame,tkinter.Label):

    def go_singleplayer(self):
        self.master.destroy()
        gameforone.singleplayer()

    def go_multiplayer(self):
        self.master.destroy()
        gamefortwo.multiplayer()

    def create_widgets(self):

        self.single = tkinter.Button(self)
        self.single["text"] = "Single Player"
        self.single["command"] = self.go_singleplayer
        self.single["fg"] = "green"
        
        self.single.pack(side="top", fill="x",ipadx=20,ipady=20,padx=40,pady=30)

        self.multi = tkinter.Button(self)
        self.multi["text"] = "MultiPlayer"
        self.multi["command"] = self.go_multiplayer
        self.multi["fg"] = "green"
        self.multi.pack(fill="x",ipadx=20,ipady=20,padx=40,pady=30)

        # self.options = tkinter.Button(self)
        # self.options["text"] = "Options"
        # self.options["command"] = None # run a code....
        # self.options["fg"] = "green"
        # self.options.pack(fill="x",ipadx=10,ipady=10,padx=10,pady=10)


        self.quit = tkinter.Button(self)
        self.quit["command"] = self.master.destroy
        self.quit["text"] = "QUIT"
        self.quit["fg"] = "red"
        self.quit.pack(fill="x",ipadx=20,ipady=20,padx=40,pady=30)

        self.label = tkinter.Label(text="Snake Game ",fg="black",bg="white")
        self.label.pack(fill="x",ipadx=20,ipady=20)



    def __init__(self,master=None):
        super().__init__(master)
        self.master = master
        self.master.minsize(400,400)
        self.master.maxsize(400,400)
        self.master.config(bg="green")
        self.master.title("Snake game")
        self.pack()
        self.create_widgets()

        
root = tkinter.Tk()

app = Application(master = root)


app.mainloop()
































