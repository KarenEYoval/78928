from flask import Flask, render_template
from modelos import Producto  # Make sure you have the Producto class in modelos module

app = Flask(__name__)

@app.route('/')
def inicio():
    productos = [Producto("Manzana", 12), Producto("Peras", 13)]  # Assuming Producto takes (name, price)
    return render_template('index.html', productos=productos)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)  # Fixed typo 'hots' to 'host'
