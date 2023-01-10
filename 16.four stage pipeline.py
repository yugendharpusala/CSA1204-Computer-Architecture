a=int(input("Enter number 1:"))
b=int(input("Enter number 2:"))
c=3
f=0
ch=int(input("1.Add,2.sub,3.Mul,4.Div:"))
if ch==1:
    print("performing addition operation:")
    res=a+b
elif ch==2:
    print("performing subtraction operation:")
    res=a-b
elif ch==3:
    print("performing multiplication operation:")
    res=a*b
elif ch==4:
    print("performing divison operation:")
    if b==0:
        print("Denominator cant be zero")
        print("Wrong input")
        f=1
    else:
        res=a/b
else:
    print("Wrong input")
    f=1
if f==0:
    print("The cycle value is",c)
    ins=int(input("Enter no of instructions:"))
    print("The performance measure:",ins/c)
