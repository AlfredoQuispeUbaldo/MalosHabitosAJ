# Función para calcular el área de un rectángulo
def calcular_area_rectangulo(base, altura):
    if base <= 0 or altura <= 0:
        raise ValueError("La base y la altura deben ser números positivos.")
    area = base * altura
    return area

# Función para calcular el área de un triángulo
def calcular_area_triangulo(base, altura):
    if base <= 0 or altura <= 0:
        raise ValueError("La base y la altura deben ser números positivos.")
    area = 0.5 * base * altura
    return area

# Función principal
def main():
    # Pedir al usuario la base del rectángulo
    while True:
        try:
            base_rectangulo = float(input("Ingrese la base del rectángulo: "))
            if base_rectangulo.is_integer():
                break
            else:
                raise ValueError("Por favor, ingrese un número entero para la base del rectángulo.")
        except ValueError:
            print("Por favor, ingrese un número válido para la base del rectángulo.")

    # Pedir al usuario la altura del rectángulo
    while True:
        try:
            altura_rectangulo = float(input("Ingrese la altura del rectángulo: "))
            if altura_rectangulo.is_integer():
                break
            else:
                raise ValueError("Por favor, ingrese un número entero para la altura del rectángulo.")
        except ValueError:
            print("Por favor, ingrese un número válido para la altura del rectángulo.")

    # Calcular y mostrar el área del rectángulo
    area_rectangulo = calcular_area_rectangulo(base_rectangulo, altura_rectangulo)
    print("Área del rectángulo:", area_rectangulo)

    # Pedir al usuario la base del triángulo
    while True:
        try:
            base_triangulo = float(input("Ingrese la base del triángulo: "))
            if base_triangulo.is_integer():
                break
            else:
                raise ValueError("Por favor, ingrese un número entero para la base del triángulo.")
        except ValueError:
            print("Por favor, ingrese un número válido para la base del triángulo.")

    # Pedir al usuario la altura del triángulo
    while True:
        try:
            altura_triangulo = float(input("Ingrese la altura del triángulo: "))
            if altura_triangulo.is_integer():
                break
            else:
                raise ValueError("Por favor, ingrese un número entero para la altura del triángulo.")
        except ValueError:
            print("Por favor, ingrese un número válido para la altura del triángulo.")

    # Calcular y mostrar el área del triángulo
    area_triangulo = calcular_area_triangulo(base_triangulo, altura_triangulo)
    print("Área del triángulo:", area_triangulo)

if __name__ == "__main__":
    main()
