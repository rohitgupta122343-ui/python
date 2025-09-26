

str = input("enter a name: ")

ans = lambda str:str[0].lower() in 'aeiou'

print(f"{str}: --> {str[0]} --> {ans(str)}")