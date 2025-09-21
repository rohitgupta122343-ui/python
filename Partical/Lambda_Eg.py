
# Write a lambda function that checks whether a given string starts with
# a specific character.


str = "hello"  # normal/ simple string

# Check The Given String start or end ? Given Character  
start_with = lambda s,c : s.startswith(c) 
end_with = lambda s,c :s.endswith(c)


# Start check examples
print(start_with(str,"h")) # True  ( The Given String Start With "hello" -> "h" ) 
print(start_with(str,"y")) # False ( The Given String Start With "hello" -> "h" ) 

# End check examples
print(end_with(str,"o")) # True  ( The Given String End With "hello" -> "o" )
print(end_with(str,"0")) # False ( The Given String End With "hello" -> "o" )  

