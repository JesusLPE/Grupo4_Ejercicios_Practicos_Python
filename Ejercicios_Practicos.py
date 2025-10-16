━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
EJERCICIO 1 [BÁSICO]: TAD Punto2D
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ENUNCIADO:
Implementar un TAD Punto2D que represente un punto en el plano cartesiano 
con coordenadas (x, y). Debe incluir operaciones para calcular la distancia 
al origen y la distancia entre dos puntos.

🔹 PSEUDOCÓDIGO:
   TAD Punto2D
      - Atributos: x, y (números reales)
      - Operaciones:
         * crear(x, y) → Punto2D
         * distanciaOrigen() → real
         * distanciaA(otroPunto) → real

Código:
import math
class Punto2D:

    #Representa un punto en el plano (x, y)
    def __init__(self, x: float, y: float):
        #Crea un punto con coordenadas (x, y)
        self.x = x
        self.y = y

    def distancia_origen(self) -> float:
        #Retorna la distancia al origen (0, 0)
        return math.sqrt(self.x**2 + self.y**2)

    def distancia_a(self, otro_punto: 'Punto2D') -> float:
        #Retorna la distancia entre dos puntos
        dx = self.x - otro_punto.x
        dy = self.y - otro_punto.y
        return math.sqrt(dx**2 + dy**2)

    def __str__(self):
        #Muestra el punto en formato (x, y)
        return f"({self.x}, {self.y})"
       
#Ejemplo de uso:
if __name__ == "__main__":
    p1 = Punto2D(3, 4)
    p2 = Punto2D(0, 0)
   
    print(f"Punto 1: {p1}")
    print(f"Punto 2: {p2}")
    print(f"Distancia de {p1} al origen: {p1.distancia_origen():.2f}")
    print(f"Distancia entre {p1} y {p2}: {p1.distancia_a(p2):.2f}")

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
EJERCICIO 2 [BÁSICO]: TAD Rectangulo
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ENUNCIADO:
Crear un TAD Rectangulo con base y altura. Implementar operaciones para 
calcular área, perímetro y verificar si es un cuadrado.

🔹 PSEUDOCÓDIGO:
   TAD Rectangulo
      - Atributos: base, altura (números reales positivos)
      - Operaciones:
         * crear(base, altura) → Rectangulo
         * calcularArea() → real
         * calcularPerimetro() → real
         * esCuadrado() → booleano

Código:
class Rectangulo:
    
# Precondición: base y altura deben ser números reales positivos.
    def _init_(self, base: float, altura: float):
        if base <= 0 or altura <= 0:
            raise ValueError("La base y la altura deben ser mayores que cero.")
        self._base = base
        self._altura = altura

#Postcondición: retorna un valor >= 0
    def calcular_area(self) -> float:
        return self._base * self._altura

    def calcular_perimetro(self) -> float:
        return 2 * (self._base + self._altura)
    
# Verificar si es cuadrado, verdadero o falso  
    def es_cuadrado(self) -> bool:
        return self._base == self._altura

# Texto del rectángulo
    def _str_(self):
        return f"Rectángulo(base={self._base}, altura={self._altura})"

#Ejemplo
rect1 = Rectangulo (10,5) 
rect2 = Rectangulo(6,6)

print(rect1)
print(f"Área: {rect1.calcular_area()}")
print(f"Perímetro: {rect1.calcular_perimetro()}")
print(f"¿Es cuadrado? {rect1.es_cuadrado()}")

print("\n", rect2)
print(f"Área: {rect2.calcular_area()}")
print(f"Perímetro: {rect2.calcular_perimetro()}")
print(f"¿Es cuadrado? {rect2.es_cuadrado()}")

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
EJERCICIO 3 [INTERMEDIO]: TAD Fraccion con Sobrecarga de Operadores
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ENUNCIADO:
Implementar un TAD Fraccion con numerador y denominador. Sobrecargar los 
operadores +, -, *, / para operar entre fracciones. Incluir método para 
simplificar la fracción.

🔹 PSEUDOCÓDIGO:
   TAD Fraccion
      - Atributos: numerador, denominador (enteros)
      - Invariante: denominador ≠ 0
      - Operaciones:
         * crear(num, den) → Fraccion
         * sumar(otraFraccion) → Fraccion
         * restar(otraFraccion) → Fraccion
         * multiplicar(otraFraccion) → Fraccion
         * dividir(otraFraccion) → Fraccion
         * simplificar() → Fraccion



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
EJERCICIO 4 [INTERMEDIO]: TAD CuentaBancaria
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ENUNCIADO:
Implementar un TAD CuentaBancaria con número de cuenta, titular y saldo.
Incluir operaciones para depositar, retirar y consultar saldo. Validar que
no se pueda retirar más del saldo disponible.

