n=int(input("Enter binary: "))
sum=0
a=0
while n>0:
    r= n%10
    sum=sum=sum+r*(pow(2,a))
    a+=1
    n=n//10
print(sum)
                       
