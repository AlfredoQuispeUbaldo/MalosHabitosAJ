# Función principal
def main():
    print("Bienvenido al programa de suma y multiplicación")

    # Solicitar al usuario que ingrese num1 y num2
    num1 = solicitar_numero("Por favor, ingrese el primer número: ")
    num2 = solicitar_numero("Por favor, ingrese el segundo número: ")

    # Llamada a la función sumar para obtener z
    z = sumar(num1, num2)

    # Llamada a la función multiplicar para obtener el resultado final
    resultado = multiplicar(num1, z)

    # Impresión del resultado
    print("El resultado de multiplicar", num1, "por la suma de", num1, "y", num2, "es:", resultado)


# Función para solicitar al usuario que ingrese un número
def solicitar_numero(mensaje):
    while True:
        try:
            numero = float(input(mensaje))
            return numero
        except ValueError:
            print("Por favor, ingrese solo números.")


# Función para realizar la suma de dos números
def sumar(primerfactor, segundofactor):
    suma = primerfactor + segundofactor
    return suma


# Función para realizar la multiplicación de dos números
def multiplicar(primerfactor, segundofactor):
    multiplicacion = primerfactor * segundofactor
    return multiplicacion


# Verificación de si este script es el programa principal y, en caso afirmativo, ejecutar la función main
if __name__ == "__main__":
    main()
