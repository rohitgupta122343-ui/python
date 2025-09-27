
def binary():
    data = bytearray([1,2,3,4])

    with open("example.bin","wb") as file:
        file.write(data)

    with open("example.bin","rb")as file:
        content = file.read()  
        print(content)  

binary()