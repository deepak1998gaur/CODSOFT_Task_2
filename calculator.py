print('''
Addition(+)
Substract(-)
Multiply(*)
Divide(/)''')

num1=int(input("enter the value1: "))
num2=int(input("enter the value2: "))
oprator=input("enter the opr..(+,-,*,/:-) ")
if oprator=="+":
    print(num1+num2)
elif oprator=="-":
    print(num1-num2)
elif oprator=="*":
    print(num1*num2)
elif oprator=="/":
    print(num1/num2)
else:
    print("invalid oppr....")