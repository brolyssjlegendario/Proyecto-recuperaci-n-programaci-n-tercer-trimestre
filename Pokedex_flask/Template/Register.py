from flask import Blueprint, render_template, request, redirect, url_for, flash  # Importa las funciones necesarias de Flask
from werkzeug.security import generate_password_hash  # Permite encriptar contraseñas de manera segura
from models import db, User  # Importa la base de datos y el modelo de usuario

# Crea un Blueprint para modularizar las rutas de registro
register_bp = Blueprint('register', __name__, template_folder='templates')

@register_bp.route("/register", methods=["GET", "POST"])
def register():
    """Maneja el registro de nuevos usuarios."""
    if request.method == "POST":  # Verifica si el usuario envió el formulario
        username = request.form["username"]  # Obtiene el nombre de usuario del formulario
        password = generate_password_hash(request.form["password"], method="pbkdf2:sha256")  
        # Encripta la contraseña antes de guardarla en la base de datos

        # Verifica si el usuario ya existe en la base de datos
        existing_user = User.query.filter_by(username=username).first()  
        if existing_user:
            flash("El usuario ya existe. Prueba con otro nombre.", "error")  # Muestra mensaje de error
            return redirect(url_for("register.register"))  # Redirige al formulario de registro

        # Crea un nuevo usuario y lo guarda en la base de datos
        new_user = User(username=username, password=password)  
        db.session.add(new_user)  # Agrega el usuario a la base de datos
        db.session.commit()  # Guarda los cambios en la base de datos
        flash("Usuario registrado exitosamente. Ahora puedes iniciar sesión.", "success")  
        # Muestra mensaje de éxito
        
        return redirect(url_for("login"))  # Redirige al login después del registro exitoso

    return render_template("register.html")  # Renderiza la página de registro si el método es GET
