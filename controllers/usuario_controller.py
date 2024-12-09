from flask import request, redirect, url_for, Blueprint
from models.usuario_model import Usuario
from views import usuario_views

usuario_bp  = Blueprint('usuario', __name__, url_prefix="/usuarios")

@usuario_bp.route("/")
def index():
    usuarios = Usuario.get_all()
    return usuario_views.list(usuarios)


@usuario_bp.route("/create", methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        nombre = request.form['nombre']
        username = request.form['username']
        password = request.form['password']
        rol = request.form['rol']

        usuario = Usuario(nombre, username, password, rol)
        usuario.save()
        return redirect(url_for('usuario.index'))

    return usuario_views.create()


@usuario_bp.route("/edit/<int:id>", methods =['GET', 'POST'])
def edit(id):
    usuario = Usuario.get_by_id(id)
    if request.method == 'POST':
        nombre = request.form['nombre']
        username = request.form['username']
        password = request.form['password']
        rol = request.form['rol']
        
        #actualizar
        usuario.update(nombre = nombre, username= username, password= password, rol= rol)
        return redirect(url_for('usuario.index'))
    return usuario_views.edit(usuario)

@usuario_bp.route("/delete/<int:id>")
def delete(id):
    usuario = Usuario.get_by_id(id)
    usuario.delete()
    return redirect(url_for('usuario.index'))
