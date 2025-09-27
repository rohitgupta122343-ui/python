
def last_line_read(n):

    with open("last.txt","w") as file:
        file.write("this is a first line\n")
        file.write("this is a second line\n")
        file.write("this is a last line\n")

    with open("last.txt","r") as file:
        lines = file.readlines()    
        last_line = lines[-1]
        print(last_line,end='')
       
       


last_line_read(3)            