🔹 PSEUDOCÓDIGO:
   TAD CuentaBancaria
      - Atributos: numeroCuenta, titular, saldo
      - Invariante: saldo >= 0
      - Operaciones:
         * crear(numero, titular, saldoInicial) → CuentaBancaria
         * depositar(monto) → void
         * retirar(monto) → booleano
         * consultarSaldo() → real
         * obtenerTitular() → cadena


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
EJERCICIO 5 [INTERMEDIO]: TAD Conjunto
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ENUNCIADO:
Crear un TAD Conjunto que represente un conjunto matemático (sin elementos
duplicados). Implementar operaciones de unión, intersección y diferencia.

🔹 PSEUDOCÓDIGO:
   TAD Conjunto
      - Atributos: elementos (colección sin duplicados)
      - Operaciones:
         * crear() → Conjunto
         * agregar(elemento) → void
         * eliminar(elemento) → booleano
         * contiene(elemento) → booleano
         * tamaño() → entero
         * union(otroConjunto) → Conjunto
         * interseccion(otroConjunto) → Conjunto
         * diferencia(otroConjunto) → Conjunto

Código:
class Conjunto:
    def __init__(self):
        self.elementos = set()  
    def agregar(self, elemento):
        self.elementos.add(elemento)

    def eliminar(self, elemento):
        if elemento in self.elementos:
            self.elementos.remove(elemento)
            return True
        return False

    def contiene(self, elemento):
        return elemento in self.elementos

    def tamaño(self):
        return len(self.elementos)

    def union(self, otroConjunto):
        resultado = Conjunto()
        resultado.elementos = self.elementos.union(otroConjunto.elementos)
        return resultado

    def interseccion(self, otroConjunto):
        resultado = Conjunto()
        resultado.elementos = self.elementos.intersection(otroConjunto.elementos)
        return resultado

    def diferencia(self, otroConjunto):
        resultado = Conjunto()
        resultado.elementos = self.elementos.difference(otroConjunto.elementos)
        return resultado

    def __str__(self):
        return f"{self.elementos}"

A = Conjunto()
B = Conjunto()
A.agregar(1)
A.agregar(2)
A.agregar(3)
B.agregar(3)
B.agregar(4)
print("A =", A)
print("B =", B)
print("Unión =", A.union(B))
print("Intersección =", A.interseccion(B))
print("Diferencia =", A.diferencia(B))

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
EJERCICIO 6 [INTERMEDIO]: TAD Fecha
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ENUNCIADO:
Implementar un TAD Fecha con día, mes y año. Validar que la fecha sea válida
(considerar años bisiestos). Implementar operación para calcular días entre
dos fechas y verificar si una fecha es anterior a otra.

🔹 PSEUDOCÓDIGO:
   TAD Fecha
      - Atributos: dia, mes, año (enteros)
      - Invariante: fecha válida según calendario gregoriano
      - Operaciones:
         * crear(dia, mes, año) → Fecha
         * esValida() → booleano
         * esBisiesto() → booleano
         * esAnterior(otraFecha) → booleano
         * diasEntre(otraFecha) → entero

Código:
from datetime import date
class Fecha:

    #Representa una fecha (día, mes, año)
    def __init__(self, dia: int, mes: int, anio: int):
        #Crea una nueva fecha
        self.dia = dia
        self.mes = mes
        self.anio = anio
        if not self.es_valida():
            raise ValueError("Fecha inválida según el calendario gregoriano")

    def es_bisiesto(self) -> bool:
        #Retorna True si el año es bisiesto
        return (self.anio % 4 == 0 and self.anio % 100 != 0) or (self.anio % 400 == 0)

    def es_valida(self) -> bool:
        #Verifica si la fecha existe
        try:
            date(self.anio, self.mes, self.dia)
            return True
        except ValueError:
            return False

    def es_anterior(self, otra: 'Fecha') -> bool:
        #Retorna True si esta fecha es anterior a otra
        return date(self.anio, self.mes, self.dia) < date(otra.anio, otra.mes, otra.dia)

    def dias_entre(self, otra: 'Fecha') -> int:
        #Calcula los días entre dos fechas
        f1 = date(self.anio, self.mes, self.dia)
        f2 = date(otra.anio, otra.mes, otra.dia)
        return abs((f1 - f2).days)

    def __str__(self):
        #Muestra la fecha en formato dd/mm/aaaa
        return f"{self.dia:02d}/{self.mes:02d}/{self.anio}"

