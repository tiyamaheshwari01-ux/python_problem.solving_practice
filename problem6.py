# 6.
"""Write a program to calculate the grade of a student from his marks from the following scheme:
90 – 100 => Ex
80 – 90 => A
70 – 80 => B
60 – 70 =>C
50 – 60 => D
<50 => F"""

m1=int(input("enter marks of subject 1:"))
m2=int(input("enter marks of subject 2:"))
m3=int(input("enter marks of subject 3:"))


total_percentage=(100*(m1+m2+m3)/300)
print(total_percentage)

"""if total_percentage is 90-100:
    print("excellent")
if total_percentage is 80-90:
    print("best")

if total_percentage is 70-80:
    print("good")
if total_percentage is 60-70:
    print("okay")
else:
    print("better try next time,fail")"""
#in this python was only running the part of else statemenets that bhi bcz if was present then only else can run
# why it was wrong??
#since pythin don't take this as a range 90-100
# it takes as a calculation returning ans -10
# in ever case 
# correct code would look like 
if 90<=  total_percentage<=100:
    print("excellent")
elif 80<=  total_percentage<=90:
    print("grade a")
elif 70<=  total_percentage<=80:
    print("grade b")
elif 60<=  total_percentage<=70:
    print("grade c")
elif 50<= total_percentage<=60:
    print("fail")
    


    