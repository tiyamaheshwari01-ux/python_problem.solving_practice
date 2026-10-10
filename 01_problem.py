f = open("poem.txt")
c = f.read()
if("twinkle" in c):
    print("Yes, 'twinkle' is present in the poem.")

else:
    print("No, 'twinkle' is not present in the poem.")
f.close()