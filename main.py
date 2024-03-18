import Modelo
from UI import mostrar_menu, obtener_opcion, obtener_cantidad

def main():
    print("Bienvenido")
    
    while True:
        mostrar_menu()
        opcion = obtener_opcion()
        
        if opcion == 1:
            Modelo.crear_cuenta(None, None, None, None)

        elif opcion == 2:
            numero_cuenta = int(input("Por favor ingrese el número de cuenta: "))
            cantidad = obtener_cantidad()
            for cuenta in Modelo.cuentaClientes:
                if cuenta.numero_cuenta == numero_cuenta:
                    cuenta.depositar_dinero(cantidad)
                    break
            else:
                print("La cuenta especificada no existe.")

        elif opcion == 3:
            numero_cuenta = int(input("Por favor ingrese el número de cuenta: "))
            cantidad = obtener_cantidad()
            for cuenta in Modelo.cuentaClientes:
                if cuenta.numero_cuenta == numero_cuenta:
                    cuenta.retirar_dinero(cantidad)
                    break
            else:
                print("La cuenta especificada no existe.")

        elif opcion == 4:
            numero_cuenta = int(input("Por favor ingrese el número de cuenta: "))
            for cuenta in Modelo.cuentaClientes:
                if cuenta.numero_cuenta == numero_cuenta:
                    cuenta.mostrar_datos()
                    break
            else:
                print("La cuenta especificada no existe.")

        elif opcion == 5:
            print("Gracias por usar nuestro servicio.")
            break

        else:
            print("Opción no válida. Por favor seleccione una opción válida.")

if __name__ == "__main__":
    main()
