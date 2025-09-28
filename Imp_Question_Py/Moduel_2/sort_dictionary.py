
score = {
    
    "rohit" : 78,
    "rahul" : 19,
    "harry" : 92,
    "harpreet" : 90
}

asc = dict(sorted(score.items(), key = lambda item:item[1]))
print(asc)