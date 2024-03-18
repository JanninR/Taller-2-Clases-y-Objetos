class Cuenta:
    def __init__(self, numero_cuenta, documento_identidad, nombre_cliente, saldo):     
        self.numero_cuenta = numero_cuenta
        self.documento_identidad = documento_identidad
        self.nombre_cliente = nombre_cliente
        self.saldo = saldo

    def depositar_dinero(self, cantidad):
        cantidad_depositada = (cantidad - cantidad*0.19)
        self.saldo += cantidad_depositada
        print(f"Se depositaron {cantidad_depositada} a la cuenta {self.numero_cuenta}.")
        print(f"Saldo actual: {self.saldo}")

    def retirar_dinero(self, cantidad):
        if self.saldo >= cantidad:
            self.saldo -= cantidad
            print("Retiro exitoso.")

        else:
            print("Saldo insuficiente para realizar el retiro.")
        
    def mostrar_datos(self): 
        print("Numero de la cuenta:", self.numero_cuenta)
        print("Documemto de identidad del cliente:", self.documento_identidad)
        print("Nombre del cliente:", self.nombre_cliente)
        print("Saldo actual:", self.saldo)

cuentaClientes = []

def crear_cuenta(numero_cuenta, documento_identidad, nombre_cliente, saldo):
        documento_identidad = int(input("Por favor ingrese el documento de identidad: "))
        numero_cuenta = int(input("Por favor ingrese el número de cuenta: "))
        nombre_cliente = input("Por favor ingrese el nombre del cliente: ")
        saldo = float(input("Por favor ingrese el saldo inicial: "))

        nueva_cuenta = Cuenta(numero_cuenta, documento_identidad, nombre_cliente, saldo)
        cuentaClientes.append(nueva_cuenta)



