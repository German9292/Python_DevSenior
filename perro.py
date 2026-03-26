"""Requisitos del ejercicio:
Crear una clase llamada Perro.
Definir tres atributos con diferentes niveles de acceso:
nombre → Público (se puede acceder directamente).
_raza → Protegido (acceso limitado, no recomendado fuera de la clase).
__edad → Privado (solo accesible mediante métodos).
Implementar:
Un getter para obtener la edad.
Un setter para modificar la edad, validando que no sea negativa.
Un método mostrar_info() que muestre todos los datos del perro.
Probar el sistema creando un objeto, mostrando su información y validando el uso de getters y setters."""

class Perro():
    def __init__(self, nombre, raza, edad):
        self.nombre = nombre
        self._raza = raza
        self.__edad = edad

    def get_nombre(self):
        return self.nombre

    def get_raza(self):
        return self._raza

    def get_edad(self):
        return self.__edad

    # Setters
    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_raza(self, raza):
        self._raza = raza

    def set_edad(self, edad):
        self.__edad = edad

    def mostrar_info(self):
        print("Nombre:", self.get_nombre())
        print("Raza:", self.get_raza())
        print("Edad:", self.get_edad())

def main():
    perro1 = Perro("Max", "Labrador", 5)
    perro2 = Perro("Lukas", "Pilbull", 2)
    
    perro1.mostrar_info()
    perro1.set_edad(6)
    perro2.mostrar_info()
    
    print("Nueva edad del perro 1:", perro1.get_edad())
    perro1.mostrar_info()


if __name__ == "__main__":
    main()