from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>Bienvenido al Demo de la Droguería</h1><p>Selecciona las opciones en el menú para explorar.</p>'

@app.route('/catalogo')
def catalogo():
    return '<h2>Catálogo de Fármacos e Insumos</h2><ul><li>Paracetamol</li><li>Guantes</li><li>Jeringas</li></ul>'

@app.route('/pedidos')
def pedidos():
    return '<h2>Realiza tu pedido aquí.</h2>'
Actualización del demo con funciones básicas

