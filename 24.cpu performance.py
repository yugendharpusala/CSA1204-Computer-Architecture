p=int(input("enter no of processors: "))
ct=[]
for i in range(0,p):
    cpi = float(input("enter the cycles per instructions: "))
    cr = float(input("enter the  clock rate in GHZ" ))
    a = 1000*cpi/cr
    ct.append(a)
print("The processor has lowest exceution time: " , min(ct))
