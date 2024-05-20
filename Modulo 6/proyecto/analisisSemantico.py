from io import open

class Simbolo:

    def __init__(self):
        self.identificador = ""
        self.tipo = ""
        self.tipoDato = ""
        self.ambito = ""

    def printSimbolo(self):
        print(f"ID: {self.identificador} | Tipo: {self.tipo} | Tipo de dato: {self.tipoDato} | Ambito: {self.ambito}")

class Funcion(Simbolo):

    def __init__(self):
        super().__init__()
        self.numParametros = 0

class Semantico:

    def __init__(self):
        self.tablaSimbolos = []
        self.listaErrores = []
        self.ambito = "Global"
        self.sangriaActual = 0
        self.regresa = False
        self.asignacion = False
        self.variableAsignacion = ""

    def crearArchivo(self):
        with open("CodigoTraducido.asm", "a+") as file:
            file.write('.386\n')
            file.write('.model flat, stdcall\n')
            file.write('option casemap:none\n\n')
            file.write('include c:\\masm32\\include\\masm32rt.inc\n\n')
            file.write('.code\n\n')

    def analiza(self, n, archivo):
        contador = 0
        siguiente = -1
        if len(n.elementosEliminados) > 0:
            for i in reversed(n.elementosEliminados):
                if i.nodo.regla == "DefFunc" and i.id == 2:
                    funcion = Funcion()
                    funcion.tipo = "Funcion"
                    funcion.tipoDato = i.nodo.elementosEliminados[-1].valor
                    funcion.ambito = "Global"

                    if not self.buscaFuncion(funcion.identificador, funcion.ambito, funcion.tipoDato):
                        self.ambito = i.nodo.elementosEliminados[-2].valor
                        self.tablaSimbolos.append(funcion)
                        funcion.identificador = i.nodo.elementosEliminados[-2].valor
                        stringAux = f'{funcion.identificador} proc'
                        archivo.write(stringAux)
                    else:
                        error = f"ERROR: Function '{funcion.identificador}' redefined"
                        self.listaErrores.append(error)

                if i.id == 1 and i.valor == "}":
                    if self.ambito == "main":
                        if self.regresa:
                            archivo.write("ret\n")
                            self.regresa = False
                        archivo.write("invoke ExitProcess, 0\n\nmain endp\nend main")
                    else:
                        if self.regresa:
                            archivo.write("ret\n")
                            self.regresa = False
                        archivo.write(f"{self.ambito} endp\n\n")

                if i.id == 2 and i.nodo.regla == "Parametros" and len(i.nodo.elementosEliminados) > 0:
                    nodoAux = i.nodo
                    parametro = Simbolo()
                    parametro.tipo = "Parametro"
                    parametro.tipoDato = nodoAux.elementosEliminados[-1].valor
                    parametro.identificador = nodoAux.elementosEliminados[-2].valor
                    parametro.ambito = self.ambito

                    if not self.buscaParametro(parametro.identificador, parametro.ambito, parametro.tipoDato):
                        self.tablaSimbolos.append(parametro)
                        self.aumentaNumParametros(self.ambito, "Global")
                        stringAux = f' {parametro.identificador}:DWORD'
                        archivo.write(stringAux)
                        listaParam = nodoAux.elementosEliminados[0].nodo

                        if listaParam.regla == "ListaParam" and len(listaParam.elementosEliminados) > 0:
                            self.agregaListaParam(listaParam, archivo)
                            archivo.write('\n')
                    else:
                        error = f"ERROR: Parameter '{parametro.identificador}' defined twice"
                        self.listaErrores.append(error)

                if i.id == 2 and i.nodo.regla == "Parametros" and len(i.nodo.elementosEliminados) == 0:
                    archivo.write('\n')

                if i.id == 2 and i.nodo.regla == "DefVar":
                    nodoAux = i.nodo
                    variable = Simbolo()
                    variable.tipo = "Variable"
                    variable.tipoDato = nodoAux.elementosEliminados[-1].valor
                    variable.identificador = nodoAux.elementosEliminados[-2].valor
                    variable.ambito = self.ambito

                    if not self.buscaIdentificador(variable.identificador, variable.ambito, variable.tipoDato):
                        self.tablaSimbolos.append(variable)
                        stringAux = f'local {variable.identificador}:DWORD\n'
                        archivo.write(stringAux)
                        listVar = nodoAux.elementosEliminados[1].nodo

                        if listVar.regla == "ListaVar" and len(listVar.elementosEliminados) > 0:
                            self.agregaListaVar(nodoAux.elementosEliminados[-1].valor, listVar, archivo)
                    else:
                        error = f"ERROR: Variable '{variable.identificador}' redefined"
                        self.listaErrores.append(error)

                if i.id == 2 and i.nodo.regla == "Termino" and i.valor == "36":
                    terminalAux = i.nodo.elementosEliminados[0]

                    if not self.existeIdentificador(terminalAux.valor, self.ambito) and not self.existeParametro(terminalAux.valor, self.ambito):
                        error = f"ERROR: Variable '{terminalAux.valor}' not defined"
                        self.listaErrores.append(error)

                if i.id == 2 and i.nodo.regla == "Sentencia" and i.valor == "21":
                    terminalAux = i.nodo.elementosEliminados[-1]

                    if not self.existeIdentificador(terminalAux.valor, self.ambito) and not self.existeParametro(terminalAux.valor, self.ambito):
                        error = f"ERROR: Variable '{terminalAux.valor}' not defined"
                        self.listaErrores.append(error)
                    else:
                        self.asignacion = True
                        self.variableAsignacion = terminalAux.valor

                if i.id == 2 and i.nodo.regla == "LlamadaFunc" and i.valor == "40":
                    terminalAux = i.nodo.elementosEliminados[-1]

                    if not self.existeFuncion(terminalAux.valor, "Global"):
                        error = f"ERROR: Function '{terminalAux.valor}' not defined"
                        self.listaErrores.append(error)
                    else:
                        arg = i.nodo.elementosEliminados[1]
                        if len(arg.nodo.elementosEliminados) > 0:
                            termino = arg.nodo.elementosEliminados[-1].nodo.elementosEliminados[0].nodo.elementosEliminados[0].valor
                            archivo.write(f"mov eax, {termino}\n")
                            archivo.write("push eax\n")

                            if len(arg.nodo.elementosEliminados[0].nodo.elementosEliminados) > 0:
                                self.agregaArgumentos(arg.nodo.elementosEliminados[0], archivo)

                    funcionAux = self.regresaFuncion(terminalAux.valor, "Global")
                    argumentos = i.nodo.elementosEliminados[1]

                    if len(argumentos.nodo.elementosEliminados) < funcionAux.numParametros:
                        error = f"ERROR: Argument count mismatch"
                        self.listaErrores.append(error)

                    archivo.write(f"call {terminalAux.valor}\n")

                    if self.asignacion:
                        archivo.write(f"mov {self.variableAsignacion}, eax\n")
                        archivo.write(f"mov eax, {self.variableAsignacion}\n")
                        archivo.write("print str$(eax)\n")
                        self.asignacion = False
                        self.variableAsignacion = ""

                if i.id == 2 and i.nodo.regla == "ValorRegresa":
                    self.regresa = True

                if i.id == 2 and i.nodo.regla == "Expresion":
                    if i.valor == "47" and i.nodo.elementosEliminados[1].valor == "+":
                        termino_1 = i.nodo.elementosEliminados[-1].nodo.elementosEliminados[-1].nodo.elementosEliminados[0].valor
                        termino_2 = i.nodo.elementosEliminados[0].nodo.elementosEliminados[-1].nodo.elementosEliminados[0].valor

                        archivo.write(f"mov eax, {termino_1}\n")
                        archivo.write(f"add eax, {termino_2}\n")

                        if self.asignacion:
                            archivo.write(f"mov {self.variableAsignacion}, eax\n")
                            archivo.write(f"mov eax, {self.variableAsignacion}\n")
                            archivo.write("print str$(eax)\n")
                            self.asignacion = False
                            self.variableAsignacion = ""

                    if i.valor == "47" and i.nodo.elementosEliminados[1].valor == "-":
                        termino_1 = i.nodo.elementosEliminados[-1].nodo.elementosEliminados[-1].nodo.elementosEliminados[0].valor
                        termino_2 = i.nodo.elementosEliminados[0].nodo.elementosEliminados[-1].nodo.elementosEliminados[0].valor
                        archivo.write(f"mov eax, {termino_1}\n")
                        archivo.write(f"sub eax, {termino_2}\n")

                        if self.asignacion:
                            archivo.write(f"mov {self.variableAsignacion}, eax\n")
                            archivo.write(f"mov eax, {self.variableAsignacion}\n")
                            archivo.write("print str$(eax)\n")
                            self.asignacion = False
                            self.variableAsignacion = ""

                if i.id == 2:
                    i.nodo.sangria = self.sangriaActual
                    i.nodo.printRegla()
                    self.analiza(i.nodo, archivo)

                contador += 1

            self.sangriaActual += round(len(n.elementosEliminados[siguiente].nodo.regla) / 2)

    def buscaIdentificador(self, nombre, ambito, tipo):
        for i in self.tablaSimbolos:
            if i.tipo == "Variable" and i.identificador == nombre and i.ambito == ambito and i.tipoDato == tipo:
                return True
        return False

    def existeIdentificador(self, nombre, ambito):
        for i in self.tablaSimbolos:
            if i.tipo == "Variable" and i.identificador == nombre and i.ambito == ambito:
                return True
        return False

    def buscaFuncion(self, nombre, ambito, tipo):
        for i in self.tablaSimbolos:
            if i.tipo == "Funcion" and i.identificador == nombre and i.ambito == ambito and i.tipoDato == tipo:
                return True
        return False

    def existeFuncion(self, nombre, ambito):
        for i in self.tablaSimbolos:
            if i.tipo == "Funcion" and i.identificador == nombre and i.ambito == ambito:
                return True
        return False

    def buscaParametro(self, nombre, ambito, tipo):
        for i in self.tablaSimbolos:
            if i.tipo == "Parametro" and i.identificador == nombre and i.ambito == ambito and i.tipoDato == tipo:
                return True
        return False

    def existeParametro(self, nombre, ambito):
        for i in self.tablaSimbolos:
            if i.tipo == "Parametro" and i.identificador == nombre and i.ambito == ambito:
                return True
        return False

    def agregaListaVar(self, tipo, nodo, archivo):
        segVariable = Simbolo()
        segVariable.tipo = "Variable"
        segVariable.tipoDato = tipo
        segVariable.identificador = nodo.elementosEliminados[-2].valor
        segVariable.ambito = self.ambito

        if not self.buscaIdentificador(segVariable.identificador, segVariable.ambito, segVariable.tipoDato):
            self.tablaSimbolos.append(segVariable)
            archivo.write(f'local {segVariable.identificador}:DWORD\n')
            listaVar = nodo.elementosEliminados[0].nodo
            if listaVar.regla == "ListaVar" and len(listaVar.elementosEliminados) > 0:
                self.agregaListaVar(tipo, listaVar, archivo)
        else:
            error = f"ERROR: Variable '{segVariable.identificador}' redefined"
            self.listaErrores.append(error)

    def agregaListaParam(self, nodo, archivo):
        segParametro = Simbolo()
        segParametro.tipo = "Parametro"
        segParametro.tipoDato = nodo.elementosEliminados[-2].valor
        segParametro.identificador = nodo.elementosEliminados[-3].valor
        segParametro.ambito = self.ambito

        if not self.buscaParametro(segParametro.identificador, segParametro.ambito, segParametro.tipoDato):
            self.tablaSimbolos.append(segParametro)
            self.aumentaNumParametros(self.ambito, "Global")
            stringAux = f',{segParametro.identificador}:DWORD'
            archivo.write(stringAux)
            listaParam = nodo.elementosEliminados[0].nodo
            if listaParam.regla == "ListaParam" and len(listaParam.elementosEliminados) > 0:
                self.agregaListaParam(listaParam, archivo)
        else:
            error = f"ERROR: Parameter '{segParametro.identificador}' defined twice"
            self.listaErrores.append(error)

    def agregaArgumentos(self, nodo, archivo):
        arg = nodo.nodo.elementosEliminados[1].nodo.elementosEliminados[0].nodo.elementosEliminados[0].valor
        archivo.write(f"mov eax, {arg}\n")
        archivo.write("push eax\n")
        if len(nodo.nodo.elementosEliminados[0].nodo.elementosEliminados) > 0:
            self.agregaArgumentos(nodo.nodo.elementosEliminados[0].nodo.elementosEliminados, archivo)

    def aumentaNumParametros(self, nombre, ambito):
        for i in self.tablaSimbolos:
            if i.tipo == "Funcion" and i.identificador == nombre and i.ambito == ambito:
                i.numParametros += 1

    def regresaFuncion(self, nombre, ambito):
        for i in self.tablaSimbolos:
            if i.tipo == "Funcion" and i.identificador == nombre and i.ambito == ambito:
                return i

    def muestraSimbolos(self):
        print("******* Tabla de Simbolos *******\n")
        for i in self.tablaSimbolos:
            i.printSimbolo()

    def muestraErrores(self):
        print("\n\n******* Analisis Semantico *******")
        if len(self.listaErrores) == 0:
            print("No se encontraron errores ")
        else:
            for i in self.listaErrores:
                print(i)
        print("\n\n")
