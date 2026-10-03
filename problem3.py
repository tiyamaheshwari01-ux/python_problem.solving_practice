#A spam comment is defined as a text containing following keywords:
#“Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program to detect these spams.

a=input("enter your comment:").lower()


"""if a==("make more money"and"buy now" and"click here" and "subscribe this"):"""
# basically this is what you do with ur head 
# python actually reads it like the last value will be tru value it will read it as 
#if a==("subcribe this") by ignoring the other value 
#so here we need to use #####
######################(in a or )################
if ("lost of money" in a or "subscribe this" in a or "click here" in a or "buynow" in a):
# if the condition is a string need to written with in the double quotes
    
    print("spam comment")
else:
    print("not spam")







# more cleaner way to do it 
# the other way to do it 
a= input("enter your comment").lower()
keywords=["subcribe now", "lot of money" , "get money", "click here"]
if any(word in a for word in keywords):
# any = koi bhi , word in a = jo input diya h usme ,(for ke jaise h koi) word in keywords= jo pehle se spam ghoshit kare kh kahi usme s toh nahi hai.
    print("spam")
else:
    print("not spam")

