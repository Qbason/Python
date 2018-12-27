import tkinter 
import gamefortwo
import gameforone



class Application(tkinter.Frame,gameforone.Score):



    def create_widgets(self):

        self.single = tkinter.Button(self)
        self.single["text"] = "Single Player"
        self.single["command"] = gameforone.singleplayer
        self.single["fg"] = "green"
        
        self.single.pack(fill="x",ipadx=10,ipady=10,padx=10,pady=10)

        self.multi = tkinter.Button(self)
        self.multi["text"] = "MultiPlayer"
        self.multi["command"] = gamefortwo.multiplayer
        self.multi["fg"] = "green"
        self.multi.pack(fill="x",ipadx=10,ipady=10,padx=10,pady=10)

        self.options = tkinter.Button(self)
        self.options["text"] = "Options"
        self.options["command"] = None # run a code....
        self.options["fg"] = "green"
        self.options.pack(fill="x",ipadx=10,ipady=10,padx=10,pady=10)

     


        self.quit = tkinter.Button(self)
        self.quit["command"] = self.master.destroy
        self.quit["text"] = "QUIT"
        self.quit["fg"] = "red"
        self.quit.pack(fill="x",ipadx=10,ipady=10,padx=10,pady=10)

    def __init__(self,master=None):
        super().__init__(master)
        self.master = master
        self.master.minsize(400,400)
        #self.master.config(bg="green")
        self.master.title("Snake game")
        self.pack()
        self.create_widgets()

        
root = tkinter.Tk()

app = Application(master = root)


app.mainloop()