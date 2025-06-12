# Importación de las bibliotecas necesarias
from flask import Flask, render_template, redirect, url_for, request, flash  # Manejo de rutas y renderizado de templates
from flask_sqlalchemy import SQLAlchemy  # ORM para bases de datos
from flask_login import LoginManager, login_user, logout_user, login_required, current_user  # Manejo de sesiones de usuario
from models import db, User, Record  # Importación de los modelos de la base de datos
from config import Config  # Configuración de la aplicación
from werkzeug.security import generate_password_hash, check_password_hash  # Manejo seguro de contraseñas

# Inicialización de la aplicación Flask
app = Flask(__name__)
app.config.from_object(Config)  # Carga la configuración desde config.py
db.init_app(app)  # Inicializa SQLAlchemy con la aplicación

# Configuración de autenticación con Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"  # Define la ruta para el login

@login_manager.user_loader
def load_user(user_id):
    """Carga el usuario desde la base de datos cuando inicia sesión."""
    return User.query.get(int(user_id))

# Ruta de inicio
@app.route("/")
def index():
    """Renderiza la página principal."""
    return render_template("index.html")

# Ruta de login
@app.route("/login", methods=["GET", "POST"])
def login():
    """Maneja el inicio de sesión del usuario."""
    if request.method == "POST":
        username = request.form["username"]  # Obtiene el nombre de usuario del formulario
        password = request.form["password"]  # Obtiene la contraseña del formulario
        user = User.query.filter_by(username=username).first()  # Busca al usuario en la base de datos

        if user and check_password_hash(user.password, password):  # Verifica la contraseña
            login_user(user)  # Inicia sesión en Flask-Login
            flash("¡Bienvenido!", "success")  # Mensaje de éxito
            return redirect(url_for("dashboard"))  # Redirige al dashboard

        flash("Usuario o contraseña incorrecta", "error")  # Mensaje de error

    return render_template("login.html")  # Renderiza la página de login

# Ruta de registro de usuario
@app.route("/register", methods=["GET", "POST"])
def register():
    """Permite el registro de nuevos usuarios."""
    if request.method == "POST":
        username = request.form["username"]
        password = generate_password_hash(request.form["password"], method="pbkdf2:sha256")  # Encripta la contraseña
        user = User(username=username, password=password)  # Crea un nuevo usuario
        db.session.add(user)  # Agrega el usuario a la base de datos
        db.session.commit()  # Guarda los cambios
        flash("Usuario registrado correctamente", "success")  # Mensaje de éxito
        return redirect(url_for("login"))  # Redirige al login

    return render_template("register.html")  # Renderiza la página de registro

# Ruta del dashboard (requiere estar autenticado)
@app.route("/dashboard")
@login_required
def dashboard():
    """Muestra el dashboard con los registros del usuario."""
    records = Record.query.filter_by(user_id=current_user.id).all()  # Obtiene los registros del usuario actual
    return render_template("dashboard.html", records=records)  # Renderiza la página del dashboard

# Ruta para agregar un nuevo registro
@app.route("/add_record", methods=["GET", "POST"])
@login_required
def add_record():
    """Formulario para agregar un nuevo registro."""
    if request.method == "POST":
        name = request.form["name"]  # Obtiene el nombre del registro
        description = request.form["description"]  # Obtiene la descripción del registro
        record = Record(name=name, description=description, user_id=current_user.id)  # Asocia el registro al usuario actual
        db.session.add(record)  # Agrega el registro a la base de datos
        db.session.commit()  # Guarda los cambios
        flash("Registro agregado", "success")  # Mensaje de éxito
        return redirect(url_for("dashboard"))  # Redirige al dashboard

    return render_template("add_record.html")  # Renderiza el formulario de agregar registro

# Ruta para editar un registro existente
@app.route("/edit_record/<int:id>", methods=["GET", "POST"])
@login_required
def edit_record(id):
    """Formulario para modificar un registro."""
    record = Record.query.get(id)  # Obtiene el registro por ID
    if request.method == "POST":
        record.name = request.form["name"]  # Actualiza el nombre del registro
        record.description = request.form["description"]  # Actualiza la descripción
        db.session.commit()  # Guarda los cambios
        flash("Registro modificado", "success")  # Mensaje de éxito
        return redirect(url_for("dashboard"))  # Redirige al dashboard

    return render_template("edit_record.html", record=record)  # Renderiza el formulario de edición

# Ruta para eliminar un registro
@app.route("/delete_record/<int:id>")
@login_required
def delete_record(id):
    """Elimina un registro de la base de datos."""
    record = Record.query.get(id)  # Obtiene el registro por ID
    db.session.delete(record)  # Elimina el registro
    db.session.commit()  # Guarda los cambios
    flash("Registro eliminado", "success")  # Mensaje de éxito
    return redirect(url_for("dashboard"))  # Redirige al dashboard

# Ruta para cerrar sesión
@app.route("/logout")
@login_required
def logout():
    """Cierra la sesión del usuario."""
    logout_user()  # Cierra la sesión del usuario actual
    return redirect(url_for("index"))  # Redirige a la página de inicio

# Inicialización del servidor Flask
if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # Crea las tablas de la base de datos si aún no existen
    app.run(debug=True)  # Inicia la aplicación Flask en modo debug
