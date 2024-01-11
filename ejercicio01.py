
def fibonacci(x):
    a = 0
    b = 1
    
    
    for  i in range (x - 1):
        c = a + b
        a = b
        b = c
 
    return c
def fiborec(y):
    if y == 0:
        return 0
    if y == 1:
        return 1
    if y > 1:
        return fiborec(y-1) + fiborec(y-2)
print(fiborec(int(input("posicion: "))))