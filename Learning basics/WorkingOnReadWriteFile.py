
class Work_on_file():
    # default name of file is data.txt
    #implement a name_file to object
    def __init__(self,name_file = "data.txt"):
        self.name_file = name_file

    def write(self,data):
        #Write something to file 
        try:
            file = open(    self.name_file    ,"w")
            file.write( str(data)   )
        finally:
            file.close()
    
    def read_content(self,howmuchbytes = None):
        #Read something from file

        # 1 way read whole content
        with open(self.name_file,"r") as f:
            self.content = ''
            try:
                self.content = f.read(howmuchbytes)
            finally:
                f.close()
                return self.content

    def read_line_by_line(self):
        # 2 way read line by line
        self.lines = []
        with open("data.txt","r") as f:
            try:
                for line in f:
                    self.lines.append(line)
                    #print(line)
                    
            finally:
                f.close()
                return self.lines

    def read_char_by_char(self):
        # 3 way read char to char basic on 1 way ( read whole content)
        with open("data.txt","r") as f:
            self.chars = []
            try:
                content = f.read()
                for char in content:
                    #print(char)
                    self.chars.append(char)
            except:
                print("Error read char by char")
            finally:
                f.close()
                return self.chars


data = Work_on_file()
data.write("content \nsomething more \nthen that")

print(data.read_content())
print(data.read_line_by_line())
print(data.read_char_by_char())







