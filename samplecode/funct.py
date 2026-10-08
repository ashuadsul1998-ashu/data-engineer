def num(data):
    value=0
    for i in range(len(data)):
        if data[i] >  value:
            value=data[i]
    return value
num_list=[10,20,30,40,50]
result=num(num_list)
print(result)
