# factorial 5!=5 x 4 x 4 x 3 x 2 x 1

a= int(input("enter the number:"))
product = 1# when you multiple you intialize from one.

for i in range(1,a+1):
    product = product*i
    print(f"the prduct on factorial of{a} is {product}")
# works
