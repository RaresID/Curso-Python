# Solicitar la edad al usuario
edad = input("Que edad tienes?")
# Convertir la entrada a entero
edad = int(edad)
# Evaluar la edad usando if-elif-else
if edad < 13:
    print("Eres un niño")
elif edad >= 13 and edad <= 17:
    print("Eres un adolescente")
elif edad >= 18 and edad <= 64:
    print("Eres un adulto")
else:
    print("Eres un adulto mayor")
# Mostrar el mensaje correspondiente