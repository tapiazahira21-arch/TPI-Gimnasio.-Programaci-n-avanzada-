#Prueba 24/06/26

# =========================
# 1. CLASE BASE
# =========================
class Persona:

    def __init__(self, nombre, apellido, dni):
        self._nombre = nombre
        self._apellido = apellido
        self._dni = dni

    def mostrar_datos(self):
        return f"{self._nombre} {self._apellido} | DNI: {self._dni}"


# =========================
# 2. CLASES DERIVADAS
# =========================
class Cliente(Persona):

    def __init__(self, nombre, apellido, dni, nro_socio):
        super().__init__(nombre, apellido, dni)
        self._nro_socio = nro_socio

    def mostrar_datos(self):
        return f"Cliente: {super().mostrar_datos()} | Socio N°: {self._nro_socio}"


class Profesor(Persona):

    # CAMBIO: horario por turno
    def __init__(self, nombre, apellido, dni, turno):
        super().__init__(nombre, apellido, dni)
        self._turno = turno

    # CAMBIO: horario por turno
    def mostrar_datos(self):
        return f"Profesor: {super().mostrar_datos()} | Turno: {self._turno}"


class Administrador(Persona):

    def __init__(self, nombre, apellido, dni):
        super().__init__(nombre, apellido, dni)

    def mostrar_datos(self):
        return f"Administrador: {super().mostrar_datos()}"

    def registrar_cliente(self, gimnasio, nombre, apellido, dni, nro_socio):
        cliente = Cliente(nombre, apellido, dni, nro_socio)
        gimnasio.agregar_cliente(cliente)
        return cliente

    # CAMBIO: horario por turno
    def registrar_profesor(self, gimnasio, nombre, apellido, dni, turno):
        profesor = Profesor(nombre, apellido, dni, turno)
        gimnasio.agregar_profesor(profesor)
        return profesor

    def registrar_pago(self, gimnasio, cliente, monto, fecha, metodo, estado):
        pago = Pago(cliente, monto, fecha, metodo, estado)
        gimnasio.agregar_pago(pago)
        return pago


# =========================
# 3. PAGO (ASOCIACIÓN)
# =========================
class Pago:

    def __init__(self, cliente, monto, fecha, metodo_pago, estado):
        self._cliente = cliente
        self._monto = monto
        self._fecha = fecha
        self._metodo_pago = metodo_pago
        self._estado = estado

    def mostrar_pago(self):
        return (
            f"Pago -> {self._cliente.mostrar_datos()} | "
            f"Monto: ${self._monto} | Fecha: {self._fecha} | "
            f"Método: {self._metodo_pago} | Estado: {self._estado}"
        )


# =========================
# 4. GIMNASIO (SINGLETON + AGREGACIÓN)
# =========================
class Gimnasio:
    _instancia = None

    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
        return cls._instancia

    def __init__(self):
        if not hasattr(self, "inicializado"):
            self._clientes = []
            self._profesores = []
            self._pagos = []
            self.inicializado = True

    # AGREGACIÓN
    def agregar_cliente(self, cliente):
        self._clientes.append(cliente)

    def agregar_profesor(self, profesor):
        self._profesores.append(profesor)

    def agregar_pago(self, pago):
        self._pagos.append(pago)

    # LISTADOS
    def listar_clientes(self):
        return [c.mostrar_datos() for c in self._clientes]

    def listar_profesores(self):
        return [p.mostrar_datos() for p in self._profesores]

    def listar_pagos(self):
        return [p.mostrar_pago() for p in self._pagos]

    # BÚSQUEDAS
    def buscar_cliente_por_dni(self, dni):
        for cliente in self._clientes:
            if cliente._dni == dni:
                return cliente
        return None

    def buscar_cliente_por_nombre(self, nombre):
        for cliente in self._clientes:
            if cliente._nombre.lower() == nombre.lower():
                return cliente
        return None


# =========================
# MENÚ
# =========================
def menu():
    print("\n===== SISTEMA GIMNASIO =====")
    print("1. Registrar cliente")
    print("2. Registrar profesor")
    print("3. Registrar pago")
    print("4. Ver informacion clientes")
    print("5. Ver informacion profesores")
    print("6. Ver informacion pagos")
    print("7. Salir")


# =========================
# MAIN
# =========================

gimnasio = Gimnasio()
admin = Administrador("Ariel", "Franco", 35123456)

while True:
    menu()
    opcion = input("Seleccione una opción: ")

    # -------------------------
    # CLIENTE
    # -------------------------
    if opcion == "1":
        nombre = input("Ingrese nombre: ")
        apellido = input("Ingrese apellido: ")
        dni = int(input("Ingrese DNI: "))
        nro_socio = int(input("Ingrese número de socio: "))

        admin.registrar_cliente(gimnasio, nombre, apellido, dni, nro_socio)
        print("Cliente registrado correctamente")

    # -------------------------
    # PROFESOR
    # -------------------------
    elif opcion == "2":
        nombre = input("Ingrese nombre: ")
        apellido = input("Ingrese apellido: ")
        dni = int(input("Ingrese DNI: "))
        turno = input("Ingrese turno: ") # CAMBIO: Ingrese turno

        admin.registrar_profesor(gimnasio, nombre, apellido, dni, turno)
        print("Profesor registrado correctamente")

    # -------------------------
    # PAGO (CON BÚSQUEDA)
    # -------------------------
    elif opcion == "3":
        if len(gimnasio._clientes) == 0:
            print("No hay clientes registrados")
            continue

        print("\nBuscar cliente:")
        print("1. Por DNI")
        print("2. Por nombre")

        op = input("Opción: ")

        cliente = None

        if op == "1":
            dni = int(input("Ingrese DNI: "))
            cliente = gimnasio.buscar_cliente_por_dni(dni)

        elif op == "2":
            nombre = input("Ingrese nombre: ")
            cliente = gimnasio.buscar_cliente_por_nombre(nombre)

        if cliente is None:
            print("Cliente no encontrado")
            continue

        monto = float(input("Monto: "))
        fecha = input("Fecha: ")
        metodo = input("Método de pago: ")
        estado = input("Estado (pagado/pendiente): ")

        admin.registrar_pago(gimnasio, cliente, monto, fecha, metodo, estado)
        print("Pago registrado correctamente")

    # -------------------------
    # VER INFO CLIENTES
    # -------------------------
    elif opcion == "4":
        print("\n--- CLIENTES ---")
        for c in gimnasio.listar_clientes():
            print(c)

    # -------------------------
    # VER INFO PROFESORES
    # -------------------------
    elif opcion == "5":
        print("\n--- PROFESORES ---")
        for p in gimnasio.listar_profesores():
            print(p)

    # -------------------------
    # VER INFO PAGOS
    # -------------------------
    elif opcion == "6":
        print("\n--- PAGOS ---")
        for p in gimnasio.listar_pagos():
            print(p)

    # -------------------------
    # SALIR
    # -------------------------
    elif opcion == "7":
        print("Saliendo del sistema...")
        break

    else:
        print("Opción inválida")