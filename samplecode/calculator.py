def calc(num):
	if num=="add":
		return add(a,b)
	if num=="mul":
		return mul(a,b)
	if num=="div":
		return div(a,b)
	if num=="sub":
		return sub(a,b)
	if num=="rem":
		return rem(a,b)
		
def add(a,b):
	return a+b
def sub(a,b):
	return a-b
def div(a,b):
    return a/b
def rem(a,b):
	return a%b
def mul(a,b):
	return a*b

a=int(input("value of a: "))
b=int(input("value of b: "))
operation=input("please choose options (add,sub,mul,div,rem): ")
print(calc(operation))
