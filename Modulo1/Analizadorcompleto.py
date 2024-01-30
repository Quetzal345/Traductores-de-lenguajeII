import re

# Definición de tokens con tipo
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

# Función para tokenizar el código fuente y asignar tipos
def tokenize(code):
    tokenizado = []
    while code:
        for token_tipo, patron, tipo in tokens:
            match = re.match(patron, code)
            if match:
                valor = match.group(0)
                tokenizado.append((tipo, valor))
                code = code[len(valor):].lstrip()
                break
        else:
            raise ValueError(f"No se pudo tokenizar: {code}")
    return tokenizado

# Ejemplo de uso
codigo_fuente = 'if (x > 0) { return x * 2; } else { return -1; } while {return (23)}'

tokens_resultantes = tokenize(codigo_fuente)
for tipo, valor in tokens_resultantes:
    print(f'Tipo: {tipo}, Valor: {valor}')
