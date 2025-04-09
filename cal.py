#simple ass cal


def add(x,y):
    return x + y

def sub(x,y):
    return x - y
def mul(x,y):
    return x * y

def div(x,y):
    if y == 0:
        return "error: can not divide by 0"
    return x / y

print('this is a simple calculator')
print("pls select a operation:")
print("1.add")
print("2.sub")
print("3.mul")
print("4.div")
print("1/2/3/4")
x = input("enter your choice")

num1 = float(input("first number"))
num2 = float(input("second number"))

if x == '1':
    print("result", add(num1,num2))
elif x == '2':
    print("result",sub(num1,num2))
elif x == '3':
    print("result",mul(num1,num2))
elif x == '4':
    print("result",div(num1,num2))
else:
    print("invalid")

