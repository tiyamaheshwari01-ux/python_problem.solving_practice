#reate an empty dictionary. Allow 4 friends to enter their favorite language as value and use key as their names. Assume that the names are unique.
dic={}

name=input("enter the name:")
language=input("enter the lang:")
dic.update({name:language})# we have used .update bcz of dictionary, in set and list -.append is used but in dictionaru it's .update
#important dictionary = update not append 
name=input("enter the name:")
language=input("enter the lang:")
dic.update({name:language})

name=input("enter the name:")
language=input("enter the lang:")
dic.update({name:language})

name=input("enter the name:")
language=input("enter the lang:")
dic.update({name:language})

name=input("enter the name:")
language=input("enter the lang:")
dic.update({name:language})

print(dic)
# in output if you will enter the same name twic then you will name enter later means that is the most updated name since value withinthe dictionary 
# can be diferrent for the same key but two same keys cant exist at the same time.
