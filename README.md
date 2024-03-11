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
