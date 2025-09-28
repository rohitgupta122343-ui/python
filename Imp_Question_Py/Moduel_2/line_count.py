
def count():

    with open("example.txt","w")as file:

        file.write("this is a first line\n")
        file.write("this is a second line\n")
        file.write("this is a last line\n")

    with open("example.txt","r")as file:

        lines = file.readlines()    
        print(f"no of a lines : {len(lines)}")
       
count()        
