from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from models.usuario_model import Usuario  # Ajusta según tu modelo
from database import db

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['usuario']
        password = request.form['password']
        
        usuario = Usuario.query.filter_by(username=username).first()
        if usuario and usuario.verify_password(password):
            session['usuario'] = usuario.username
            session['role'] = usuario.rol
            return redirect(url_for('home'))  # Redirige al home
        else:
            flash('Usuario o contraseña incorrectos', 'danger')
    return render_template('login.html')


@auth_bp.route('/logout')
def logout():
    session.pop('usuario', None)
    session.pop('role', None)  # Elimina el rol de la sesión al cerrar sesión
    return redirect(url_for('auth.login'))

