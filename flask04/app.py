from flask import Flask, render_template, request, Response, redirect, url_for
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    # Connect to the database and fetch products
    con = conexion()
    productos = con.execute('SELECT * FROM productos').fetchall()  # Retrieve all products
    con.close()
    return render_template('productos.html', productos=productos)

@app.route('/editar/<int:id>')
def editar(id):
    con = conexion()
    producto = con.execute('SELECT * FROM productos WHERE id = ?', (id,)).fetchone()
    con.close()
    # Show product for editing
    return render_template('editar.html', producto=producto)

@app.route('/guardar', methods=['POST'])
def guardar():
    # Save edited product
    n = request.form.get('nombre')
    p = request.form.get('precio')
    id = request.form.get('id')
    
    con = conexion()
    con.execute('UPDATE productos SET nombre = ?, precio = ? WHERE id = ?', (n, p, id))
    con.commit()
    con.close()
    
    return Response("guardado", headers={'Location': '/'}, status=302)

@app.route('/eliminar/<int:id>')
def eliminar(id):
    # Delete product
    con = conexion()
    con.execute('DELETE FROM productos WHERE id = ?', (id,))
    con.commit()
    con.close()
    
    return Response("eliminado", headers={'Location': '/'}, status=302)

@app.route('/crear', methods=['POST'])
def crear():
    # Create new product
    n = request.form.get('nombre')
    p = request.form.get('precio')
    
    con = conexion()
    con.execute('INSERT INTO productos (nombre, precio) VALUES (?, ?)', (n, p))
    con.commit()
    con.close()
    
    return redirect(url_for('index'))

def conexion():
    con = sqlite3.connect('productos.db')
    con.row_factory = sqlite3.Row
    return con  

def iniciar_db():
    print("Iniciando base de datos...")
    con = conexion()
    con.execute('''
        CREATE TABLE IF NOT EXISTS productos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            precio REAL NOT NULL
        )
    ''')
    con.commit()
    con.close()
    print("Base de datos inicializada.")


if __name__ == '__main__':
    iniciar_db()
    app.run(host='0.0.0.0', debug=True)
