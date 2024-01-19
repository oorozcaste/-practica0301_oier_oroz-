import csv
import cProfile

def lista_csv(s):
     with open(s, "r") as fitxategi:
          lista = csv.reader(fitxategi, delimiter= ',', quotechar= ',')
          lista1 = nombre_capital(lista) 
          lista2 = numero_dni(lista1)
               
          
          
          return print(lista2)
          
def nombre_capital(lista):
     for i in (lista):
          i[0] = i[0].title()
     return lista
          

def numero_dni(lista):
     letras = "TRWAGMYFPDXBNJZSQVHLCKE"
     for i in lista:
          x = int(i[1]) % 23
          i[1] = (i[1] +letras[x])
     return lista 
z = input("qeu lista quieres reescribir 50.csv o 1000.csv: ")
cProfile.run((lista_csv(z)))



