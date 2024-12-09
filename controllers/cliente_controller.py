from flask import request, redirect, url_for, Blueprint

from models.cliente_model import Cliente

from views import cliente_views

cliente_bp  = Blueprint('cliente', __name__, url_prefix="/clientes")

@cliente_bp.route("/")
def index():
    clientes = Cliente.get_all()
    return cliente_views.list(clientes)


@cliente_bp.route("/create", methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        nombre = request.form['nombre']
        email = request.form['email']
        telefono = request.form['telefono']
        

        cliente = Cliente(nombre, email, telefono)
        cliente.save()
        return redirect(url_for('cliente.index'))

    return cliente_views.create()

#EDITAR
@cliente_bp.route("/edit/<int:id>", methods =['GET', 'POST'])
def edit(id):
    cliente = Cliente.get_by_id(id)
    if request.method == 'POST':
        nombre = request.form['nombre']
        email = request.form['email']
        telefono = request.form['telefono']
        
        
        #actualizar
        cliente.update(nombre = nombre, email= email, telefono= telefono)
        return redirect(url_for('cliente.index'))
    return cliente_views.edit(cliente)

@cliente_bp.route("/delete/<int:id>")
def delete(id):
    cliente = Cliente.get_by_id(id)
    cliente.delete()
    return redirect(url_for('cliente.index'))

    return cliente_views.create()