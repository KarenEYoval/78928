from flask import Flask

app = Flask(__name__)

@app.route('/inicio')
def inicio():
    return '<h1 style="color:red;">Inicioo!!</h1>'

@app.route('/adios')
def adios():
    return '<h1 style="color:blue;">Adios!!</h1>'

@app.route('/json')
def algo():
    return {"nombre":"Juan", "edad":30}

@app.route('/XML')
def XML():
   return "<nombre>Karen</nombre><edad>20</edad>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

