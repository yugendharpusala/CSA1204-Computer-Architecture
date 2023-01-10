a=int(input("Enter a number= "))
b=int(input("Enter another number= "))
c=4
f=0
print("select a choice")
ch=int(input("1 for Addition\n2 for subtraction\n3 for multiplication\n4 for Division\n"))
if ch==1:
    res=a+b
elif (ch==2):
    res=a-b
elif(ch==3):
    res=a*b
elif(ch==4):
    if(b==0):
        print("Denominator can't be zero/nWrong output")
        f=1
    else:
        res=a/b
else:
    print("Wrong output")
    f=1
if(f==0):
    print("The cycle value is",c)
    ins=int(input("Enter no. of instructions: "))
    print("The performance measure: ", ins/c)
    print("res=", res)
    
