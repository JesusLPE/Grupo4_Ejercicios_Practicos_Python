===============================================================================
           25 EJERCICIOS DE PRÁCTICA - ESTRUCTURA DE DATOS
     Contenidos: TAD, Complejidad Algorítmica y Pilas (Grupos 1-4)
===============================================================================

===============================================================================
SECCIÓN 1: TIPOS ABSTRACTOS DE DATOS (TAD)
Grupos 1 y 2 - Ejercicios 1 al 6
===============================================================================

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
EJERCICIO 1 [BÁSICO]: TAD Punto2D
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📝 ENUNCIADO:
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

✅ EJEMPLO RESUELTO:

```python
import math

class Punto2D:
    """TAD que representa un punto en el plano cartesiano"""
    
    def __init__(self, x: float, y: float):
        """
        Crea un nuevo punto con coordenadas (x, y)
        Precondición: x, y son números reales
        """
        self._x = x
        self._y = y
    
    def distancia_origen(self) -> float:
        """
        Calcula la distancia del punto al origen (0, 0)
        Postcondición: retorna un valor >= 0
        """
        return math.sqrt(self._x**2 + self._y**2)
    
    def distancia_a(self, otro: 'Punto2D') -> float:
        """
        Calcula la distancia entre este punto y otro punto
        Precondición: otro es un Punto2D válido
        Postcondición: retorna un valor >= 0
        """
        dx = self._x - otro._x
        dy = self._y - otro._y
        return math.sqrt(dx**2 + dy**2)
    
    def __str__(self):
        return f"({self._x}, {self._y})"

# Ejemplo de uso:
p1 = Punto2D(3, 4)
p2 = Punto2D(0, 0)

print(f"Punto 1: {p1}")
print(f"Distancia al origen: {p1.distancia_origen()}")  # 5.0
print(f"Distancia entre puntos: {p1.distancia_a(p2)}")  # 5.0
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
EJERCICIO 2 [BÁSICO]: TAD Rectangulo
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📝 ENUNCIADO:
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

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
EJERCICIO 3 [INTERMEDIO]: TAD Fraccion con Sobrecarga de Operadores
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📝 ENUNCIADO:
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

✅ EJEMPLO RESUELTO:

```python
from math import gcd

class Fraccion:
    """TAD que representa una fracción matemática"""
    
    def __init__(self, numerador: int, denominador: int):
        """
        Crea una fracción num/den
        Precondición: denominador != 0
        """
        if denominador == 0:
            raise ValueError("El denominador no puede ser cero")
        self._numerador = numerador
        self._denominador = denominador
        self._simplificar()
    
    def _simplificar(self):
        """Simplifica la fracción usando el MCD"""
        mcd = gcd(abs(self._numerador), abs(self._denominador))
        self._numerador //= mcd
        self._denominador //= mcd
        # Mantener el signo en el numerador
        if self._denominador < 0:
            self._numerador = -self._numerador
            self._denominador = -self._denominador
    
    def __add__(self, otra: 'Fraccion') -> 'Fraccion':
        """Suma dos fracciones: a/b + c/d = (a*d + b*c)/(b*d)"""
        num = self._numerador * otra._denominador + self._denominador * otra._numerador
        den = self._denominador * otra._denominador
        return Fraccion(num, den)
    
    def __sub__(self, otra: 'Fraccion') -> 'Fraccion':
        """Resta dos fracciones"""
        num = self._numerador * otra._denominador - self._denominador * otra._numerador
        den = self._denominador * otra._denominador
        return Fraccion(num, den)
    
    def __mul__(self, otra: 'Fraccion') -> 'Fraccion':
        """Multiplica dos fracciones: (a/b) * (c/d) = (a*c)/(b*d)"""
        return Fraccion(self._numerador * otra._numerador, 
                       self._denominador * otra._denominador)
    
    def __truediv__(self, otra: 'Fraccion') -> 'Fraccion':
        """Divide dos fracciones: (a/b) / (c/d) = (a*d)/(b*c)"""
        return Fraccion(self._numerador * otra._denominador, 
                       self._denominador * otra._numerador)
    
    def __str__(self):
        return f"{self._numerador}/{self._denominador}"

# Ejemplo de uso:
f1 = Fraccion(1, 2)
f2 = Fraccion(1, 3)

print(f"{f1} + {f2} = {f1 + f2}")  # 1/2 + 1/3 = 5/6
print(f"{f1} * {f2} = {f1 * f2}")  # 1/2 * 1/3 = 1/6
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
EJERCICIO 4 [INTERMEDIO]: TAD CuentaBancaria
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📝 ENUNCIADO:
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

