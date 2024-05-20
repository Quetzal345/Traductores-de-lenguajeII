import analisisLexico2
import pila
import arbolSintactico
import elementoPila
import analisisSemantico

class sintactico:

    def __init__(self):
        self.pila = pila.stack()
        self.gramatica = []
        self.popElements = []
        self.nombreRegla = []
        self.matrizGramatica = []

    def readFile(self):
        file = open("compilador.lr", "r")
        fullString = file.readlines()
        self.gramatica.append("52")
        self.popElements.append("0")
        self.nombreRegla.append(" ")

        for i in range(1, 54):
            line = fullString[i]
            line = line[:-1].split("\t")

            if i != 53:
                self.gramatica.append(line[0])
                self.popElements.append(line[1])
                self.nombreRegla.append(line[2])

            elif i == 53:
                self.gramatica.append(line[0])
                self.popElements.append(line[1])
                self.nombreRegla.append(" ")

        for i in range(54, 148):
            line = fullString[i]
            line = line[:-1].split("\t")
            self.matrizGramatica.append(line)
        file.close()

    def compilador(self, e):
        self.readFile()
        self.pila.limpiar()
        lexico = analisisLexico2.analizador(e)
        e = e + " $"
        entradaDividida = e.split(" ")
        primerNT = elementoPila.noTerminal("$", "$", 2)
        primerEstado = elementoPila.estado("0", "", 3)
        self.pila.push(primerNT)
        self.pila.push(primerEstado)

        valida = False
        cont = 0
        valorTabla = ""

        while not valida:
            (tipo, valor) = lexico.returnTipo(lexico.evaluaElemento(entradaDividida[cont]))
            topePila = int(self.pila.top().returnValor())
            valorTabla = int(self.matrizGramatica[topePila][valor])

            if valorTabla == 0:
                self.report_error(entradaDividida[cont], cont, lexico)
                break

            elif valorTabla > 0:
                terminal = elementoPila.terminal(entradaDividida[cont], "", 1)
                estado = elementoPila.estado(str(valorTabla), "", 3)
                self.pila.push(terminal)
                self.pila.push(estado)
                cont += 1

            elif valorTabla < 0:
                if valorTabla == -1:
                    valida = True
                    print("\n\n***********Arbol Sintactico*************\n")
                    arbolFinal = arbolSintactico.arbolSintactico()
                    analizadorSem = analisisSemantico.Semantico()
                    self.pila.pop()  # POP AL ULTIMO ELEMENTO QUE ES UN ESTADO
                    elemento = self.pila.pop()
                    elemento.nodo.printRegla()
                    analizadorSem.crearArchivo()
                    file = open('CodigoTraducido.asm', 'a+')  # CREAR EL ARCHIVO EN ENSAMBALDOR
                    analizadorSem.analiza(elemento.nodo, file)
                    file.close()
                    analizadorSem.muestraSimbolos()
                    analizadorSem.muestraErrores()  # MOSTRAR LOS ERRORES DEL ANÁLISIS SEMÁNTICO
                    break

                nodo = arbolSintactico.Nodo()
                valorTabla += 1
                numeroEliminar = int(self.popElements[abs(valorTabla)])
                nomRegla = self.nombreRegla[abs(valorTabla)]
                nodo.regla = nomRegla

                if numeroEliminar > 0:
                    for i in range(int(numeroEliminar) * 2):
                        elemento = self.pila.pop()
                        if i % 2 == 1:
                            nodo.elementosEliminados.append(elemento)

                topePila = int(self.pila.top().returnValor())
                reglaReal = str(abs(valorTabla))
                regla = int(self.gramatica[abs(valorTabla)])
                valorTabla = self.matrizGramatica[topePila][regla]

                noTerminal = elementoPila.noTerminal(reglaReal, nomRegla, 2)
                noTerminal.nodo = nodo
                estado = elementoPila.estado(str(valorTabla), "", 3)

                self.pila.push(noTerminal)
                self.pila.push(estado)

    def report_error(self, token, position, lexico):
        token_type = lexico.returnTipo(lexico.evaluaElemento(token))
        print("\n\n***********Analisis semantico************")
        print(f"Error encontrado en el token '{token}' en la posición {position}. Tipo de token: {token_type}")
        print("Posibles causas del error:")
        if token_type == "Identificador":
            print("- Identificador no definido")
            print("- Uso incorrecto del identificador")
        elif token_type == "+":
            print("- Operador '+' utilizado incorrectamente")
        elif token == "$":
            print("- Fin de la entrada inesperado")
        else:
            print("- Símbolo inesperado encontrado")
        print("\n\n")

# Ejemplo de uso:
sint = sintactico()
sint.compilador("a + b")
