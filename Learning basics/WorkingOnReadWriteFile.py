
class Work_on_file():
    # default name of file is data.txt
    #implement a name_file to object
    def __init__(self,name_file = "data.txt"):
        self.name_file = name_file

    def write(self,data):
        #Write something to file 
        try:
            file = open(    self.name_file    ,"a")
            file.write( str(data)   )
        finally:
            file.close()
    
    def read_content(self,howmuchbytes = None):
        #Read something from file

        # 1 way read whole content
        with open(self.name_file,"r") as f:
            try:
                content = f.read(howmuchbytes)
                print(content)
            finally:
                f.close()

    def read_line_by_line(self):
        # 2 way read line by line
        with open("data.txt","r") as f:
            try:
                for line in f:
                    print(line)
                    
            finally:
                f.close()

    def read_char_by_char(self):
        # 3 way read char to char basic on 1 way ( read whole content)
        with open("data.txt","r") as f:
            try:
                content = f.read()
                for char in content:
                    print(char)
            except:
                print("Error read char by char")
            finally:
                f.close()


data = Work_on_file()
data.write("content \nsomething more \nthen that")
data.read_content()
#data.read_line_by_line()
#data.read_char_by_char()








