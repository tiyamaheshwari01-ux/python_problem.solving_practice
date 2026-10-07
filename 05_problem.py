#Write a program to find the sum of first n natural numbers using while loop.
"""n=int(input("enter a number:"))
i=1
sum=0# to store in sum of temporari i value which will be assignes a = 5 , 5+4+3+2+1
while(i<=sum):
    sum= sum+1
    i+=1
    print(sum)"""
n = int(input("Enter a number: "))
i = 1
total_sum = 0 # Renamed from 'sum' to avoid confusion with Python's sum() function

while i <= n:
    total_sum = total_sum + i  # Add the current number (i) to our total
    i += 1                     # Increment i to the next natural number

print("The total sum is:", total_sum)
