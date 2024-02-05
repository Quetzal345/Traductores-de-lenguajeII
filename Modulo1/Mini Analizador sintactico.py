import tkinter as tk
import sys

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

def ejemplo1():
    pila = Pila()

    pila.push(2)
    pila.push(3)
    pila.push(4)
    pila.push(5)

    print("Pila inicial:")
    pila.muestra()

    print("\nTop de la pila:", pila.top())
    print("Top de la pila:", pila.top())

    print("\nPop de la pila:", pila.pop())
    print("Pop de la pila:", pila.pop())

    print("\nPila final:")
    pila.muestra()

def ejemplo2():
    lexico = Lexico("+-+")

    while not lexico.terminado():
        lexico.sigSimbolo()
        texto_resultado.insert(tk.END, lexico.simbolo + "\n")

    lexico = Lexico("a")
    texto_resultado.insert(tk.END, "\nIdentificador reconocido:\n")

    while not lexico.terminado():
        lexico.sigSimbolo()
        texto_resultado.insert(tk.END, lexico.simbolo + "\n")

# Crear la interfaz gráfica con Tkinter
root = tk.Tk()
root.title("Mini Analizador Sintáctico")

# Crear y configurar el widget de texto
texto_resultado = tk.Text(root, height=10, width=50)
texto_resultado.pack()

# Redirigir la salida estándar al widget de texto
def redirigir_salida(text_widget):
    class StdoutRedirector:
        def write(self, string):
            text_widget.insert(tk.END, string)
            text_widget.see(tk.END)

    sys.stdout = StdoutRedirector()

# Botones para ejecutar los ejemplos
boton_ejemplo1 = tk.Button(root, text="Ejemplo 1", command=ejemplo1)
boton_ejemplo1.pack()

boton_ejemplo2 = tk.Button(root, text="Ejemplo 2", command=ejemplo2)
boton_ejemplo2.pack()

# Configurar la redirección de salida al widget de texto
redirigir_salida(texto_resultado)

# Ejecutar la interfaz gráfica
root.mainloop()