📝 ENUNCIADO:
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

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
EJERCICIO 6 [INTERMEDIO]: TAD Fecha
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📝 ENUNCIADO:
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


===============================================================================
SECCIÓN 2: ANÁLISIS DE COMPLEJIDAD ALGORÍTMICA
Grupo 3 - Ejercicios 7 al 13
===============================================================================

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
EJERCICIO 7 [BÁSICO]: Análisis de Búsqueda Lineal
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📝 ENUNCIADO:
Analizar la complejidad temporal y espacial del siguiente algoritmo de
búsqueda lineal. Determinar el mejor caso, caso promedio y peor caso.

🔹 PSEUDOCÓDIGO:
   Función busquedaLineal(lista, elemento):
       Para i desde 0 hasta longitud(lista) - 1:
           Si lista[i] == elemento:
               Retornar i
       Retornar -1

✅ EJEMPLO RESUELTO:

```python
def busqueda_lineal(lista, elemento):
    """
    Busca un elemento en una lista de forma secuencial
    """
    for i in range(len(lista)):
        if lista[i] == elemento:
            return i
    return -1

# ANÁLISIS DE COMPLEJIDAD:

"""
COMPLEJIDAD TEMPORAL:
- Mejor caso: O(1) - El elemento está en la primera posición
- Caso promedio: O(n/2) = O(n) - El elemento está en alguna posición intermedia
- Peor caso: O(n) - El elemento no está o está en la última posición

EXPLICACIÓN:
En el peor caso, debemos recorrer todos los n elementos de la lista.
Cada iteración realiza una comparación (operación constante O(1)).
Por lo tanto, n iteraciones × O(1) = O(n)

COMPLEJIDAD ESPACIAL:
O(1) - Solo usamos variables auxiliares (i) independientes del tamaño de entrada

JUSTIFICACIÓN MATEMÁTICA:
Sea n = longitud(lista)
T(n) = 1 + 1 + 1 + ... + 1 (n veces) = n
Por lo tanto, T(n) = O(n)
"""

# Ejemplo de medición:
import time

lista_grande = list(range(100000))

# Mejor caso:
inicio = time.time()
busqueda_lineal(lista_grande, 0)
print(f"Mejor caso: {time.time() - inicio:.6f} segundos")

# Peor caso:
inicio = time.time()
busqueda_lineal(lista_grande, 99999)
print(f"Peor caso: {time.time() - inicio:.6f} segundos")
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
EJERCICIO 8 [BÁSICO]: Análisis de Suma de Elementos
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📝 ENUNCIADO:
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

📝 ENUNCIADO:
Ordenar las siguientes complejidades de menor a mayor eficiencia:
O(n²), O(1), O(log n), O(n log n), O(2ⁿ), O(n), O(n³)

Además, indicar cuál sería preferible para un dataset de 1 millón de elementos.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
EJERCICIO 10 [INTERMEDIO]: Análisis de Bucles Anidados
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📝 ENUNCIADO:
Analizar la complejidad temporal del siguiente código con bucles anidados:

🔹 PSEUDOCÓDIGO:
   Función buscarDuplicados(lista):
       Para i desde 0 hasta longitud(lista) - 1:
           Para j desde i + 1 hasta longitud(lista) - 1:
               Si lista[i] == lista[j]:
                   Retornar Verdadero
       Retornar Falso

✅ EJEMPLO RESUELTO:

```python
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

# ANÁLISIS DE COMPLEJIDAD:

"""
COMPLEJIDAD TEMPORAL:

Análisis del bucle externo:
- Se ejecuta n veces (donde n = len(lista))

Análisis del bucle interno:
- Primera iteración (i=0): se ejecuta n-1 veces
- Segunda iteración (i=1): se ejecuta n-2 veces
- Tercera iteración (i=2): se ejecuta n-3 veces
- ...
- Última iteración (i=n-2): se ejecuta 1 vez

Total de comparaciones:
(n-1) + (n-2) + (n-3) + ... + 1 = n(n-1)/2

Aplicando notación Big O:
T(n) = n(n-1)/2 = (n² - n)/2
T(n) = O(n²)

MEJOR CASO: O(1) - Si encuentra duplicados en las primeras posiciones
PEOR CASO: O(n²) - Si no hay duplicados o están al final

COMPLEJIDAD ESPACIAL:
O(1) - Solo usa variables i, j independientes del tamaño de entrada
"""

