def dividir_numeros():
    try:

        # Solicitar al usuario que introduzca dos números
        numero1 = input("Introduce  numero 1")
        numero2 = input("Introduce  numero 2")
        
        
        # Convertir las entradas a números enteros
        num1=int(numero1)
        num2=int(numero2)
        
        # Realizar la división del primer número entre el segundo
        div = num1 / num2
        
        # Devolver el resultado de la división
        return div
    
    
    except ValueError:
            print("Error: Debes introducir un número válido")
    except ZeroDivisionError:
            print("Error: No es posible dividir entre cero")
    
    finally:
        print("Operación finalizada")


# Llamada a la función
dividir_numeros()