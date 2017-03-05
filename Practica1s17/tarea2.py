__author__ = 'Jose'

from flask import Flask, request, Response
app = Flask("Estructuras_De_Datos_tarea2")

@app.route('/tarea2',methods=['POST'])
def tarea2():
	parametro = str(request.form['p'])
	return " Jose Alejandro Urbina Ramirez 201314798 "

@app.route('/')
def hellof():
    return "Estructuras de Datos Jose Urbina"

if __name__ == "__main__":
  app.run()