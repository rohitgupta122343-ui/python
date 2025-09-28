
def copy():
    
    with open("example.txt","w")as file:
            
            file.write("this is a first line: \n")
            file.write("here some issues of numpy in python libary: \n")
            file.write("they fixed it  pip install numpy: ")

    with open("example.txt","r")as file:
          
          content = file.read()

    with open("copy.txt","w")as file:
         copy =  file.write(content) 
         print(copy) 

copy()             