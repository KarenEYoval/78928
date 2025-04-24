#Importar lo necesario para que flask funcione
#Importar la clase Flask
#Response es para devolver una respuesta en formato JSON
from flask import Flask, Response 

#Creamos la aplicacion y le damos un nombre
app = Flask(__name__)

#Es un decorador. Esto le dice a Flask que cada vez que un usuario visite la URL /, 
#se debe ejecutar la función que está justo debajo de esa línea. 
#En este caso, es la función inicio().
@app.route('/')
def inicio():
    return 'Bienvenido a la pagina de inicio!'

@app.route('/saludar')
def hola_mundo():
    return 'Hola Mundo!'

@app.route('/hola')
def hola_html():
    return '<h1 style="color:red";>Hola!</h1> '

@app.route('/adios')
def adios_mundo():
    return 'Adios Mundo!'

@app.route('/json')
def algo():
    return Response('{"nombre":"John"}', mimetype='application/json')

@app.route('/xml')
def xml():
    xml= '''<?xml version="1.0"?>
    <persona>
    <nombre>John</nombre>
    </persona>'''
    return Response(xml, mimetype='application/xml')

if _name_ == '_main_':
    app.run(host='0.0.0.0', debug=True)