#Writ a program to print multiplication table of a given number using for loop.
'''i=0
a=int(input("enter the number:"))
for i in range (1,11):# to be noted in rage itakes as the number from which we right not like in that of indexing 

    i=i*a
    print("table of 2:",i)

'''


# this as a code also runes forthe table of two but pratically this is better 
# by using f string 
n=int(input("enter the number:"))
for i in range(1,10):
    print(f"{n} x {i}= {n*i}")

# this is more professional to write a atable 

