ScalingFactor = int(input("Enter the scaling faactor:"))
N = int(input("Enter n:"))
Nlist = []
SF = 10**ScalingFactor
print("Now, enter " + str(N) + " values:")
for i in range(N):
    temp = int(input())

    Nlist.append(temp)



for i in Nlist:
    Ans = i/ SF
    print(str(i) + " gets normalized to " + str(Ans))
















