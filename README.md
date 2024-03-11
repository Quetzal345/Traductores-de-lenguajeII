# Seminario de solucion de problemas de traductores-de-lenguaje II 
En este readme se podran observar todos los tabajos de la materia.

## [¿Qué es es un analizador léxico?](https://github.com/Quetzal345/Traductores-de-lenguajeII/blob/433b93d2e190244fe7c2afbeac6a5a0a538065ca/que%20es_analizadorlexico_Delgado.pdf)
Un analizador léxico es un programa que se encarga de dividir una secuencia de
caracteres en unidades más pequeñas llamadas tokens, que tienen un significado y una
categoría. Los tokens son la entrada para el analizador sintáctico, que los convierte en
una estructura de árbol que representa la sintaxis del lenguaje.

## [Mini generador léxico](https://github.com/Quetzal345/Traductores-de-lenguajeII/blob/e28a8502635de06d21c78ad7348934c200c2f7c9/Modulo1/Mini_%20analizador%20.py)
El análisis léxico es la primera fase en el proceso de compilación de un programa. Su objetivo es convertir una secuencia de caracteres, representando el código fuente del programa, en una secuencia de "tokens" o unidades léxicas significativas. Estos tokens pueden ser palabras clave, identificadores, operadores, números, etc. Esta fase es crucial ya que proporciona una base para el análisis sintáctico posterior.

En el código proporcionado, se ha implementado un analizador léxico simple en Python que reconoce identificadores y números (tanto enteros como reales) en una cadena de entrada.

