F = open('myfile.txt','r')
R = open('another.txt','w')

Fdata = F.read()
Flist = Fdata.split("\n")
for element in Flist:
    if element!='':
        R.write(element+"\n")



F.close()
R.close()

G = open('myfile.txt','w')
H = open('another.txt','r')

Hdata = H.read()
Hlist = Hdata.split("\n")

for i in Hlist:
    G.write(i+"\n")




G.close()
H.close()







