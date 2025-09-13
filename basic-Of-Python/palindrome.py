
def palindrome(val):
    
    ans = val[::-1]
    
    if ans == val:
        return True
    else:
        return False

val = input("Enter a Number or Word: ")


if palindrome(val):
    print("This is a Palindrome ",val)

else:
    print("This is Not a Palindrome ",val)

