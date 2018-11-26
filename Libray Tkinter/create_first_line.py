import tkinter as tk


class Application (tk.Frame,tk.Canvas):

        def create_widgets(self):
            self.quit = tk.Button(self.master)
            self.quit["fg"] = "red"
            self.quit["command"] = self.master.destroy
            self.quit.pack(side="left")
            self.quit["text"] = "Quit!"

            #self.c = self.tk.Canvas(master,width=200,height=200)
            # self.c.pack(side="right")
            #self.create_line(0,0,200,100)

        def __init__(self,master = None):
            super().__init__(master)
            #tk.Frame.__init__(master)
            self.master = master
            self.master.minsize(500,500)
            self.master.title("Nazwa okienka")

            #self.pack()

            self.create_widgets()
        


   


root = tk.Tk()

app = Application(master = root)

app.mainloop()

