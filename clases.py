class Animales():
    def __init__(self, nombre, raza, color,edad,genero):
        self.nombre = nombre
        self.raza = raza
        self.color = color
        self.edad = edad
        self.genero = genero
    def ladrar(self):
        print('El perro ladra')
    def correr(self):
        print('El perro está corriendo')
    def morder(self):
        print('El perro muerde')
    def __str__(self):
        return (f"nombre: {self.nombre} raza: {self.raza} color: {self.color} edad: {self.edad} genero: {self.genero}")
    
perro_1 = Animales('lukas', 'pitbull', 'negro', '4', 'macho')
perro_2 = Animales('Max', 'Pincher', 'blanco', '2', 'macho')
print(perro_1)
print(perro_2)

perro_1.ladrar()
perro_2.morder()


