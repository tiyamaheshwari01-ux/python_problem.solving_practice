#Write a program to find whether a given number is prime or not.
a=int(input("enter the number:"))
i=1
for i in range(2,a):# this logical syntax to find out a prime number 
    
        if(a%i)==0:
                print("this is not a prime number")
                break
else:
    print("it is a prime no")

