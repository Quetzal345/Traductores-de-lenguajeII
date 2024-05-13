import os

# Analizador Léxico
def scanner(code):
    tokens = []
   
    for line in code.split('\n'):
        for word in line.split():
            tokens.append(word)

    return tokens

# Tabla LR
class LRTable:
    def __init__(self, filename):
        self.idRegla = []
        self.lonRegla = []
        self.noTerminal = []
        self.table = []

        with open(filename, 'r') as file:
            
            lines = file.readlines()
            
            for line in lines[:3]:
                parts = line.strip().split('\t')
                try:
                    self.idRegla.append(int(parts[0]))
                    self.lonRegla.append(int(parts[1]))
                    self.noTerminal.append(parts[2])
                except IndexError:
                    print("Error: formato incorrecto en la línea:", line.strip())

            
            dimensions = lines[3].split()
            rows = int(dimensions[0])
            columns = int(dimensions[1])

            # Leer la tabla LR
            self.table = []
            for line in lines[4:]:
                try:
                    row = list(map(int, line.split()))
                    self.table.append(row)
                except ValueError:
                    print("Error: formato incorrecto en la línea de la tabla LR:", line.strip())

    def parse(self, tokens):
        stack = [0]
        cursor = 0
        while True:
            state = stack[-1]
            symbol = tokens[cursor]
            action = self.table[state][symbol]
            if action > 0:  # Desplazamiento
                stack.append(action)
                cursor += 1
            elif action < 0:  # Reducción
                rule_id = -action
                rule_len = self.lonRegla[rule_id - 1]
                for _ in range(rule_len):
                    stack.pop()
                state = stack[-1]
                stack.append(self.table[state][self.idRegla[rule_id - 1]])
            elif action == 0:
                if cursor == len(tokens) - 1:
                    print("Análisis sintáctico exitoso.")
                    break
                else:
                    print("Error de sintaxis.")
                    break

# Ejemplo de uso
if __name__ == "__main__":
    # Solicitar la ruta del archivo al usuario
    filename = input("Por favor, ingresa la ruta del archivo: ")
    
    # Normalizar la ruta del archivo para asegurar su correcta interpretación
    filename = os.path.normpath(filename)
    
    # Verificar si el archivo existe antes de intentar abrirlo
    if os.path.exists(filename):
        # Analizar léxicamente el código fuente
        try:
            with open(filename, 'r') as file:
                code = file.read()
            tokens = scanner(code)
            print("Tokens:", tokens)

            # Crear la tabla LR y analizar sintácticamente el código fuente
            lr_table = LRTable(filename)
            lr_table.parse(tokens)
        except FileNotFoundError:
            print("El archivo especificado no se encontró.")
    else:
        print("La ruta especificada no es válida.")

