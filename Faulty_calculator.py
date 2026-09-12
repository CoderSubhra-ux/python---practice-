print("----Faulty Calculator---")
x= int(input("Enter first digit:-"))
abb= (input("aapka lakshya chune :- [+,-,*,/] --"))
y= int(input("Enter second digit:-"))

if x==10 and y==15 and '+' :
	print("30")
elif x==5 and y==3 and '*' :
	print("20")
elif x==10 and y== 6 and '-':
	print("5")
elif x==30 and y==10 and '/' :
	print("5")
	
else:
    if abb == '+':
        print(x+y)
    elif abb == '-':
        print(x-y)
    elif abb == '*':
        print(x*y)
    elif abb == '/':
        print(x/y)
