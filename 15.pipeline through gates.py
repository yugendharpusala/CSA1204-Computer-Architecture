a=int(input("Enter a number:"))
b=int(input("Enter another number:"))
c=4
rand=a&b
ror=a|b
rnand=~rand
print("The cycle value is",c)
ins=int(input("Enter the no of instructions"))
print("The performance measure:",ins/c)
print("Result and=",rand)
print("Result or=",ror)
print("Result nand=",rnand)
