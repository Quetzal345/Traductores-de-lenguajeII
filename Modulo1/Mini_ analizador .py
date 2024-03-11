import re

def analizador_lexico(cadena):
    # Definimos las expresiones regulares para identificadores y números reales
    patron_identificador = r'[a-zA-Z][a-zA-Z0-9]*'
    patron_numero_real = r'\d+\.\d+'
    patron_numero_entero = r'\d+'

    # Lista para almacenar los tokens encontrados
    tokens = []

    # Escaneo de la cadena para identificar tokens
    while cadena:
        # Eliminamos los espacios en blanco al inicio de la cadena
        cadena = cadena.lstrip()

        # Verificamos si el token es un identificador
        match_identificador = re.match(patron_identificador, cadena)
        if match_identificador:
            identificador = match_identificador.group(0)
            tokens.append(('IDENTIFICADOR', identificador))
            cadena = cadena[len(identificador):].lstrip()
            continue

        # Verificamos si el token es un número real
        match_numero_real = re.match(patron_numero_real, cadena)
        if match_numero_real:
            numero_real = match_numero_real.group(0)
            tokens.append(('REAL', numero_real))
            cadena = cadena[len(numero_real):].lstrip()
            continue

        # Verificamos si el token es un número entero
        match_numero_entero = re.match(patron_numero_entero, cadena)
        if match_numero_entero:
            numero_entero = match_numero_entero.group(0)
            tokens.append(('ENTERO', numero_entero))
            cadena = cadena[len(numero_entero):].lstrip()
            continue

        # Si no coincide con ninguno de los tokens, se considera un error léxico
        print("Error léxico: no se pudo reconocer el token")
        return []

    return tokens

# Ejemplo de uso
cadena_prueba = "x12 y 34.56 z 78.9 123"
tokens = analizador_lexico(cadena_prueba)
if tokens:
    print("Tokens encontrados:")
    for token in tokens:
        print(token)
else:
    print("No se encontraron tokens.")