#Ejemplo de uso:

if __name__ == "__main__":
    f1 = Fecha(12, 10, 2025)
    f2 = Fecha(1, 1, 2024)

    print(f"Fecha 1: {f1}")
    print(f"Fecha 2: {f2}")
    print(f"¿{f1.anio} es bisiesto? → {f1.es_bisiesto()}")
    print(f"¿{f2.anio} es bisiesto? → {f2.es_bisiesto()}")
    print(f"¿{f2} es anterior a {f1}? → {f2.es_anterior(f1)}")
    print(f"Días entre {f1} y {f2}: {f1.dias_entre(f2)} días")

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
EJERCICIO 7 [BÁSICO]: Análisis de Búsqueda Lineal
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ENUNCIADO:
Analizar la complejidad temporal y espacial del siguiente algoritmo de
búsqueda lineal. Determinar el mejor caso, caso promedio y peor caso.

🔹 PSEUDOCÓDIGO:
   Función busquedaLineal(lista, elemento):
       Para i desde 0 hasta longitud(lista) - 1:
           Si lista[i] == elemento:
               Retornar i
       Retornar -1

Código:
def busqueda_lineal(lista, elemento):
  # Realiza una búsqueda lineal en una lista, retorna el índice del elemento si se encuentra, o -1 si no está.

    for i in range(len(lista)):
        if lista[i] == elemento:
            return i
    return -1

# Ejemplo 
lista = [3, 8, 5, 2, 9]
elemento = 2

resultado = busqueda_lineal(lista, elemento)

if resultado != -1:
    print(f" El elemento {elemento} se encuentra en la posición {resultado}.")
else:
    print(f"El elemento {elemento} no está en la lista.")

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
EJERCICIO 8 [BÁSICO]: Análisis de Suma de Elementos
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ENUNCIADO:
Analizar la complejidad del siguiente algoritmo que suma todos los elementos
de una lista.

🔹 PSEUDOCÓDIGO:
   Función sumaElementos(lista):
       suma ← 0
       Para cada elemento en lista:
           suma ← suma + elemento
       Retornar suma

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
EJERCICIO 9 [BÁSICO]: Comparar Complejidades
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ENUNCIADO:
Ordenar las siguientes complejidades de menor a mayor eficiencia:
O(n²), O(1), O(log n), O(n log n), O(2ⁿ), O(n), O(n³)

Además, indicar cuál sería preferible para un dataset de 1 millón de elementos.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
EJERCICIO 10 [INTERMEDIO]: Análisis de Bucles Anidados
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ENUNCIADO:
Analizar la complejidad temporal del siguiente código con bucles anidados:

🔹 PSEUDOCÓDIGO:
   Función buscarDuplicados(lista):
       Para i desde 0 hasta longitud(lista) - 1:
           Para j desde i + 1 hasta longitud(lista) - 1:
               Si lista[i] == lista[j]:
                   Retornar Verdadero
       Retornar Falso

Código:
def buscar_duplicados(lista):
    """
    Busca elementos duplicados en una lista
    """
    n = len(lista)
    for i in range(n):
        for j in range(i + 1, n):
            if lista[i] == lista[j]:
                return True
    return False

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
EJERCICIO 11 [INTERMEDIO]: Búsqueda Binaria
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ENUNCIADO:
Analizar la complejidad del algoritmo de búsqueda binaria. Explicar por qué
es O(log n) y en qué casos es más eficiente que la búsqueda lineal.

🔹 PSEUDOCÓDIGO:
   Función busquedaBinaria(listaOrdenada, elemento):
       izq ← 0
       der ← longitud(listaOrdenada) - 1
       
       Mientras izq <= der:
           medio ← (izq + der) / 2
           Si listaOrdenada[medio] == elemento:
               Retornar medio
           SiNo Si listaOrdenada[medio] < elemento:
               izq ← medio + 1
           SiNo:
               der ← medio - 1
       
       Retornar -1

Código:
class BusquedaBinaria:

    # TAD que realiza una búsqueda binaria en una lista ordenada
    def __init__(self, lista):
        # Inicializa la lista ordenada
        self.lista = lista

    def buscar(self, elemento):
        # Busca un elemento en la lista
        izq = 0
        der = len(self.lista) - 1
        while izq <= der:
            medio = (izq + der) // 2  # Calcula el punto medio
            if self.lista[medio] == elemento:
                return medio
            elif self.lista[medio] < elemento:
                izq = medio + 1
            else:
                der = medio - 1
        return -1  # No encontrado

    def __str__(self):
        # Muestra la lista contenida
        return f"Lista: {self.lista}"