![](https://github.com/Quetzal345/Traductores-de-lenguajeII/blob/15fd0a9100648283dd43ed8ee5d6946673126b69/Capturas/cap1.png)

## [Mini analizador sintáctico (Excel)](https://github.com/Quetzal345/Traductores-de-lenguajeII/blob/4701768d08f386457ceb9424dc4aed27301f024d/Modulo1/Mini%20analizador%20lexico.xlsx)
Realizar un archivo en excel simulando las gramáticas del ejercicio 1 y 2 del archivo 

Entrada para el Ejercicio 1
hola+mundo

Entrada para el Ejercicio 2
a+b+c+d+e+f

![](https://github.com/Quetzal345/Traductores-de-lenguajeII/blob/06a3542761f39a6cb3e5e397e67f04ab2ca55b41/Capturas/cap2.png)

## [Analizador léxico completo](https://github.com/Quetzal345/Traductores-de-lenguajeII/blob/a0b84fa3e7707e5a23a09f512a39cb24249b81c3/Modulo1/reporte_Analizadorcompleto.pdf)
Lo que se tiene que hacer en esta actividad, es realizar el analizador léxico completo, 
que reconozca ciertos tokens y a cada uno se le asignara un numero para que al 
momento de imprimir muestre también el número de cada valor como una llave o un 
paréntesis.

Para realizar el código fue reutilizar el código de la practica anterior y agregar mas tokens 
y a estos agregarles un numero aquí se muestra un ejemplo de uso, que pongo dentro 
del código para ver si analiza bien todos los tokens.

### [Codigo del analizador lexico completo](https://github.com/Quetzal345/Traductores-de-lenguajeII/blob/a0b84fa3e7707e5a23a09f512a39cb24249b81c3/Modulo1/Analizadorcompleto.py)

En esta parte del codigo se puede observar que se utilizaron todos los simbolos lexicos del archivo, para asi realizar la actividad.
```
tokens = [
    ('IDENTIFICADOR', r'[a-zA-Z][a-zA-Z0-9]*', 0),
    ('ENTERO', r'\d+', 1),
    ('REAL', r'\d+\.\d+', 2),
    ('CADENA', r'"[^"]*"', 3),
    ('TIPO', r'int|float|void', 4),
    ('OP_SUMA', r'[+-]', 5),
    ('OP_MUL', r'[*/]', 6),
    ('OP_RELAC', r'<|<=|>|>=|!=|==', 7),
    ('OP_OR', r'\|\|', 8),
    ('OP_AND', r'&&', 9),
    ('OP_NOT', r'!', 10),
    ('OP_IGUALDAD', r'==|!=', 11),
    ('PUNTO_Y_COMA', r';', 12),
    ('COMA', r',', 13),
    ('PARENTESIS_ABIERTO', r'\(', 14),
    ('PARENTESIS_CERRADO', r'\)', 15),
    ('LLAVE_ABIERTA', r'{', 16),
    ('LLAVE_CERRADA', r'}', 17),
    ('ASIGNACION', r'=', 18),
    ('IF', r'if', 19),
    ('WHILE', r'while', 20),
    ('RETURN', r'return', 21),
    ('ELSE', r'else', 22),
    ('DESCONOCIDO', r'$', 23)
]
```
![](https://github.com/Quetzal345/Traductores-de-lenguajeII/blob/169a9f278a6284281cf6205f10366f13cd814ac8/Capturas/cap3.png)

## [Mini analizador sintáctico (código)](https://github.com/Quetzal345/Traductores-de-lenguajeII/blob/e80422fce12d798ae0cce1715a1eb21124078777/Modulo1/reporte_mini_analizador.pdf)
Generar un algoritmo para analizar los Ejercicios 1 y 2, los que se realizaron en excel, ahora se realizaran mediante codigo.

### [Codigo](https://github.com/Quetzal345/Traductores-de-lenguajeII/blob/e80422fce12d798ae0cce1715a1eb21124078777/Modulo1/Mini%20Analizador%20sintactico.py)

Se define una clase Pila que implementa una pila básica utilizando una lista en Python. Esta clase tiene métodos para realizar operaciones típicas de una pila como push, pop, top, muestra, e isEmpty.
```
class Pila:
    def __init__(self):
        self.items = []

    def push(self, elemento):
        self.items.append(elemento)

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()

    def top(self):
        if not self.isEmpty():
            return self.items[-1]

    def muestra(self):
        for item in self.items:
            print(item, end=' ')
        print()

    def isEmpty(self):
        return len(self.items) == 0

```
Se define una clase Lexico que representa un analizador léxico básico. Esta clase se utiliza para analizar una cadena de entrada y dividirla en símbolos. Tiene métodos para avanzar al siguiente símbolo y verificar si se ha llegado al final de la entrada.
```
class Lexico:
    def __init__(self, entrada):
        self.entrada = entrada
        self.indice = 0
        self.simbolo = ''

    def sigSimbolo(self):
        if self.indice < len(self.entrada):
            self.simbolo = self.entrada[self.indice]
            self.indice += 1

    def terminado(self):
        return self.indice >= len(self.entrada)

```

![]()

## [Analizador Sintáctico (Implementación usando Objetos)](https://github.com/Quetzal345/Traductores-de-lenguajeII/blob/12f6f5a9cfe146f9c95e5bc60c7e088686072a88/Modulo1/reporte_analizador_objetos.pdf)
Se ha implementado una jerarquía de clases utilizando herencia y clases abstractas para 
representar elementos de una pila, como Terminal, NoTerminal, y Estado.
La clase Pila se encarga de gestionar una lista que actúa como una pila, con métodos 
para agregar, eliminar y mostrar elementos.
Se han creado objetos de las clases definidas, insertándolos en la pila y mostrando su 
contenido.
La estructura general del código sigue principios de programación orientada a objetos 
(OOP) con encapsulamiento y polimorfismo.

Se definen tres clases concretas que heredan de ElementoPila: Terminal, NoTerminal y Estado. Cada una de estas clases representa un tipo de elemento que puede estar en la pila. Cada clase implementa el método muestra según su propio tipo.

```
class Terminal(ElementoPila):
    def __init__(self, simbolo):
        self.simbolo = simbolo
    
    def muestra(self):
        print(f"Terminal: {self.simbolo}")

class NoTerminal(ElementoPila):
    def __init__(self, simbolo):
        self.simbolo = simbolo
    
    def muestra(self):
        print(f"No terminal: {self.simbolo}")

class Estado(ElementoPila):
    def __init__(self, numero):
        self.numero = numero
    
    def muestra(self):
        print(f"Estado: {self.numero}")

```
