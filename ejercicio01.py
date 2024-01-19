
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
import datetime
z = int(input("posicion: "))
h = int(input("el tiempo de ejecucion de que funcion quieres medir fibonacci (1) o fiborec (2): "))
if h == 1:
    hasiera = datetime.datetime.now()
    x = fibonacci(z)
    print(x)
    fin = datetime.datetime.now()
    total = fin - hasiera
    print("el tiempo de ejecucion es",total)
if h == 2:
    hasiera = datetime.datetime.now()
    x = fiborec(z)
    print(x)
    fin = datetime.datetime.now()
    total = fin - hasiera
    print("el tiempo de ejecucion es",total)