# Comparación con solución más eficiente:
def buscar_duplicados_optimizado(lista):
    """Versión O(n) usando conjunto"""
    vistos = set()
    for elemento in lista:
        if elemento in vistos:
            return True
        vistos.add(elemento)
    return False

# Esta versión es O(n) temporal pero O(n) espacial
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
EJERCICIO 11 [INTERMEDIO]: Búsqueda Binaria
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📝 ENUNCIADO:
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

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
EJERCICIO 12 [INTERMEDIO]: Complejidad con Estructuras de Datos
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📝 ENUNCIADO:
Comparar la complejidad de las siguientes operaciones en listas vs diccionarios
en Python:
- Buscar un elemento
- Insertar un elemento
- Eliminar un elemento

Indicar cuándo conviene usar cada estructura de datos.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
EJERCICIO 13 [INTERMEDIO]: Análisis de Algoritmo Recursivo
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📝 ENUNCIADO:
Analizar la complejidad temporal y espacial del algoritmo factorial recursivo.
Comparar con la versión iterativa.

🔹 PSEUDOCÓDIGO:
   Función factorialRecursivo(n):
       Si n <= 1:
           Retornar 1
       SiNo:
           Retornar n * factorialRecursivo(n - 1)


===============================================================================
SECCIÓN 3: PILAS (STACKS)
Grupo 4 - Ejercicios 14 al 25
===============================================================================

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
EJERCICIO 14 [BÁSICO]: Implementación Básica de Pila
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📝 ENUNCIADO:
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

✅ EJEMPLO RESUELTO:

```python
class Pila:
    """Implementación de TAD Pila usando lista de Python"""
    
    def __init__(self):
        """Crea una pila vacía"""
        self._elementos = []
    
    def push(self, elemento):
        """
        Apila un elemento en el tope
        Postcondición: size aumenta en 1
        """
        self._elementos.append(elemento)
    
    def pop(self):
        """
        Desapila y retorna el elemento del tope
        Precondición: pila no vacía
        Postcondición: size disminuye en 1
        """
        if self.is_empty():
            raise IndexError("Pop desde pila vacía")
        return self._elementos.pop()
    
    def peek(self):
        """
        Retorna el elemento del tope sin eliminarlo
        Precondición: pila no vacía
        """
        if self.is_empty():
            raise IndexError("Peek en pila vacía")
        return self._elementos[-1]
    
    def is_empty(self) -> bool:
        """Retorna True si la pila está vacía"""
        return len(self._elementos) == 0
    
    def size(self) -> int:
        """Retorna la cantidad de elementos"""
        return len(self._elementos)
    
    def __str__(self):
        return f"Pila: {self._elementos} (tope: {self._elementos[-1] if not self.is_empty() else 'vacía'})"

# Ejemplo de uso:
pila = Pila()
pila.push(10)
pila.push(20)
pila.push(30)

print(pila)  # Pila: [10, 20, 30] (tope: 30)
print(f"Tope: {pila.peek()}")  # 30
print(f"Desapilar: {pila.pop()}")  # 30
print(f"Tamaño: {pila.size()}")  # 2
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
EJERCICIO 15 [BÁSICO]: Invertir una Cadena
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📝 ENUNCIADO:
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

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
EJERCICIO 16 [BÁSICO]: Validar Paréntesis Balanceados
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📝 ENUNCIADO:
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

✅ EJEMPLO RESUELTO:

```python
def validar_parentesis(expresion: str) -> bool:
    """
    Verifica si los paréntesis están balanceados
    
    Ejemplos:
    >>> validar_parentesis("(())")
    True
    >>> validar_parentesis("(()")
    False
    >>> validar_parentesis(")(")
    False
    """
    pila = []
    
    for caracter in expresion:
        if caracter == '(':
            pila.append(caracter)
        elif caracter == ')':
            if not pila:  # Pila vacía
                return False
            pila.pop()
    
    return len(pila) == 0  # Verdadero si no quedan paréntesis sin cerrar

# Casos de prueba:
casos = [
    ("()", True),
    ("(())", True),
    ("(()())", True),
    ("(()", False),
    ("())", False),
    (")(", False),
    ("", True),
]

for expresion, esperado in casos:
    resultado = validar_parentesis(expresion)
    estado = "✓" if resultado == esperado else "✗"
    print(f"{estado} '{expresion}' → {resultado} (esperado: {esperado})")
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
EJERCICIO 17 [INTERMEDIO]: Validar Múltiples Tipos de Delimitadores
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📝 ENUNCIADO:
Exte
