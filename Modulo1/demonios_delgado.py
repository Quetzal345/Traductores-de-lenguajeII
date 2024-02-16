import random
import tkinter as tk
from tkinter import messagebox, simpledialog
import pickle
import threading
import time
import multiprocessing

class JuegoAdivinanzaGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Juego de Adivinanzas")

        self.label_instrucciones = tk.Label(self.root, text="Elige el rango de números:")
        self.label_instrucciones.pack(pady=10)

        self.scale_rango = tk.Scale(self.root, from_=1, to=100, orient=tk.HORIZONTAL, length=200, resolution=1)
        self.scale_rango.set(50)
        self.scale_rango.pack(pady=10)

        self.label_rango = tk.Label(self.root, text="Rango: 1 - 100")
        self.label_rango.pack(pady=10)

        self.entry = tk.Entry(self.root)
        self.entry.pack(pady=10)

        self.button_adivinar = tk.Button(self.root, text="Adivinar", command=self.verificar_adivinanza)
        self.button_adivinar.pack(pady=10)

        self.label_intentos = tk.Label(self.root, text="Intentos: 0")
        self.label_intentos.pack(pady=10)

        self.button_cambiar_dificultad = tk.Button(self.root, text="Cambiar Dificultad", command=self.cambiar_dificultad)
        self.button_cambiar_dificultad.pack(pady=5)

        self.button_reiniciar_juego = tk.Button(self.root, text="Reiniciar Juego", command=self.reiniciar_juego)
        self.button_reiniciar_juego.pack(pady=5)

        self.menu = tk.Menu(self.root)
        self.menu.add_command(label="Salir", command=self.salir)
        self.root.config(menu=self.menu)

        self.cargar_estado()
        self.iniciar_demonio_estado_juego()

    def iniciar_demonio_estado_juego(self):
        threading.Thread(target=self.demonio_estado_juego, daemon=True).start()

    def demonio_estado_juego(self):
        while True:
            time.sleep(30)  # Revisa el estado del juego cada 30 segundos
            self.imprimir_estado_juego()

    def imprimir_estado_juego(self):
        print("Demonio: Revisando estado del juego...")

    def verificar_adivinanza(self):
        rango = int(self.scale_rango.get())

        if not hasattr(self, 'numero_secreto'):  # Si el número secreto aún no ha sido generado
            self.numero_secreto = random.randint(1, rango)

        intento = int(self.entry.get())
        self.intentos += 1

        if intento == self.numero_secreto:
            messagebox.showinfo("¡Correcto! :)", f"¡Has adivinado el numero en {self.intentos} intentos!")
            self.reiniciar_juego()
            return  # Salir de la función después de adivinar correctamente
        elif intento < self.numero_secreto:
            messagebox.showinfo("Incorrecto :(", "El numero es mayor. ¡Intentalo de nuevo! :( ")
        else:
            messagebox.showinfo("Incorrecto :(", "El numero es menor. ¡Intentalo de nuevo! :(")

        self.label_intentos.config(text=f"Intentos: {self.intentos}")
        self.label_rango.config(text=f"Rango: 1 - {rango}")
        self.guardar_estado()

    def reiniciar_juego(self):
        self.intentos = 0
        self.label_intentos.config(text="Intentos: 0")
        self.scale_rango.set(self.rango_guardado)  # Restaurar el rango anterior
        self.label_rango.config(text=f"Rango: 1 - {self.rango_guardado}")

        # Generar un nuevo número secreto
        rango = int(self.scale_rango.get())
        self.numero_secreto = random.randint(1, rango)

    def cambiar_dificultad(self):
        rango = int(self.scale_rango.get())
        nuevo_rango = tk.simpledialog.askinteger("Cambiar Dificultad", "Introduce un nuevo rango (1-100):", initialvalue=rango)
        if nuevo_rango is not None:
            self.scale_rango.set(nuevo_rango)
            self.label_rango.config(text=f"Rango: 1 - {nuevo_rango}")

    def salir(self):
        self.root.destroy()

    def guardar_estado(self):
        estado = {"intentos": self.intentos, "rango": int(self.scale_rango.get())}
        with open("estado_juego.pkl", "wb") as archivo:
            pickle.dump(estado, archivo)

    def cargar_estado(self):
        try:
            with open("estado_juego.pkl", "rb") as archivo:
                estado = pickle.load(archivo)
                self.intentos = estado.get("intentos", 0)
                self.rango_guardado = estado.get("rango", 50)  # Valor predeterminado si 'rango' no está presente
                self.scale_rango.set(self.rango_guardado)
                self.label_rango.config(text=f"Rango: 1 - {self.rango_guardado}")
        except Exception as e:
            messagebox.showerror("Error", f"Error al cargar el estado del juego: {e}")

    def ejecutar_operacion_costosa(self):
        def operacion_costosa():
            # Simulación de una operación costosa que toma tiempo
            numeros = [random.randint(1, 100) for _ in range(1000000)]
            suma = sum(numeros)
            print("Suma de los números generados:", suma)

        threading.Thread(target=operacion_costosa).start()

    def ejecutar_operacion_costosa_proceso(self):
        proceso = multiprocessing.Process(target=self.operacion_costosa_proceso)
        proceso.start()

    def operacion_costosa_proceso(self):
        # Simulación de una operación costosa que toma tiempo
        numeros = [random.randint(1, 100) for _ in range(1000000)]
        suma = sum(numeros)
        print("Suma de los números generados:", suma)

if __name__ == "__main__":
    juego_gui = JuegoAdivinanzaGUI()
    juego_gui.root.mainloop()
