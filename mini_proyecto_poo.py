"""Vas a crear una clase llamada CuentaBancaria que simule una billetera digital como Nequi o Daviplata.

🔹 Requisitos
1. Atributos

Debes usar los tres niveles de acceso:

titular → Público
_historial → Protegido
__saldo → Privado
2. Constructor

Debe recibir:

titular
saldo inicial
3. Métodos obligatorios
🔹 Getters y Setters
Obtener saldo (NO acceso directo)
Modificar saldo SOLO con validación
🔹 Funcionalidades
depositar(monto)
retirar(monto)
ver_saldo()
ver_historial()
4. Validaciones
No permitir saldo negativo
No permitir retiros mayores al saldo
No permitir depósitos negativos
5. Prueba del sistema

En el programa principal:

Crear una cuenta
Depositar dinero
Retirar dinero
Mostrar saldo
Mostrar historial"""

class Cuenta_Bancaria:
    def __init__(self, titular, saldo_inicial):
        self.titular = titular
        self._historial = []
        self.__saldo = 0
        self.depositar(saldo_inicial)
    # self._historial.append(f"Cuenta creada con saldo inicial de: {saldo_inicial}")
    
    def get_saldo(self):
        return self.__saldo
    
    def set_saldo(self, nuevo_saldo):
        if nuevo_saldo < 0:
            print('El saldo no puede ser negativo')
        else:
            self.__saldo = nuevo_saldo
            self._historial.append(f"Saldo actualizado a:  {nuevo_saldo}")

    def depositar(self, monto):
        if monto <= 0:
            print('El monto depositado debe ser mayor a 0.')
            return
        self.__saldo += monto
        self._historial.append(f"Deposito: {monto}")

    def retirar(self, monto):
        if monto <= 0:
            print('El monto a retirar debe ser mayor a 0.')
            return
        self.__saldo -= monto
        self._historial.append(f"Retiro: {monto}")

    def ver_saldo(self):
        print(f"Saldo actual: {self.__saldo}")
    
    def  ver_historial(self):
        print("Historial de transacciones:")
        for transaccion in self._historial:
            print(transaccion)

def main():
# Crear una cuenta
    cuenta = Cuenta_Bancaria("Fabian", 100000)
# Depositar dinero
    cuenta.depositar(70000)
# Retirar dinero
    cuenta.retirar(30000)
    print(f"esta es la cuenta de {cuenta.titular} y su saldo es: {cuenta.get_saldo()}")
# Mostrar saldo
    cuenta.ver_saldo()
# Mostrar historial
    cuenta.ver_historial()
if __name__ == "__main__":    main()