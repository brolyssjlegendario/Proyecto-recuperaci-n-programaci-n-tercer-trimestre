Instrucciones de uso del programa Pokédex con Flask, organizadas por pasos:

1. Instalación de dependencias
Antes de ejecutar el programa, asegúrate de instalar las bibliotecas necesarias. En la terminal, ejecuta:
```bash
pip install flask flask-login flask-sqlalchemy werkzeug
```

2. Ejecutar la aplicación
Para iniciar la aplicación, abre una terminal en la carpeta del proyecto y ejecuta:
```bash
python app.py
```
Esto iniciará el servidor Flask y podrás acceder desde tu navegador en `http://127.0.0.1:5000/`.

---

3. Registro e inicio de sesión
Accede a la página de inicio en `http://127.0.0.1:5000/`, haz clic en "Registrarse" para crear un nuevo usuario, ingresa un nombre de usuario y contraseña y confirma el registro. Luego, en la página de inicio, haz clic en "Iniciar sesión" e ingresa tus credenciales.

4 Usar el Dashboard
Una vez que inicies sesión, serás redirigido al Dashboard, donde puedes:
- Ver tus Pokémon capturados o registros almacenados.
- Añadir un nuevo Pokémon o registro.
- Editar los detalles de un Pokémon o registro.
- Eliminar un Pokémon o registro (requiere confirmación).

5. Añadir un nuevo registro
Desde el Dashboard, haz clic en "agregar nuevo registro". Completa todos los campos necesarios, haz clic en guardar registro y serás redirigido al Dashboard 

6. Editar un registro
En el Dashboard, encuentra el registro que quieres modificar, haz clic en "Editar" en el registro correspondiente, edítalo y regresa al Dashboard 

7. Eliminar un registro
En el Dashboard, busca el registro que deseas eliminar, haz clic en "Eliminar", se mostrará una confirmación. Acepta la eliminación y el registro desaparecerá de la lista.

8. Cerrar sesión
Haz clic en **"Cerrar sesión"** en la parte superior del Dashboard y serás redirigido a la página de inicio.
