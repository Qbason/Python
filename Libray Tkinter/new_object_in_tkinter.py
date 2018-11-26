from tkinter import *

# class Application(Frame):
#     def say_hi(self):
#         print ("hi there, everyone")
    
#     def createWidgets(self):
#         self.QUIT = Button(self)
#         self.QUIT["text"] = "QUIT"
#         #self.QUIT.config(fg = "red")
#         #self.QUIT["fg"] = "red"
#         self.QUIT["command"] = self.quit

#         self.QUIT.pack({"side": "left"})

#         self.hi_there = Button (self)
#         self.hi_there["text"] = "Hello"
#         self.hi_there["command"] = self.say_hi

#         self.hi_there.pack({"side": "left"})

#     def __init__(self, master=None):
#             Frame.__init__(self,master)
#             self.pack()
#             self.createWidgets()

# root = Tk()
# app = Application(master=root)
# app.mainloop()
# root.destroy()

class App(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()

        self.entrythingy = Entry()
        self.entrythingy.pack()

        # here is the application variable
        #self.content = StringVar()
        # set it to some value
        #self.content.set("this is a variable")
        # tell the entry widget to watch this variable
        self.entrythingy["textvariable"] #= self.content

        # and here we get a callback when the user hits return.
        # we will have the program print out the value of the
        # application variable when the user hits return
        self.entrythingy.bind('<Key-Return>', self.print_content)

    def print_content(self, event):
        print ("hi. contents of entry is now ---->", self.entrythingy.get())


root = Tk()
app = App(master = root)
app.master.minsize(200,200)
app.master.maxsize(400,400)
app.mainloop()
#root.destroy()