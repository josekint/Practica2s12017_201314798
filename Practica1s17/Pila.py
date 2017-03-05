__author__ = 'Jose'

import NodoPila
import os
nodo = NodoPila

class Pila(object):
    def __init__(self):
        self.primero = None

    def esVacio(self):
        if self.primero == None:
            return True

    def insertarPila(self,numero):
        nuevo = nodo.NodoPila(numero)
        if self.esVacio() == True:
            self.primero = nuevo
        else:
            nuevo.siguiente = self.primero
            self.primero = nuevo

    def eliminar(self):
        if self.esVacio() == True:
            print("Pila vacia")
        var = self.primero.getNumero()
        self.primero = self.primero.siguiente
        return var

    def imprimirPila(self):
        aux = self.primero
        while aux != None:
            print(aux.getNumero())
            aux = aux.siguiente

    def graficarPila(self):
        aux = self.primero
        aux2 = self.primero.siguiente
        file_path = "Graficas"
        try:
            if not os.path.exists(file_path):
                os.makedirs(file_path)
                print("se ha creado el directorio")
            archivo = open("Graficas/pila.dot", "w")
            archivo.write("digraph Lista{\n")
            archivo.write("\t node[shape=record];\n")
            archivo.write("\t subgraph culsterStack {\n")
            archivo.write("\t label = \"Pila \";\n")
            archivo.write("\t fontsize = 16;\n")
            while aux != None and aux2 != None:
                archivo.write("\t" + aux.getNumero() + "->" + aux2.getNumero() + "\n")
                aux = aux.siguiente
                aux2 = aux2.siguiente
            archivo.write("\t}\n")
            archivo.write("}")
            archivo.close()


        except ValueError:
            print("Error!")