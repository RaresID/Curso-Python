print("\n")
print("=" * 20)
print("ESTRUCTURAS CONTROL ITERATIVO")
print("=" * 20)
print("\n")

print("\n")
print("=" * 20)
print("BUCLES FOR")
print("=" * 20)
print("\n")

frutas = ["manzana", "banana", "cereza"]
print(f"Lista de frutas: {frutas}")

for fruta in frutas:
    print(fruta)

print("\n")
print("=" * 20)
print("RANGE")
print("=" * 20)
print("\n")

for i in range(5):
    print(i)
    
print("\n")

for i in range(3, 8):
    print(i)
    
print("\n")

for i in range (2, 11, 2):
    print(i)
    
print("\n")

for i in range(5, 0, 1):
    print(i)
    
print("\n")

# cuenta atrás hasta 0
for i in range(5, -1, -1):
    print(i)

print("\n")
print("=" * 20)
print("ITERAR SOBRE ÍNDICES")
print("=" * 20)
print("\n")

nombres = ["Ana", "Carlos", "Elena"]
print(f"Lista de nombres: {nombres}")

for i in range(len(nombres)):
    print(f"Posición {i}: {nombres[i]}")

print("\n")

for indice, nombre in enumerate(nombres):
    print(f"Posición {indice}: {nombre}")

print("\n")
print("=" * 20)
print("BUCLES WHILE")
print("=" * 20)
print("\n")

"""

Bucle while

Bucle indeterminado, porque se ejecuta en base a condiciones por lo que 
a priori podemos no saber cuántas veces se va a ejecutar.

Ideal para crear aplicaciones de consola (CLI apps)

No tiene do while como en Java, se podría emular con while True (bucle infinito)

Puede haber más de una condición en el while pero dificulta la lectura
"""
contador = -2

while contador < 10:
    print(contador)
    contador += 1
    
    
"""
Explorar la keyword "continue" permite saltar a la siguiente iteración
de un bucle sin ejecutar el código que hay después.

a diferencia de break, continue no rompe el bucle no salimos del bucle
simplemente salta a la siguiente iteración

Imprime números impares
"""

numero = 0

while numero < 10:
    numero += 1
    if numero % 2 == 0: # comprobar si el número es par
        continue
    
    print(f"Número impar {numero}")
    
    
    

"""
Bucle infinito

Ideal para aplicaciones de terminal-consola (cli)

Salimos del bucle cuando el usuario escriba salir

Es indeterminado porque a priori no sabemos cuándo el usuario va a querer salir

break rompe el bucle, sale del bucle.
"""

while True:
    print("""
            Welcome.
            Elige una opción:
            1 - Mostrar productos
            2 - Mostrar un producto
            salir - salir del programa
            """)

    opcion = input("Introduce una opción: ")
    print(f"Has elegido la opción: {opcion}")
    
    if opcion == "salir":
        print("Hasta la proxima")
        break
    

print("Fuera del bucle")



"""

Iterar una estructura de datos, por ejemplo una lista []

Itera la lista mientras la lista no esté vacía

La función pop() viene de las listas, y elimina y devuelve un elemento de la lista.

.pop(0) elimina el primero
.pop() elimina el último
"""

nombres = ["Kary", "Jorge", "Marcos"]

while nombres:
    nombre = nombres.pop(1)
    # if len(nombres) == 0:
    #     print("Ya no quedan mas nombres, este es el último:")
    print(nombre)
    