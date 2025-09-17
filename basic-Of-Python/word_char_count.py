
# Write a program to compute number of characters and words in a
# string

# Nomal / Simple string 
str ="Here Some issues in a Numpy Python Libary"

# count to a total words in a string by using len property/method  
word_count = len(str)

# count to a character in string and blank space also split e.g -> hello -> 'h' , 'e' , 'l' , 'l' , 'o'
char_count = len(str.split())

print("Given String: ",str)
print("Number of character: ",char_count)
print("Number of Words: ",word_count)

