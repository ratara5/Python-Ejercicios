def publicarmensaje(origen, destinatario):
	print()	
	mensaje = input("Escribe un mensaje. ")
	print()
	print("-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-")
	if destinatario=="" or destinatario==" ":
		print(origen, "dice:", mensaje)
		print("-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-")
	else:
		print(origen, "dice a @"+destinatario, ": ", mensaje)
	print()