#ejemplo de uso
if __name__ == "__main__":
    datos = [2, 4, 6, 8, 10, 12, 14, 16, 18]
    buscador = BusquedaBinaria(datos)

    print(buscador)
    
    elemento = 10
    resultado = buscador.buscar(elemento)
    if resultado != -1:
        print(f"Elemento {elemento} encontrado en la posición {resultado}.")
    else:
        print(f"Elemento {elemento} no encontrado en la lista.")

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
EJERCICIO 12 [INTERMEDIO]: Complejidad con Estructuras de Datos
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ENUNCIADO:
Comparar la complejidad de las siguientes operaciones en listas vs diccionarios
en Python:
- Buscar un elemento
- Insertar un elemento
- Eliminar un elemento

Indicar cuándo conviene usar cada estructura de datos.

Código:
def comparar_complejidad():
 
    print("=== COMPLEJIDAD DE OPERACIONES ===\n")

    print(" LISTAS:")
    print("- Buscar un elemento: O(n) → depende del tamaño de la lista.")
    print("- Insertar un elemento al final: O(1) promedio.")
    print("- Insertar en posición específica o eliminar: O(n) (se deben mover elementos).")

    print("\n DICCIONARIOS:")
    print("- Buscar una clave: O(1) promedio (usa tabla hash).")
    print("- Insertar una clave-valor: O(1) promedio.")
    print("- Eliminar una clave: O(1) promedio.")

    print("\n Cuándo usar cada estructura:")
    print("- Usa LISTA cuando necesitas mantener un orden secuencial de elementos o duplicados.")
    print("- Usa DICCIONARIO cuando necesitas búsquedas rápidas por clave y acceso directo.")
    print("- En general, los diccionarios son más eficientes en búsqueda e inserción.")

#  Ejemplo 
comparar_complejidad()

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
EJERCICIO 13 [INTERMEDIO]: Análisis de Algoritmo Recursivo
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ENUNCIADO:
Analizar la complejidad temporal y espacial del algoritmo factorial recursivo.
Comparar con la versión iterativa.

🔹 PSEUDOCÓDIGO:
   Función factorialRecursivo(n):
       Si n <= 1:
           Retornar 1
       SiNo:
           Retornar n * factorialRecursivo(n - 1)



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
EJERCICIO 14 [BÁSICO]: Implementación Básica de Pila
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ENUNCIADO:
Implementar una clase Pila con las operaciones básicas: push (apilar),
pop (desapilar), peek (ver tope), isEmpty (verificar si está vacía) y
size (obtener tamaño).

🔹 PSEUDOCÓDIGO:
   TAD Pila:
       - Atributos: elementos (lista)
       
       Operaciones:
       * push(elemento) → void
           agregar elemento al tope
       
       * pop() → elemento
           Precondición: pila no vacía
           eliminar y retornar elemento del tope
       
       * peek() → elemento
           Precondición: pila no vacía
           retornar elemento del tope sin eliminarlo
       
       * isEmpty() → booleano
           retornar verdadero si pila vacía
       
       * size() → entero
           retornar cantidad de elementos



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
EJERCICIO 15 [BÁSICO]: Invertir una Cadena
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ENUNCIADO:
Usar una pila para invertir una cadena de texto. Por ejemplo, "HOLA" debe
convertirse en "ALOH".

🔹 PSEUDOCÓDIGO:
   Función invertirCadena(texto):
       pila ← nueva Pila()
       
       Para cada caracter en texto:
           pila.push(caracter)
       
       resultado ← ""
       Mientras NO pila.isEmpty():
           resultado ← resultado + pila.pop()
       
       Retornar resultado

Código:
class Pila:
    def __init__(self):
        self.items = []
    def push(self, elemento):
        self.items.append(elemento)
    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        return None
    def isEmpty(self):
        return len(self.items) == 0
def invertirCadena(texto):
    pila = Pila()
    for caracter in texto:
        pila.push(caracter)
    resultado = ""
    while not pila.isEmpty():
        resultado += pila.pop()
    return resultado
cadena = "HOLA"
print("Original:", cadena)
print("Invertida:", invertirCadena(cadena))

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
EJERCICIO 16 [BÁSICO]: Validar Paréntesis Balanceados
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ENUNCIADO:
Implementar una función que verifique si una expresión tiene los paréntesis
correctamente balanceados usando una pila.
Ejemplos:
- "(())" → Verdadero
- "(()" → Falso
- ")(" → Falso

