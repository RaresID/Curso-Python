print("=" * 20)
print("NUMEROS ENTEROS")
print("=" * 20)


edad = 25
temperatura_bajo_cero = -10
poblacion_mundial = 8_000_000_000

print(f"Edad: {edad}")
print(f"Edad: "+ str(edad))
print(f"Temperatura bajo cero: {temperatura_bajo_cero}")
print(f"Población mundial: {poblacion_mundial}")

complejo = 3+4j
print(f"Numero complejo: {complejo}")
print(f"Parte real: {complejo.real}")
print(f"Parte imaginaria: {complejo.imag}")

print("\n")
print("=" * 20)
print("OPERACIONES")
print("=" * 20)
print("\n")

suma = 5 + 3
resta = 10 - 4
multiplicacion = 3 * 7
division = 20 / 4

print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicacion: {multiplicacion}")
print(f"Division: {division}")

redondeo_decimal = round(3.141592, 2)
print(f"Redondeo a 2 decimales: {redondeo_decimal}")

print("\n")
print("=" * 20)
print("CONVERSIONES")
print("=" * 20)
print("\n")

edad_aproximada = int(27.2)
print(f"Edad aproximada: {edad_aproximada}")

precio_exacto = float(20)
print(f"Precio exacto: {precio_exacto}")

cantidad = int("15")
medida = float("8.2")

print("\n")
print("=" * 20)
print("NUMEROS ALEATORIOS")
print("=" * 20)
print("\n")

import random

dado = random.randint(1,6)
print(f"Tirar un dado: {dado}")
print(f"Tirar un dado: {random.randint(1, 6)}")
print(f"Tirar un dado: {random.randint(1, 6)}")
print(f"Tirar un dado: {random.randint(1, 6)}")
print(f"Tirar un dado: {random.randint(1, 6)}")
print(f"Tirar un dado: {random.randint(1, 6)}")
print(f"Tirar un dado: {random.randint(1, 6)}")

print("\n")
print("=" * 20)
print("TEXTO STRING")
print("=" * 20)
print("\n")

nombre_simple = 'Ana'
mensaje = "Hola, como estás?"
descripcion = """Este es un texto
que ocupa varias
lineas"""

print(nombre_simple)
print(mensaje)
print(descripcion)

palabra = "Hola"
letra_L = palabra[2]
print(letra_L)

print("\n")
print("=" * 20)
print("METODOS DE CADENAS")
print("=" * 20)
print("\n")

genero = "Corvus"
especie = "Monedula"
especie_minusculas = especie.lower()

nombre_cientifico = genero + " " + especie_minusculas
print(nombre_cientifico)

print("\n")
print("=" * 20)
print("BUSQUEDAS EN CADENAS")
print("=" * 20)
print("\n")

frase = "Me encantan las aves"

contiene_ave = "aves" in frase
print(f"Frase: {frase}")
print(contiene_ave)

print("\n")
print("=" * 20)
print("FORMATEO DE CADENAS")
print("=" * 20)
print("\n")

nombre = "Grajilla"
edad = 27
mensaje = f"Hola, me llamo{nombre} y tengo {edad} años"

print(mensaje)

print("\n")
print("=" * 20)
print("")
print("=" * 20)
print("\n")

edad = 25
edad_texto = str(edad)
print("Edad: " + edad_texto)

print("\n")
print("=" * 20)
print("BOOLEAN")
print("=" * 20)
print("\n")

esta_lloviendo = True
print(f"¿Esta lloviendo?{esta_lloviendo}")

es_fin_de_semana = False
print(f"¿Es fin de semana? {es_fin_de_semana}")

print("\n")
print("=" * 20)
print("CONVERSIONES")
print("=" * 20)
print("\n")

print(bool(0))
print(bool(42))
print(bool(""))
print(bool([]))
print(bool([1, 2, 3]))
