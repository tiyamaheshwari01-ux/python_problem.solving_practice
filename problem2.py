m1=int(input("enter the marks of first subject"))
m2=int(input("enter the marks of first subject"))
m3=int(input("enter the marks of first subject"))
 # at first you need to find out the total percentage so that at least the siystem and compare 
 # the system wont solve the percentage khud s 
 # you need to put in formula with in the code 
 
total_percentage=(((m1+m2+m3)*100)/300)#formula
#we can also remove the zero writing it as (((m1+m2+m3))/3) to optimise the code and better mathematics


# here you can't write it as m1+m2+m3/300(this actually mean is m3/300)*
#better use braceket as used niow it will give you perfect output 


if total_percentage*100>=40 and m1>=33 and m2>=33 and m3>=33:
    print("you are pass",total_percentage)
else:
    print("try again next year",total_percentage)

    

