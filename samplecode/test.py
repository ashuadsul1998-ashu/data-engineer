a=input("please enter your name: ")
b=input("please enter your age: ")

def boy(name,age):
    if name=="ashu" and age != 30:
        print("please enter correct age")
    elif age == 30:
        print("age verification completed.")
    elif name == "Kedar":
        print(name, "please login with password")
    elif age ==30 and name=="ashu":
        print("you have successfully login.")
    else:
        print("please enter correct credential.")
    
    for i in range(1,20,3):
        print(i)
boy(a,b)

list=[20,25,30]
def girl(data):
    age=[]
    for i in list:
        if i <= 20:
            eligibility="minor"
            age.append(eligibility)
            
        elif i > 20 and i < 30:
            eligibility= "Major"
            age.append(eligibility)
        else:
            eligibility= "mature"
            age.append(eligibility) 
    return age
result=girl(list)
print(result)
    