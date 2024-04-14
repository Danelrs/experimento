from flask import Flask, render_template, request, abort, redirect, url_for, make_response
import mysql.connector

db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Rolonlol135",
    database="tienda"
)
cursor = db_connection.cursor()

app = Flask(__name__)

def obtener_clientes():
    cursor.execute("SELECT * FROM clientes")
    clientes = cursor.fetchall()
    return clientes

def obtener_categorias():
    cursor.execute("SELECT * FROM categorias")
    categorias = cursor.fetchall()
    return categorias

def obtener_productos():
    cursor.execute("SELECT * FROM productos")
    productos = cursor.fetchall()
    return productos

def obtener_compras():
    cursor.execute("SELECT * FROM compras")
    compras = cursor.fetchall()
    return compras

def obtener_detalles_pedidos():
    cursor.execute("SELECT * FROM detalles_pedidos")
    detalles_pedidos = cursor.fetchall()
    return detalles_pedidos

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        clientes = obtener_clientes()
        categorias = obtener_categorias()
        productos = obtener_productos()
        compras = obtener_compras()
        detalles_pedidos = obtener_detalles_pedidos()
        
        return render_template('index.html', clientes=clientes, categorias=categorias,
                               productos=productos, compras=compras,
                               detalles_pedidos=detalles_pedidos)

    return render_template('index.html')


@app.route('/agregar_cliente', methods=['POST'])
def agregar_cliente():
    nombre = request.form['nombre']
    apellido = request.form['apellido']
    correo = request.form['correo']
    telefono = request.form['telefono']
    
    cursor.execute("INSERT INTO clientes (Nombre, Apellido, CorreoElectronico, Telefono) VALUES (%s, %s, %s, %s)",
                   (nombre, apellido, correo, telefono))
    db_connection.commit()
    
    return True

@app.route('/agregar_categoria', methods=['POST'])
def agregar_categoria():
    nombre = request.form['nombre']
    descripcion = request.form['descripcion']
    
    cursor.execute("INSERT INTO categorias (Nombre, Descripcion) VALUES (%s, %s)",
                   (nombre, descripcion))
    db_connection.commit()
    
    return True

@app.route('/agregar_producto', methods=['POST'])
def agregar_producto():
    nombre = request.form['nombre']
    descripcion = request.form['descripcion']
    precio = request.form['precio']

    cursor.execute("INSERT INTO productos (Nombre, Descripcion, Precio) VALUES (%s, %s, %s)",
                   (nombre, descripcion, precio))
    db_connection.commit()
    
    return True

@app.route('/agregar_compra', methods=['POST'])
def agregar_compra():
    fecha = request.form['fecha']
    hora = request.form['hora']
    precio = request.form['precio']
    
    cursor.execute("INSERT INTO compras (Fecha, Hora, Precio) VALUES (%s, %s, %s)",
                   (fecha, hora, precio))
    db_connection.commit()
    
    return True

@app.route('/agregar_detalle_pedido', methods=['POST'])
def agregar_detalle_pedido():
    cantidad = request.form['cantidad']
    precio_unidad = request.form['precio_unidad']
    
    cursor.execute("INSERT INTO detalles_pedidos (Cantidad, Precio_Unidad) VALUES (%s, %s)",
                   (cantidad, precio_unidad))
    db_connection.commit()
    
    return True

if __name__ == '__main__':
    app.run(debug=True)
