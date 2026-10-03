# Write a program to find whether a given username contains less than 10 
#   characters or not.
a =(input("enter your name:"))
if (len(a)<10):
   # here no one iscounting a since a is string which might be converted into the int but noone is counting how many charcter are there ina  
# so we are inbulding the len funtion with the condition.(fun + condition)
   print("valid name")
else:
   print("limit excceded")

# even you need to count the name given by user you dont need to convert it into string 
# why?
# bcz the len function counts that ,
