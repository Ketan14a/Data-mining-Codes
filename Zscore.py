import math

N = int(input("Enter n:"))
Nlist = []
print("Now, enter " + str(N) + " values:")
sum=0
for i in range(N):
    temp = int(input())
    sum = sum + temp
    Nlist.append(temp)



mean = sum/N


Stdevs = []
sum=0
for i in Nlist:
    diff = i - mean
    sum = sum + (diff**2)

Ans = sum/N
Stdev = math.sqrt(Ans)


Zscorelist = []

for i in Nlist:
    temp = (i-mean)/Stdev
    print(str(i)+" gets normalized to " + str(temp))






















