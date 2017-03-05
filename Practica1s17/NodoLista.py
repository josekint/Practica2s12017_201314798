__author__ = 'Jose'

class NodoLista(object):
    def __init__(self,palabra):
        self.palabra = palabra
        self.siguiente = None
    def getPalabra(self):
        return self.palabra