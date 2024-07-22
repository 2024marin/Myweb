#String
'''saludo1 = "Hola mundo"
saludo2 = "Hola mundo blanco"
nombre = "Mauricio"
print(saludo1, saludo2, nombre) # si se usan comas se separan con espacios 
name = 'CARLA Marcela'
last_name = '   Florida     Roman  '
print(5 * name)
print(name + ' ' + last_name) # cuando se concatena se unen sin espacio
print(len(name))
print(len(last_name))
print(name.lower())
print(name.upper())
print(last_name.strip())
print(name[4:])
print(name *5)
print(len(last_name))
print(len(name))
print(name.lower())
print(name.upper())
print(last_name.strip())
#print(last_name.count("Florida"))'''

'''#Classes
x = 10 
y = 5.678
#z = 1.2E6
#a = 1.2E-6
print(type(x))
print(type(y))
#print(z)
#print(a)
print(x + x)
print(x + y)
print(y + y)
is_true = True
is_false = False
print(is_true)
print(type(is_true))'''

'''print("Nunca", "pares", "de", "aprender", sep=", " )
print("Nunca" , end=" ") # Permite crear texto horizontla sinque comeince una nueva linea
print("pares de aprender", end=" ") 
print("Python, es lo mejor")
frase = "Nunca pares de aprender" 
author = "Platzi" 
print(f"La frase Frase: {frase}, Autor: {author}")

valor = 3.14159
print("Valor: {:.5f}".format(valor)) # :.xf muestra los decimales que se quieren imprimir
Euler = 2.84278284
print("Valor euler:\n{:.3f}".format(Euler))
print('Hola soy \'Carli\'')
print("Hola\nmundo") #\n hace saltos de linea que se est '''

'''
a = 10
b = 3
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)
print(a == b)
print(a != b)
print(a % b, end=" ")
print(a / b, end=" ")
print(a // b)'''



'''a = 10
b = 10
print("Suma:", a + b)
print("Resta:", a - b)
print("Multiplicación:", a * b)
print("Potenciación:", a ** b)
print("División:", a / b)
print("Parte entera de la división:", a // b)
print("Módulo:", a % b)
a /= 2
print(a)
operation_1  = 2 + 3 * 4
operation_2  = (2 + 3) * 4
print(operation_1)
print(operation_2)
operation_3 = (2+3) * (4**2)/ 8 - 1
print(operation_3)'''
   
"""
name = input("Ingrese su nombre: ") # entrada de datos
print(name)
print(type(name))
age = int(input("Ingrese su edad: ")) #entraada de datos

print(type(age))"""

"""
to_do = ["Dirigirnos al hotel",
         "Ir a almorzar",
         "Visitar un museo",
         "Volver al hotel"]
print(to_do)
numbers = [1,2,3,4, "cinco"] #lista[]
print(type(numbers))
mix = ["uno", 2, 3.14, True, [1,2,3]] #lista
print(mix)
print(len(mix))
print("Primer elemento", mix[0])
print("Segundo elemento", mix[1])
print("Ultimo elemento:", mix[-1])
string = "Hola mundo"
print("Primer elemento", string[0])
print("Segundo elemento", string[1])
print("Ultimo elemento:", string[-1])
print(mix[2:-2])
print(mix)
mix.append(False)
print(mix)
mix.append(["a","b"])
print(mix)
mix.insert(1,["a","b"])
print(mix)
print(mix.index(["a","b"]))
numbers = [1,2,100.01,90.45,3,4, 5]
print(numbers)
print("Mayor:",max(numbers)) #Mayor, 
print("Menor:",min(numbers)) #Menor,
del numbers[-1] # indica que se puedden eliminar
print(numbers)
del numbers[:2]
print(numbers)
del numbers"""

"""a = [1,2,3,4,5]
b = a
print(a)
print(b)
del a[0]
print(id(a))
print(id(b))
c = a[:]
print(id(a))
print(id(b))
print(id(c))
a.append(6)# añaidr primero va mi variable
print(a)
print(b)
print(c)
"""

"""matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]
print(matrix[2][1])
print(matrix[0])
numbers = 1,2,3,4,5
print(numbers)
print(type(numbers))
print(numbers[0])
#numbers[0] = 'unos'
#print(numbers)"""

"""chess_board = [
    ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
    ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
    ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
]

print(chess_board)"""

"""
# dict
numbers = {1:"uno", 2:"dos", 3:"tres"}
print(numbers[2])
information = {"nombre": "Carla",
               "Apellido": "Florida",
               "Altura": 1.60,
               "Edad": 29}
print(information)
del information["Edad"] # del information
print(information)
claves = information.keys()
print(claves)
#print(type(claves))
values = information.values()
print(values)
pairs = information.items()
print(pairs)
contacts = {"Carla": {"Apellido": "Florida",
               "Altura": 1.60,
               "Edad": 29},
                "Diego": {"Apellido": "Antezana",
               "Altura": 1.80,
               "Edad": 32},
                "Eduardo": {"Apellido": "Martinez",
               "Altura": 1.75,
               "Edad": 35}}

print(contacts)
print(contacts["Carla"])"""

'''is_member = True
age = 11

if is_member:
    if age>=15:
        print("Tienes acceso ya que eres miembro y mayor o igual a 15 años")
    else:
        print("No tienes acceso ya que eres miembro pero menor a 15 años")
else:
    print("No eres miembro y NO TIENES ACCESO")'''


'''x = 3
if x > 5: #
    print("X es mayor que 5")
elif x == 5: # 
    print("X es igual que 5")
else: # solo se puede uno
    print("X es menor que 5")
print("afuera")'''


'''x = 15
y = 20

if x>10 and y>25: #evaluamos dos 
    print("X es mayor que 10 y Y es mayor que 15")

if x>10 or y>25: #para que una se cumpla
    print("X es mayor que 10 O Y es Mayor que 25")

if not x>10: #
    print("X no es mayor que 10")'''

#Bucles

numbers = [1, 2, 3, 4, 5, 6]
for i in numbers:
    print("Aquí i es igual a:",i+1)

for i in range(3,10):
    print(i)



fruits = ["Manzana", "Pera", "Uva", "Naranja", "Tomate"]
for fruit in fruits: #por cada fruta que este almacenada en la coleccion frutas si
    print(fruit)
    if fruit == "lulo":
        print("lulo encontrada")
    elif fruit != "Lulo":
        print("fruta desconocida")


x = 0 #minetras se cumpla una condicion entranos en while, mientras
while x<15: #mientras x sea menor que cinco
    if x ==3 :
        break
    print(x) 
    x +=1
    

 




















