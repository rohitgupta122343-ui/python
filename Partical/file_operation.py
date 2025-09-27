
def text():

    with open("example.txt","w") as file:
        file.write("This is a first line of the file\n")
        file.write("This is a second line of file ")

    with open("example.txt","r") as file:
        content = file.read()
        print(content)


text()