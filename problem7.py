#Write a program to find out whether a given post is talking about “Harry” or not.
post="tanishka maheshwari is a good coder, she is also good with skills "
if "tanishka" in post:
    print("yes,its is about tanishka")
if "maheshwari" in post:# i have used elif statement it would have write down the first only since the first contion become tru it stopped there only 
    
    print("yes,it is about maheshwari ji")
else:
    print("post is for non coders")
