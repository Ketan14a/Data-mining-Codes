import math

Bins = []
N = int(input("Enter n:"))
Nlist = []
print("Now, enter " + str(N) + " values:")
sum=0
for i in range(N):
    temp = float(input())
    Nlist.append(temp)


b = max(Nlist)
a = min(Nlist)
width = math.ceil((b-a)/N)

Printed = []
Show = []
for i in Nlist:
    if i not in Printed:
        Printed.append(i)
        for j in Nlist:
            if j not in Printed:
                if j>=(i+width) and j<=(i+2*width):
                    Show.append(j)
                    Printed.append(j)


        print(Show)
        Show=[]































