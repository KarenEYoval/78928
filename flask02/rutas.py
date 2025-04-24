from flask import Flask, render_template
from modelos import Producto  
#Es una función que te permite renderizar archivos HTML 
#Usamos esto cuando queremos pasarle datos a un archivo HTML y mostrarlo en el navegador

app = Flask(__name__)

@app.route('/')
def inicio():
    productos = [Producto("Manzana", 12), Producto("Peras", 13)]  
    # Assuming Producto takes (name, price)
    return render_template('index.html', productos=productos)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)  # Fixed typo 'hots' to 'host'
