"""s=set()
n1=int (input("enter the first number:"))
set.add(int(n1))

n2=int (input("enter the first number:"))
set.add(int(n2))

n3=int (input("enter the first number:"))
set.add(int(n3))

n4=int (input("enter the first number:"))
set.add(int(n4))

n5=int (input("enter the first number:"))
set.add(int(n5))

n6=int (input("enter the first number:"))
set.add(int(n6))

n7=int (input("enter the first number:"))
set.add(int(n7))

n8=int (input("enter the first number:"))
set.add(int(n8))
print(set)"""
# the point is that you cant  take set.add(set-is a in build function in the python so you cant assign it as a variable )
# as i mentioned before 
s = set()

n1 = int(input("Enter number 1: "))
s.add(n1)

n2 = int(input("Enter number 2: "))
s.add(n2)

n3 = int(input("Enter number 3: "))
s.add(n3)

n4 = int(input("Enter number 4: "))
s.add(n4)

n5 = int(input("Enter number 5: "))
s.add(n5)

n6 = int(input("Enter number 6: "))
s.add(n6)

n7 = int(input("Enter number 7: "))
s.add(n7)

n8 = int(input("Enter number 8: "))
s.add(n8)

print("Final set is:", s)
# the uppar wala code also wrkds just that you need to assign set=set()
# this hwere we are creating a aempty set 
#then the code will run how i created a emtry list was e=set()
#and i didn't assgned e as the e.add(int(n1))
