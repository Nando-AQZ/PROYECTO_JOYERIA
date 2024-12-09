from flask import Flask, render_template, request, redirect, url_for, session
from controllers import usuario_controller, cliente_controller, producto_controller, venta_controller, auth_controller
from database import db

app = Flask(__name__)

app.secret_key = "clave_super_secreta"  

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///ventas.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

app.register_blueprint(auth_controller.auth_bp)
app.register_blueprint(usuario_controller.usuario_bp)
app.register_blueprint(cliente_controller.cliente_bp)
app.register_blueprint(producto_controller.producto_bp)
app.register_blueprint(venta_controller.venta_bp)

@app.context_processor
def inject_active_path():
    def is_active(path):
        return 'active' if request.path == path else ''
    return dict(is_active=is_active)

@app.route("/")
def home():
    return render_template("home.html")

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)


