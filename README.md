# Seminario de solucion de problemas de traductores-de-lenguaje II 
En este readme se podran observar todos los trabajos de la materia y la construccion del traductor.

## [¿Qué es es un analizador léxico?](https://github.com/Quetzal345/Traductores-de-lenguajeII/blob/433b93d2e190244fe7c2afbeac6a5a0a538065ca/que%20es_analizadorlexico_Delgado.pdf)
Un analizador léxico es un programa que se encarga de dividir una secuencia de
caracteres en unidades más pequeñas llamadas tokens, que tienen un significado y una
categoría. Los tokens son la entrada para el analizador sintáctico, que los convierte en
una estructura de árbol que representa la sintaxis del lenguaje.

## [Mini generador léxico](https://github.com/Quetzal345/Traductores-de-lenguajeII/blob/e28a8502635de06d21c78ad7348934c200c2f7c9/Modulo1/Mini_%20analizador%20.py)
El análisis léxico es la primera fase en el proceso de compilación de un programa. Su objetivo es convertir una secuencia de caracteres, representando el código fuente del programa, en una secuencia de "tokens" o unidades léxicas significativas. Estos tokens pueden ser palabras clave, identificadores, operadores, números, etc. Esta fase es crucial ya que proporciona una base para el análisis sintáctico posterior.

En el código proporcionado, se ha implementado un analizador léxico simple en Python que reconoce identificadores y números (tanto enteros como reales) en una cadena de entrada.

cadena_prueba = "x12 y 34.56 z 78.9 123"

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

![](https://github.com/Quetzal345/Traductores-de-lenguajeII/blob/0b87f605e2f632357813b220fe1dba8b9848e56b/Capturas/cap5.png)

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

Se define la clase Pila, que representa una pila de elementos. Tiene métodos para agregar (push) y quitar (pop) elementos de la pila, así como para obtener el elemento en la parte superior de la pila (top). Además, tiene un método muestra para mostrar el contenido de la pila.

```
class Pila:
    def __init__(self):
        self.lista = []

    def push(self, elemento):
        self.lista.insert(0, elemento)

    def pop(self):
        return self.lista.pop(0)

    def top(self):
        return self.lista[0] if self.lista else None

    def muestra(self):
        print("Pila:")
        for elemento in self.lista:
            elemento.muestra()
        print()

```
## [Gramática del compilador](https://github.com/Quetzal345/Traductores-de-lenguajeII/blob/433b93d2e190244fe7c2afbeac6a5a0a538065ca/Modulo1/Gramatica_compilador.pdf)
Este código implementa un analizador léxico y un analizador sintáctico utilizando una 
tabla LR para realizar el análisis sintáctico de un archivo de código fuente. Aquí hay una 
introducción para comprender mejor cada parte:
Analizador Léxico (scanner): Esta función toma el código fuente como entrada y genera 
una lista de tokens. Los tokens son los componentes básicos del lenguaje de 
programación, como palabras clave, identificadores, operadores, etc. El analizador léxico 
divide el código fuente en palabras individuales y las almacena como tokens.

Esta clase tiene cuatro atributos: idRegla, lonRegla, noTerminal, y table. Estos atributos se inicializan como listas vacías en el constructor __init__.

```
class LRTable:
    def __init__(self, filename):
        self.idRegla = []
        self.lonRegla = []
        self.noTerminal = []
        self.table = []

```

Se lee cada línea del archivo y se almacenan en la variable lines. Luego, se itera sobre las primeras tres líneas (lines[:3]). Para cada línea, se eliminan los espacios en blanco al inicio y al final con strip(), y luego se divide la línea en partes utilizando el carácter de tabulación como separador ('\t') mediante split('\t'). Estas partes se almacenan en la lista parts.
```
lines = file.readlines()
for line in lines[:3]:
    parts = line.strip().split('\t')
    try:
        self.idRegla.append(int(parts[0]))
        self.lonRegla.append(int(parts[1]))
        self.noTerminal.append(parts[2])
    except IndexError:
        print("Error: formato incorrecto en la línea:", line.strip())

```

## [Construccion del traductor](https://github.com/Quetzal345/Tolerante-a-fallas/blob/9ed87781a14dda29e0fa896d2b805ffed479d3b2/Modulo%201/Avance_Traductor.pdf)

En esta seccion se veran los avances en general del traductor, ya que las demas secciones explican partes del traductor, aqui veran el traductor armado si se podria decir, claro que se ira actualizando pero se veran los avances.

parsetab.py contiene información importante sobre cómo el analizador sintáctico debe interpretar y procesar la entrada

_tabversion: Indica la versión de la tabla de análisis. Esto puede ser útil para garantizar la compatibilidad entre diferentes versiones del generador de analizadores sintácticos.

_lr_method: Especifica el método de análisis utilizado. En este caso, se utiliza el método LALR (Look-Ahead Left-to-Right, Rightmost derivation).

_lr_signature: Define la firma de la tabla de análisis. Esta firma describe la gramática que el analizador debe reconocer. La firma está escrita en una notación especial que describe las reglas de producción gramatical del lenguaje. Por ejemplo, en la firma proporcionada, podemos ver las reglas de producción para la gramática del lenguaje, como las reglas para las expresiones, términos y factores.

```
_tabversion = '3.10'
_lr_method = 'LALR'
_lr_signature = 'DIVIDE LPAREN MINUS NUMBER PLUS RPAREN TIMESexpression :
expression PLUS term\n | expression MINUS
term\n | termterm : term TIMES factor\n |
term DIVIDE factor\n | factorfactor : NUMBER\n |
LPAREN expression RPAREN'

```

Se define una función para manejar el token NUMBER, que representa un número entero en la entrada. Esta función utiliza una expresión regular para identificar y convertir los números en enteros.

```
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

```

Se definen expresiones regulares para cada token simple. Estas expresiones regulares se utilizan para identificar y reconocer patrones en la entrada que corresponden a cada token.

```
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'

```
Resultados del Traductor

![](https://github.com/Quetzal345/Traductores-de-lenguajeII/blob/67f69f4407a79f85597c1cfc0b56e3e92592096f/Capturas/cap4.png)

