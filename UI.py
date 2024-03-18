def mostrar_menu():
    print("1. Crear cuenta")
    print("2. Depositar dinero")
    print("3. Retirar dinero")
    print("4. Mostrar datos de la cuenta")
    print("5. Salir")

def obtener_opcion():
    return int(input("Por favor seleccione una opción: "))

def obtener_cantidad():
    return float(input("Por favor ingrese la cantidad: "))
