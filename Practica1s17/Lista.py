__author__ = 'Jose'

import NodoLista
import os
import graphviz as ejecutar
nodo = NodoLista


class ListaSimple(object):
    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.tamanio = 0

    def esVacio(self):
        if self.primero == None:
            return True

    def insertarInicio(self,palabra):
        nuevo = nodo.NodoLista(palabra)
        if self.esVacio()==True:
            self.primero = nuevo
            self.ultimo = nuevo
        else:
            nuevo.siguiente = self.primero
            self.primero = nuevo
        self.tamanio +=1


    def obtenerTamanio(self):
        return self.tamanio

    def buscar(self, valor):
        aux = self.primero
        encontrado = False
        while(aux!=None and encontrado!=True):
            if valor == aux.getPalabra():
                encontrado = True
            else:
                aux = aux.siguiente
        return encontrado

    def obtenerPosicion(self, valor):
        if self.buscar(valor):
            aux = self.primero
            contador = 0
            while valor != aux.getPalabra():
                contador = contador +1
                aux = aux.siguiente
            return contador
        else:
            print("NO SE ENCONTRÓ EL DATO")



    def eliminarPorIndice(self,indice):
        if indice >=0 and indice<self.tamanio:
            if indice ==0:
                self.primero = self.primero.siguiente
            elif indice == self.obtenerTamanio()-1:
                actual = self.primero
                while actual.siguiente!=self.ultimo:
                    actual = actual.siguiente
                aux = actual.siguiente
                actual.siguiente = None
                self.ultimo = actual
            else:
                aux = self.primero
                contador = 0
                while contador<indice-1:
                    aux = aux.siguiente
                    contador+=1
                siguienteNodo = aux.siguiente
                aux.siguiente = siguienteNodo.siguiente
                aux = None
        self.tamanio -=1


    def insertarFinal(self,palabra):
        nuevo = nodo.NodoLista(palabra)
        if self.esVacio()==True:
            self.primero = nuevo
            self.ultimo = nuevo
        else:
            self.ultimo.siguiente = nuevo
            self.ultimo = nuevo
        self.tamanio += 1

    def imprimirLista(self):
        if self.esVacio()==True:
            print("Lista Vacia")
        else:
            validar = True
            temp = self.primero
            while(validar):
                print(temp.getPalabra())
                if temp == self.ultimo:
                    validar = False
                else:
                    temp = temp.siguiente

    def graficarLista(self):
        aux = self.primero
        aux2 = self.primero.siguiente
        file_path = "Graficas"
        try:
            if not os.path.exists(file_path):
                os.makedirs(file_path)
                print("se ha creado el directorio")
            archivo = open("Graficas/lista.dot","w")
            archivo.write("digraph Lista{\n")
            archivo.write("\t node[shape=record];\n")
            archivo.write("\t subgraph culsterStack {\n")
            archivo.write("\t label = \"Lista Simple Enlazada \";\n")
            archivo.write("\t fontsize = 16;\n")
            while aux!=None and aux2!=None:
                archivo.write("\t"+aux.getPalabra()+"->"+aux2.getPalabra()+"\n")
                aux = aux.siguiente
                aux2 = aux2.siguiente
            archivo.write("\t}\n")
            archivo.write("}")
            archivo.close()


        except ValueError:
            print("Error!")