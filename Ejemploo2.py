# Esta función principal ejecuta el código principal del programa
def main():
    # Definir las variables

    while True:
        try:
            numero1 = float(input("Ingrese numero 01: "))
            numero2 = float(input("Ingrese numero 02: "))
            numero3 = float(input("Ingrese numero 03: "))

            if numero1.is_integer() or numero2.is_integer() or numero3.is_integer():
                break
            else:
                raise ValueError("Por favor, ingrese un numero valido.")
        except ValueError:
            print("Por favor, ingrese un número válido")

    # Calcular el resultado llamando a la función 'calcular'
    resultado = calcular(numero1, numero2, numero3)

    # Mostrar el resultado
    print("El resultado es:", resultado)


# Esta función calcula el resultado de a * b + c
def calcular(primerfactor, segundofactor, tercerfactor):
    resultado = primerfactor * segundofactor + tercerfactor
    return resultado


# Llamar a la función principal para ejecutar el programa
main()
