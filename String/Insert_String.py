
def insert_Str(str,sub,index):

    ans = str[:index] + sub 
    return ans


str = "hello "
sub = "world "
index = 5

print(insert_Str(str,sub,index))