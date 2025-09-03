def sumar(a, b):
    """Devuelve la suma de dos números"""
    return a + b

def restar(a, b):
    """Devuelve la resta de dos números"""
    return a - b

def multiplicar(a, b):
    """Devuelve la multiplicación de dos números"""
    return a * b

def dividir(a, b):
    """Devuelve la división de dos números (con validación de cero)"""
    if b == 0:
        return "Error: No se puede dividir entre 0"
    return a / b

def mostrar_menu():
    """Muestra el menú de opciones"""
    print("\n=== CALCULADORA ===")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

def pedir_numero(mensaje):
    """Pide al usuario un número y lo convierte a float"""
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Error: Ingresa un número válido.")

def calculadora():
    """Función principal que ejecuta la calculadora"""
    while True:
        mostrar_menu()
        opcion = input("Elige una opción (1-5): ")

        if opcion == "5":
            print("¡Gracias por usar la calculadora! 👋")
            break

        if opcion in ["1", "2", "3", "4"]:
            a = pedir_numero("Ingresa el primer número: ")
            b = pedir_numero("Ingresa el segundo número: ")

            if opcion == "1":
                resultado = sumar(a, b)
            elif opcion == "2":
                resultado = restar(a, b)
            elif opcion == "3":
                resultado = multiplicar(a, b)
            elif opcion == "4":
                resultado = dividir(a, b)

            print(f"Resultado: {resultado}")
        else:
            print("Opción inválida. Intenta de nuevo.")

if __name__ == "__main__":
    calculadora()