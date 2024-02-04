# Importar el módulo abc para crear clases abstractas
from abc import ABC, abstractmethod

# Crear la clase ElementoPila
class ElementoPila(ABC):
    # Definir el método abstracto muestra
    @abstractmethod
    def muestra(self):
        pass

# Crear la clase Terminal que hereda de ElementoPila
class Terminal(ElementoPila):
    # Definir el constructor con el atributo simbolo
    def __init__(self, simbolo):
        self.simbolo = simbolo
    
    # Implementar el método muestra
    def muestra(self):
        print(f"Terminal: {self.simbolo}")

# Crear la clase NoTerminal que hereda de ElementoPila
class NoTerminal(ElementoPila):
    # Definir el constructor con el atributo simbolo
    def __init__(self, simbolo):
        self.simbolo = simbolo
    
    # Implementar el método muestra
    def muestra(self):
        print(f"No terminal: {self.simbolo}")

# Crear la clase Estado que hereda de ElementoPila
class Estado(ElementoPila):
    # Definir el constructor con el atributo numero
    def __init__(self, numero):
        self.numero = numero
    
    # Implementar el método muestra
    def muestra(self):
        print(f"Estado: {self.numero}")

# Crear la clase Pila
class Pila:
    # Definir el constructor con el atributo lista
    def __init__(self):
        self.lista = []
    
    # Definir el método push que acepta un objeto de tipo ElementoPila
    def push(self, elemento):
        self.lista.insert(0, elemento)
    
    # Definir el método pop que devuelve un objeto de tipo ElementoPila
    def pop(self):
        return self.lista.pop(0)
    
    # Definir el método top que devuelve un objeto de tipo ElementoPila
    def top(self):
        return self.lista[0] if self.lista else None
    
    # Definir el método muestra que muestra el contenido de la pila
    def muestra(self):
        print("Pila:")
        for elemento in self.lista:
            elemento.muestra()
        print()

# Crear una función de ejemplo
def ejemplo():
    # Crear una pila
    pila = Pila()
    # Crear algunos objetos de las clases Terminal, NoTerminal y Estado
    t1 = Terminal("a")
    t2 = Terminal("+")
    n1 = NoTerminal("S")
    e1 = Estado(0)
    e2 = Estado(1)
    e3 = Estado(2)
    # Insertar los objetos en la pila
    pila.push(e1)
    pila.push(t1)
    pila.push(e2)
    pila.push(t2)
    pila.push(n1)
    pila.push(e3)
    # Mostrar el contenido de la pila
    pila.muestra()
    # Eliminar un objeto de la pila
    pila.pop()
    # Mostrar el contenido de la pila
    pila.muestra()

# Llamar a la función de ejemplo
ejemplo()
