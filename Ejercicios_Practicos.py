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

