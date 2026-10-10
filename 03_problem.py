# write a program to generate table from 2 to 20 
for i in range(2, 21):
    def generatetable(n):
        table = ""
        for i in range(1, 11):
            table += f"{n} x {i} = {n*i}\n"
        return table