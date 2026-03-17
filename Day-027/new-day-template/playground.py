# print("Hello World")
def add(*args):
    suma = 0
    for arg in args:
        suma += arg
    
    return suma

add_num = add(2,4,5,6,7,1)
print(add_num)



