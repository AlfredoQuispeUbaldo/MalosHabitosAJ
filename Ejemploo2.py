# Esta función principal ejecuta el código principal del programa
def main():
    # Definir las variables
    num1 = 5
    num2 = 3
    num3 = 7

    # Calcular el resultado llamando a la función 'calcular'
    resultado = calcular(num1, num2, num3)

    # Mostrar el resultado
    print("El resultado es:", resultado)


# Esta función calcula el resultado de a * b + c
def calcular(primerfactor, segundofactor, tercerfactor):
    resultado = primerfactor * segundofactor + tercerfactor
    return resultado


# Llamar a la función principal para ejecutar el programa
main()
