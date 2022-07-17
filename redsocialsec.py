# Proyecto RED SOCIAL
# Importar archivos con funciones
import redsocial_solicitarperfil
import redsocial_mostrarperfil
import redsocial_publicarmensaje
import redsocial_opciones
print("Bienvenido a ... ")
print("""              _                  __
               __ ___.                  __    
______   _____/  |\_ |__   ____   ____ |  | __
\____ \_/ __ \   __\ __ \ /  _ \ /  _ \|  |/ /
|  |_> >  ___/|  | | \_\ (  <_> |  <_> )    < 
|   __/ \___  >__| |___  /\____/ \____/|__|_ \
|__|        \/         \/                   \/
""")
# Solicitar los datos al usuario.
# redsocial_solicitarperfil.solicitarperfil()
(nombre, edad, estatura_m, estatura_cm, num_amigos, genero, pais)=redsocial_solicitarperfil.solicitarperfil()
# Mostrar los datos del usuario
redsocial_mostrarperfil.mostrarperfil(nombre, edad, estatura_m, estatura_cm, num_amigos, genero, pais)
# Solicitar mensaje de prueba
redsocial_publicarmensaje.publicarmensaje(nombre, " ")
# Solicitar más datos e informar todo el perfil ¿¿??
#Variable boole y ciclo para que el usuario siga activo
opcion = 1
while opcion != 0:
    opcion=redsocial_opciones.opciones()
    #Código para la opción 1. Publicar un mensaje.
    if opcion == 1:
        redsocial_publicarmensaje.publicarmensaje(nombre, " ")

    #Código para la opción 2. Publicar un mensaje a un grupo de personas.
    elif opcion == 2:
        print()
        for i in range(num_amigos):
            nombre_amigo = input("Ingresa el nombre de tu amigo o amiga número "+str(i+1)+" : ")
            redsocial_publicarmensaje.publicarmensaje(nombre, nombre_amigo)

    #Código para la opción 3. Publicar los datos del perfil del usuario.
    elif opcion == 3:
        redsocial_mostrarperfil.mostrarperfil(nombre, edad, estatura_m, estatura_cm, num_amigos, genero, pais)

    #Código para la opción 4. Actualizar los datos del perfil del usuario.
    elif opcion == 4:
        (nombre, edad, estatura_m, estatura_cm, num_amigos, genero, pais)=redsocial_solicitarperfil.solicitarperfil()
		
    #Código para la opción 0. Salir.
    elif opcion == 0:
        print("Has decidido salir.")

    #Código para la opción que no coincida con ninguna anterior.
    else:
        print("No conozco la opción que has ingresado. Inténtalo otra vez.")

print()
print("Gracias por usar Mi Red. ¡Hasta pronto!")
print()