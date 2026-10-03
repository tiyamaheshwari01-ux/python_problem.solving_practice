#Write a program to find the greatest of four numbers entered by the user.
a=int(input("enter the number:"))
b=int(input("enter the number:"))
c=int(input("enter the number:"))
d=int(input("enter the number:"))
"""if a>b:
    print(a)
elif b>c:
    print(b)
elif c>d:
    print(c)
else:
    print(d)"""# this wont work every single time bcz you are not compaining every single value with out its just 
#first to second ,second to third ,third to fourth, foruth 

# but to create you need to compare every single value with one another so that we get the correct match 
if(a>b and a>c and a>d):
    print("gretest number",a)
elif(b>a and b>c and b>d):
    print("gretest number",b)
elif(c>a and c>b and c>d):
    print("gretest number",b)
elif(d>a and d>b and d>c):
    print("gretest number",d)
#works
