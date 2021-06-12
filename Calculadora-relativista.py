import numpy
import os


numpy.seterr('ignore')
luz = int(300000000)

while True:


	inicio = input("¿que deseas?(entrar, salir o limpiar): \n>")
	print ("")
	
	if inicio == "entrar" or inicio == "enter":
		
		opcion = input("elige la magnitud(energia, fuerza o recorrido): \n>")
	
		if opcion == "energia" or opcion == "energy" or opcion == "energi":	
	
				try:
					print(" ")
					masa_en_reposo = float(input("ingresa la masa (kg): \n>"))
					
					print(" ")
					aceleracion = float(input("ingresa la aceleracion (m/s): \n>"))
					
					if aceleracion > (luz):
							print ("las ecuaciones de einstein impiden velocidades superluminicas por lo que intentarlo conlleva numeros “rotos” aun así, si te interesa ver el resultado, elimina esta condicion del codigo y veras un “nan”.")
							print("")

					else:
						
						relatividad = (masa_en_reposo/(numpy.sqrt(1-(aceleracion**2)/luz**2)))
				
						energia = (0.5*(relatividad * (aceleracion**2)))
				
						print ("la energia usada son:", energia,"J\n")
				
				
						
				
				except:
					
						print("")
						print(" ")
						
					
					
		elif opcion == "fuerza" or opcion == "momento lineal" or opcion == "momentum" or opcion == "impetú":
			
				try:
					
					print("")
					masa_en_reposo = float(input("ingresa la masa (kg): \n>"))
					
					print(" ")
					aceleracion = float(input("ingresa la aceleracion (m/s): \n>"))
					
					print(" ")
					
					if (aceleracion) > (luz):
						print ("las ecuaciones de einstein impiden velocidades superluminicas por lo que intentarlo conlleva numeros “rotos” aun así, si te interesa ver el resultado, elimina esta condicion del codigo y veras un “nan”.")
						print("")
						
					else:
				
						relatividad = (masa_en_reposo/(numpy.sqrt(1-(aceleracion**2)/luz**2)))
				
						fuerza = (relatividad * aceleracion)
					
						peso = (fuerza/9.81)
					
						print ("la fuerza (newtons) es:",fuerza,"N")
					
						print (" ")
					
						print("la fuerza (kilogramos) es:", peso, "kg/f\n")
						
					
						print(" ")
			
				except:
				
					print("")
					print(" ")
		elif opcion == "recorrido":
			try:
				
				print(" ")
				espacio = float(input("ingresa la distancia a recorrer(m):\n>"))
				print(" ")
				
			
				
				velocidad = float(input("ingresa la velocidad (m/s): \n>"))
				print("")
				
				if velocidad > (luz):
					print ("las ecuaciones de einstein impiden velocidades superluminicas por lo que intentarlo conlleva numeros “rotos” aun así, si te interesa ver el resultado, elimina esta condicion del codigo y veras un “nan”.")
				
					print("")
				
				else:
					relatividad = (espacio *(numpy.sqrt(1-(velocidad**2)/(luz**2))))
					
					dilatacion = (1*(numpy.sqrt(1-(velocidad**2)/(luz**2))))
				
					tiempo = (relatividad/velocidad)
					
					total= (tiempo/dilatacion)
				
					print ("recorrer la distancia de", espacio,"metros", "toma", tiempo, "segundos")
					print(" ")
				
			except:
				print("")
					
		else:
			
				print("")
	
	elif inicio == "salir" or inicio == "exit":
		break			
	elif inicio == "limpiar" or inicio == "clean":
		if os.name == "posix":
			
			os.system ("clear")
		
		elif os.name == "ce" or os.name == "nt" or os.name == "dos":
			
			os.system ("cls")
				
	else:
		print("ingresa opcion valida")
		print(" ")
