import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import time

# Función para verificar las credenciales de login
def verificar_credenciales():
    usuario = entry_usuario.get()
    contrasena = entry_contrasena.get()
    
    # Aquí se puede añadir la lógica para verificar las credenciales
    # en este caso con un usuario y contraseña predefinidas (ESTO ES UN EJEMPLO POR AHORA) hay que hacer clases 
    # y llamarlos
    if usuario == "Kevin" and contrasena == "12345":
        messagebox.showinfo("Login exitoso", "Bienvenido, Kevin")
    else:
        messagebox.showerror("Error de login", "Usuario o contraseña incorrectos")

# Muestra la animación
def mostrar_animacion():
    animacion = tk.Toplevel()
    animacion.title("Bienvenido")
    animacion.geometry("400x300")
    animacion.overrideredirect(True)  # Elimina la barra de título

    # Carga lo que es el logo
    #No me muestra el logoooooo
    logo = Image.open("assets\logo.jpg")
    
    # Esto de aca abajo tuve el problema con el path donde no me tomaba la imagen
    # igualmente por el foro que use para entender esto usaba el comando ANTIALIAS que es antiguo y no
    # funciona actualmente sino hay que cambiarlo por el LANCZOS
    logo = logo.resize((200, 200), Image.LANCZOS)
    logo_img = ImageTk.PhotoImage(logo)

    # widgets para la animación
    label_logo = tk.Label(animacion, image=logo_img)
    label_logo.pack(pady=20)
    label_mensaje = tk.Label(animacion, text="Bienvenido", font=("Helvetica", 16))
    label_mensaje.pack()

    # Mostrar la animación por 3 segundos
    ventana.after(3000, animacion.destroy)

# Ventana
ventana = tk.Tk()
ventana.title("Login")

# Mostrar la animación
mostrar_animacion()

# Widgets en la ventana principal
label_usuario = tk.Label(ventana, text="Usuario")
label_usuario.pack(pady=5)
entry_usuario = tk.Entry(ventana)
entry_usuario.pack(pady=5)

label_contrasena = tk.Label(ventana, text="Contraseña")
label_contrasena.pack(pady=5)
entry_contrasena = tk.Entry(ventana, show="*")
entry_contrasena.pack(pady=5)

boton_login = tk.Button(ventana, text="Login", command=verificar_credenciales)
boton_login.pack(pady=20)

# Ejecutar la aplicación principal
ventana.mainloop()
