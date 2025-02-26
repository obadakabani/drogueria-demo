from flask import Flask, render_template_string, request, redirect, url_for

app = Flask(__name__)

# Página de inicio
@app.route('/')
def home():
    return '''
    <h1>Bienvenido al Demo de la Droguería</h1>
    <p>Selecciona las opciones para explorar:</p>
    <ul>
        <li><a href="/catalogo">Catálogo de Fármacos e Insumos</a></li>
        <li><a href="/pedidos">Realizar Pedido</a></li>
    </ul>
    '''

# Catálogo con selección de productos
@app.route('/catalogo', methods=['GET', 'POST'])
def catalogo():
    productos = ['Paracetamol', 'Guantes', 'Jeringas', 'Alcohol Gel']
    if request.method == 'POST':
        seleccionados = {producto: request.form.get(producto) for producto in productos if request.form.get(producto)}
        return f"<h2>Productos seleccionados:</h2><ul>{''.join([f'<li>{producto}: {cantidad} unidades</li>' for producto, cantidad in seleccionados.items()])}</ul><a href='/catalogo'>Volver</a>"
    
    return render_template_string('''
    <h2>Catálogo de Fármacos e Insumos</h2>
    <form method="POST">
        {% for producto in productos %}
            <label>{{ producto }}:</label>
            <input type="number" name="{{ producto }}" min="0" placeholder="Cantidad"><br>
        {% endfor %}
        <button type="submit">Agregar al Pedido</button>
    </form>
    <a href="/">Volver al inicio</a>
    ''', productos=productos)

# Página para realizar pedidos
@app.route('/pedidos', methods=['GET', 'POST'])
def pedidos():
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        centro_costo = request.form.get('centro_costo')
        observaciones = request.form.get('observaciones')
        return f'''
        <h2>Pedido Realizado</h2>
        <p><strong>Nombre:</strong> {nombre}</p>
        <p><strong>Centro de Costo:</strong> {centro_costo}</p>
        <p><strong>Observaciones:</strong> {observaciones}</p>
        <a href="/pedidos">Realizar otro pedido</a>
        '''
    
    return '''
    <h2>Formulario de Pedido</h2>
    <form method="POST">
        Nombre: <input type="text" name="nombre" required><br>
        Centro de Costo: <input type="text" name="centro_costo" required><br>
        Observaciones: <textarea name="observaciones"></textarea><br>
        <button type="submit">Enviar Pedido</button>
    </form>
    <a href="/">Volver al inicio</a>
    '''