🔹 PSEUDOCÓDIGO:
   Función validarParentesis(expresion):
       pila ← nueva Pila()
       
       Para cada caracter en expresion:
           Si caracter == '(':
               pila.push(caracter)
           SiNo Si caracter == ')':
               Si pila.isEmpty():
                   Retornar Falso
               pila.pop()
       
       Retornar pila.isEmpty()

Código:
class Pila:

    #almacena elementos con regla LIFO
    def __init__(self):
        #Crea una pila vacía
        self.elementos = []

    def push(self, elemento):
        #Agrega un elemento al tope
        self.elementos.append(elemento)

    def pop(self):
        #Quita y devuelve el tope
        if not self.esta_vacia():
            return self.elementos.pop()
        else:
            raise IndexError("❌ La pila está vacía")

    def esta_vacia(self) -> bool:
        # Retorna True si la pila está vacía
        return len(self.elementos) == 0

#validar paréntesis balanceados
def validar_parentesis(expresion: str) -> bool:
    #Verifica si los paréntesis están balanceados
    pila = Pila()
    for caracter in expresion:
        if caracter == '(':
            pila.push(caracter)
        elif caracter == ')':
            if pila.esta_vacia():
                return False
            pila.pop()
    return pila.esta_vacia()

#ejemplo de uso
if __name__ == "__main__":
    ejemplos = ["(())", "(()", ")(", "((()))", "())(()"]
    for exp in ejemplos:
        print(f"Expresión: {exp} → Balanceada: {validar_parentesis(exp)}")

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
EJERCICIO 17 [INTERMEDIO]: Validar Múltiples Tipos de Delimitadores
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ENUNCIADO:
Extender el ejercicio anterior para validar paréntesis (), corchetes [] y
llaves {}. Los delimitadores deben cerrarse en el orden correcto.
Ejemplos:
- "{[()]}" → Verdadero
- "{[(])}" → Falso (orden incorrecto)
- "{[}" → Falso (falta cerrar)

🔹 PSEUDOCÓDIGO:
   Función validarDelimitadores(expresion):
       pila ← nueva Pila()
       aperturas ← {'(', '[', '{'}
       cierres ← {')', ']', '}'}
       pares ← {')': '(', ']': '[', '}': '{'}
       
       Para cada caracter en expresion:
           Si caracter está en aperturas:
               pila.push(caracter)
           SiNo Si caracter está en cierres:
               Si pila.isEmpty():
                   Retornar Falso
               Si pila.pop() != pares[caracter]:
                   Retornar Falso
       
       Retornar pila.isEmpty()

Código:
def validar_delimitadores(expresion):
    pila = []  
    pares = {')': '(', ']': '[', '}': '{'}  # Relación cierre ↔ apertura

    for caracter in expresion:
        # Si es un delimitador de apertura, lo guardamos en la pila
        if caracter in "([{":
            pila.append(caracter)
        # Si es de cierre, comprobamos correspondencia
        elif caracter in ")]}":
            if not pila:  # Si no hay nada que cerrar
                return False
            tope = pila.pop()  # Extrae el último abierto
            if pares[caracter] != tope:  # Si no coincide el tipo
                return False

    # Si al final quedan aperturas sin cerrar
    return not pila

# Ejemplos 
expresiones = ["{[()]}", "([)]", "{{[[(())]]}}", "({[", "[()]{}{[()()]()}"]

for exp in expresiones:
    if validar_delimitadores(exp):
        print(f"{exp} Correcta")
    else:
        print(f"{exp} Incorrecta")

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
EJERCICIO 18 [INTERMEDIO]: Evaluador de Expresiones Postfijas (RPN)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ENUNCIADO:
Implementar un evaluador de expresiones en notación postfija (Reverse Polish
Notation). En RPN, los operadores van después de los operandos.
Ejemplo: "3 4 + 2 *" equivale a (3 + 4) * 2 = 14

🔹 PSEUDOCÓDIGO:
   Función evaluarPostfija(expresion):
       pila ← nueva Pila()
       tokens ← dividir expresion por espacios
       
       Para cada token en tokens:
           Si token es número:
               pila.push(convertir token a número)
           SiNo:  // token es operador
               operando2 ← pila.pop()
               operando1 ← pila.pop()
               resultado ← aplicar operador(operando1, operando2, token)
               pila.push(resultado)
       
       Retornar pila.pop()


           pilaRehacer.push(contenido)
           contenido ← pilaDeshacer.pop()
       
       Función rehacer():
           Si pilaRehacer.isEmpty():
               retornar
           pilaDeshacer.push(contenido)
           contenido ← pilaRehacer.pop()

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
EJERCICIO 19 [INTERMEDIO]: Convertir Infija a Postfija
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ENUNCIADO:
Implementar el algoritmo Shunting Yard para convertir expresiones infijas
(notación normal) a postfijas. Considerar precedencia de operadores y paréntesis.
Ejemplo: "3 + 4 * 2" → "3 4 2 * +"

