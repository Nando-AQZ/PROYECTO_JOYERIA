from flask import Flask, render_template, request, redirect, url_for, session
from controllers import usuario_controller, cliente_controller, producto_controller, venta_controller, auth_controller
from database import db

# Inicialización de la app
app = Flask(__name__)

# Configuración de la app
app.secret_key = "clave_super_secreta"  

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///ventas.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicialización de la base de datos
db.init_app(app)

# Registro de Blueprints
app.register_blueprint(auth_controller.auth_bp)
app.register_blueprint(usuario_controller.usuario_bp)
app.register_blueprint(cliente_controller.cliente_bp)
app.register_blueprint(producto_controller.producto_bp)
app.register_blueprint(venta_controller.venta_bp)

# Procesador de contexto para rutas activas
@app.context_processor
def inject_active_path():
    def is_active(path):
        return 'active' if request.path == path else ''
    return dict(is_active=is_active)

# Procesador de contexto para pasar el rol del usuario
@app.context_processor
def inject_role():
    role = session.get("role", None)  # Obtén el rol de la sesión, o None si no existe
    return dict(role=role)

# Ruta principal y home
@app.route("/")
@app.route("/home")
def home():
    role = session.get('role')  # Obtén el rol del usuario desde la sesión
    return render_template('home.html', role=role)  # Pasa el rol a la plantilla

# Ejecución de la app
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Crear las tablas si no existen
    app.run(debug=True)


