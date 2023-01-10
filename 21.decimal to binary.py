n=int(input("Enter Decimal:"))
sum=0
m=1
while n>0:
    r=n%2
    n=n//2
    sum=sum+(r*m)
    m=m*10
print("Binary:",sum)