🔹 PSEUDOCÓDIGO:
   Función infijaAPostfija(expresion):
       salida ← lista vacía
       pila ← nueva Pila()
       precedencia ← {'+': 1, '-': 1, '*': 2, '/': 2}
       
       tokens ← tokenizar(expresion)
       
       Para cada token en tokens:
           Si token es número:
               agregar token a salida
           SiNo Si token es '(':
               pila.push(token)
           SiNo Si token es ')':
               Mientras pila.peek() != '(':
                   agregar pila.pop() a salida
               pila.pop()  // eliminar '('
           SiNo:  // token es operador
               Mientras NO pila.isEmpty() Y 
                        pila.peek() != '(' Y
                        precedencia[pila.peek()] >= precedencia[token]:
                   agregar pila.pop() a salida
               pila.push(token)
       
       Mientras NO pila.isEmpty():
           agregar pila.pop() a salida
       
       Retornar unir salida con espacios

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
EJERCICIO 20 [INTERMEDIO]: Historial de Navegación
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ENUNCIADO:
Implementar un sistema de historial de navegación web usando dos pilas:
una para "atrás" y otra para "adelante". Implementar las funciones:
- visitar(url): visitar nueva página
- atras(): volver a la página anterior
- adelante(): ir a la página siguiente

🔹 PSEUDOCÓDIGO:
   Clase Navegador:
       Atributos:
           pilaAtras ← nueva Pila()
           pilaAdelante ← nueva Pila()
           paginaActual ← null
       
       Función visitar(url):
           Si paginaActual != null:
               pilaAtras.push(paginaActual)
           paginaActual ← url
           limpiar pilaAdelante
       
       Función atras():
           Si pilaAtras.isEmpty():
               error "No hay páginas anteriores"
           pilaAdelante.push(paginaActual)
           paginaActual ← pilaAtras.pop()
       
       Función adelante():
           Si pilaAdelante.isEmpty():
               error "No hay páginas siguientes"
           pilaAtras.push(paginaActual)
           paginaActual ← pilaAdelante.pop()

Código:
class Pila:
    def __init__(self):
        self.items = []
    def push(self, elemento):
        self.items.append(elemento)
    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
    def isEmpty(self):
        return len(self.items) == 0
    def limpiar(self):
        self.items = []
class Navegador:
    def __init__(self):
        self.pilaAtras = Pila()
        self.pilaAdelante = Pila()
        self.paginaActual = None
    def visitar(self, url):
        if self.paginaActual is not None:
            self.pilaAtras.push(self.paginaActual)
        self.paginaActual = url
        self.pilaAdelante.limpiar()
        print(f"Visitando: {self.paginaActual}")
    def atras(self):
        if self.pilaAtras.isEmpty():
            print("Error: No hay páginas anteriores")
            return
        self.pilaAdelante.push(self.paginaActual)
        self.paginaActual = self.pilaAtras.pop()
        print(f"Volviendo atrás a: {self.paginaActual}")
    def adelante(self):
        if self.pilaAdelante.isEmpty():
            print("Error: No hay páginas siguientes")
            return
        self.pilaAtras.push(self.paginaActual)
        self.paginaActual = self.pilaAdelante.pop()
        print(f"Avanzando a: {self.paginaActual}")
nav = Navegador()
nav.visitar("google.com")
nav.visitar("youtube.com")
nav.visitar("wikipedia.org")
nav.atras()
nav.atras()
nav.adelante()

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
EJERCICIO 21 [INTERMEDIO]: Verificar Palíndromos
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ENUNCIADO:
Usar una pila para verificar si una palabra es un palíndromo (se lee igual
de izquierda a derecha que de derecha a izquierda). Ignorar espacios y
mayúsculas/minúsculas.
Ejemplos: "anilina", "radar", "reconocer"

🔹 PSEUDOCÓDIGO:
   Función esPalindromo(texto):
       pila ← nueva Pila()
       textoLimpio ← eliminar espacios y convertir a minúsculas
       
       // Apilar primera mitad
       Para i desde 0 hasta longitud(textoLimpio)/2 - 1:
           pila.push(textoLimpio[i])
       
       // Comparar segunda mitad
       inicio ← Si longitud(textoLimpio) es impar entonces longitud/2 + 1 
                SiNo longitud/2
       
       Para i desde inicio hasta fin:
           Si pila.isEmpty() O textoLimpio[i] != pila.pop():
               Retornar Falso
       
       Retornar Verdadero

