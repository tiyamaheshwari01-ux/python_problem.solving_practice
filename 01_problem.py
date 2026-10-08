# wri aprogram to find greatest of three number using function 
""""def grestest():# here i didn't delared the variable in the funtion defination
    if (a>b)or(a>c):
        print(a)
    elif(b>a)or(b>c):
        print(b)
    elif(c>a)or(c>b):
        print(c)


        # also for finding gretes we us and for the correct one 
        
    here a,b,c are not gibed in the function defination 
    and input is taken after comparision they will compar what than than gopal
    
        a=int(input("enter the number:"))
        b=int(input("enter the number:"))
        c=int(input("enter the number:"))
        return(grestest())"""
        # this will give you infinite recursions 


# the correct code 

def great(a, b, c):# assigning the variables used in the function defination 
    if (a > b) and (a > c):
        print(a)
    elif (b > a) and (b > c):
        print(b)
    else:
        print(c)
    # here the comparision ends 

a = int(input("enter the number: "))
b = int(input("enter the number: "))
c = int(input("enter the number: "))

great(a, b, c)