Código:
class Pila:

    #almacena elementos con regla LIFO
    def __init__(self):
        #Crea una pila vacía
        self.elementos = []

    def push(self, elemento):
        #Agrega un elemento al tope
        self.elementos.append(elemento)

    def pop(self):
        #Quita y devuelve el elemento superior
        if not self.esta_vacia():
            return self.elementos.pop()
        else:
            raise IndexError("La pila está vacía")

    def esta_vacia(self) -> bool:
        # Retorna True si la pila no tiene elementos
        return len(self.elementos) == 0

#Verificar si una palabra es palíndromo
def es_palindromo(texto: str) -> bool:
    #Verifica si un texto es palíndromo usando una pila
    pila = Pila()
    texto_limpio = texto.replace(" ", "").lower()
    n = len(texto_limpio)

    #Apila la primera mitad
    for i in range(n // 2):
        pila.push(texto_limpio[i])

    #Determina inicio de la segunda mitad
    inicio = (n // 2) + 1 if n % 2 != 0 else n // 2

    #Compara con los desapilados
    for i in range(inicio, n):
        if pila.esta_vacia() or texto_limpio[i] != pila.pop():
            return False
    return pila.esta_vacia()

#Ejemplo de uso
if __name__ == "__main__":
    ejemplos = ["anilina", "radar", "reconocer", "python", "Neuquen", "amor a roma"]
    for palabra in ejemplos:
        print(f"{palabra!r} → Palíndromo: {es_palindromo(palabra)}")

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
EJERCICIO 22 [INTERMEDIO]: Sistema Deshacer/Rehacer (Undo/Redo)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ENUNCIADO:
Implementar un editor de texto simple con funcionalidad de deshacer y rehacer
usando dos pilas. Debe soportar:
- escribir(texto): agregar texto
- deshacer(): deshacer última acción
- rehacer(): rehacer acción deshecha

🔹 PSEUDOCÓDIGO:
   Clase EditorTexto:
       Atributos:
           contenido ← ""
           pilaDeshacer ← nueva Pila()
           pilaRehacer ← nueva Pila()
       
       Función escribir(texto):
           pilaDeshacer.push(contenido)
           contenido ← contenido + texto
           limpiar pilaRehacer
       
       Función deshacer():
           Si pilaDeshacer.isEmpty():
               retornar
           pilaRehacer.push(contenido)
           contenido ← pilaDeshacer.pop()
       
       Función rehacer():
           Si pilaRehacer.isEmpty():
               retornar
           pilaDeshacer.push(contenido)
           contenido ← pilaRehacer.pop()

Código:
class Pila:
    def _init_(self):
        self._elementos = []

    def empujar(self, elemento):
        self._elementos.append(elemento)

    def estallar(self):
        return self._elementos.pop()

    def esta_vacia(self):
        return len(self._elementos) == 0

#Vaciar la pila
    def limpiar(self):
        self._elementos.clear()

class EditorDeTexto:
    #Editor de texto con funciones de deshacer y rehacer
    
    def _init_(self):
        self._contenido = ""
        self._pila_deshacer = Pila()
        self._pila_rehacer = Pila()

    def escribir(self, texto: str):
        # Se agrega texto nuevo al contenido actual.
        
        self._pila_deshacer.empujar(self._contenido)
        self._contenido += texto
        self._pila_rehacer.limpiar()

    def deshacer(self):
       # Deshace la última acción, mueve el estado actual a la pila
    
        if self._pila_deshacer.esta_vacia():
            print(" No hay acciones para deshacer.")
            return
        self._pila_rehacer.empujar(self._contenido)
        self._contenido = self._pila_deshacer.estallar()

    def rehacer(self):
        #Rehace una acción previamente deshecha.

        if self._pila_rehacer.esta_vacia():
            print(" No hay acciones para rehacer.")
            return
        self._pila_deshacer.empujar(self._contenido)
        self._contenido = self._pila_rehacer.estallar()

    def mostrar_contenido(self):
        #Muestra el contenido actual del editor
        print(f" Contenido actual: '{self._contenido}'")

# Ejemplo
editor = EditorDeTexto()

editor.escribir("Hola")
editor.mostrar_contenido()

editor.escribir(" como estás")
editor.mostrar_contenido()

editor.deshacer()
editor.mostrar_contenido()

editor.rehacer()
editor.mostrar_contenido()

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
EJERCICIO 23 [INTERMEDIO]: Torre de Hanoi
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ENUNCIADO:
Implementar el juego de la Torre de Hanoi usando pilas. El problema consiste
en mover n discos de una torre origen a una torre destino usando una torre
auxiliar, con las reglas:
- Solo se puede mover un disco a la vez
- Un disco más grande no puede estar sobre uno más pequeño

🔹 PSEUDOCÓDIGO:
   Función hanoi(n, origen, destino, auxiliar):
       Si n == 1:
           mover disco de origen a destino
           retornar
       
       hanoi(n-1, origen, auxiliar, destino)
       mover disco de origen a destino
       hanoi(n-1, auxiliar, destino, origen)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
EJERCICIO 24 [INTERMEDIO]: Validar Sintaxis HTML Simplificada
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ENUNCIADO:
Usar una pila para verificar si las etiquetas HTML están correctamente
balanceadas y anidadas. Considerar solo etiquetas de apertura <tag> y
cierre </tag>.
Ejemplo válido: "<html><body><h1>Título</h1></body></html>"
Ejemplo inválido: "<html><body></html></body>"

🔹 PSEUDOCÓDIGO:
   Función validarHTML(codigo):
       pila ← nueva Pila()
       etiquetas ← extraer todas las etiquetas del código
       
       Para cada etiqueta en etiquetas:
           Si etiqueta es de apertura:
               pila.push(nombre de etiqueta)
           SiNo:  // etiqueta de cierre
               Si pila.isEmpty():
                   Retornar Falso
               Si pila.pop() != nombre de etiqueta:
                   Retornar Falso
       
       Retornar pila.isEmpty()

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
EJERCICIO 25 [INTERMEDIO]: Pila con Mínimo en O(1)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ENUNCIADO:
Diseñar una pila que además de las operaciones normales (push, pop, peek),
pueda retornar el elemento mínimo en tiempo constante O(1). Implementar:
- push(elemento)
- pop()
- peek()
- getMin() → retorna el mínimo actual en O(1)

🔹 PSEUDOCÓDIGO:
   Clase PilaMinimo:
       Atributos:
           pilaElementos ← nueva Pila()
           pilaMinimos ← nueva Pila()
       
       Función push(elemento):
           pilaElementos.push(elemento)
           
           Si pilaMinimos.isEmpty() O elemento <= pilaMinimos.peek():
               pilaMinimos.push(elemento)
       
       Función pop():
           Si pilaElementos.isEmpty():
               error
           
           elemento ← pilaElementos.pop()
           Si elemento == pilaMinimos.peek():
               pilaMinimos.pop()
           
           Retornar elemento
       
       Función getMin():
           Si pilaMinimos.isEmpty():
               error
           Retornar pilaMinimos.peek()
Código:
class PilaMinimo:
    """
    Pila que mantiene el mínimo en tiempo O(1)
    Usa dos pilas: una para elementos y otra para mínimos
    """
    
    def __init__(self):
        self._elementos = []
        self._minimos = []
    
    def push(self, elemento):
        """Apila elemento y actualiza mínimo si es necesario"""
        self._elementos.append(elemento)
        
        #Si es el primer elemento o es menor/igual al mínimo actual
        if not self._minimos or elemento <= self._minimos[-1]:
            self._minimos.append(elemento)
    
    def pop(self):
        """Desapila elemento y actualiza mínimo si es necesario"""
        if not self._elementos:
            raise IndexError("Pop desde pila vacía")
        
        elemento = self._elementos.pop()
        
        #Si el elemento desapilado era el mínimo, también lo quitamos
        if elemento == self._minimos[-1]:
            self._minimos.pop()
        
        return elemento
    
    def peek(self):
        """Retorna el tope sin desapilar"""
        if not self._elementos:
            raise IndexError("Peek en pila vacía")
        return self._elementos[-1]
    
    def get_min(self):
        """Retorna el mínimo actual en O(1)"""
        if not self._minimos:
            raise IndexError("Pila vacía")
        return self._minimos[-1]
    
    def is_empty(self):
        return len(self._elementos) == 0

# Demostración:
pila = PilaMinimo()
operaciones = [
    ('push', 5),
    ('push', 3),
    ('push', 7),
    ('push', 1),
    ('push', 4),
]
print("Operación\tPila\t\tMínimo")
print("-" * 40)

for op, valor in operaciones:
    pila.push(valor)
    print(f"push({valor})\t\t{pila._elementos}\t{pila.get_min()}")

print("\nDesapilando...")
while not pila.is_empty():
    elemento = pila.pop()
    minimo = pila.get_min() if not pila.is_empty() else "N/A"
    print(f"pop() → {elemento}\t{pila._elementos}\t{minimo}")
