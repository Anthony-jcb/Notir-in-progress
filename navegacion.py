from tkinter import Frame, Label
from interfaz import root
import time

"""
En la "barra superior" se encuentran
"linea_superior" y "reloj_superior".
"""	
barra_superior= Frame(root)
barra_superior.config(height="430", bg="white")
barra_superior.pack(fill="x", side="top")

reloj_superior= Label(barra_superior, text="", font=("ArcaMajora3-Bold", 19), bg="white", fg="#0092CB", padx=2)
reloj_superior.grid(row=0, column=0)


"""
"linea_superior" solo es la línea de color
que aparece debajo de "barra_superior".

En "Dark Mode" se tiñe de color oscuro.
"""
		
linea_superior=Frame(root)
linea_superior.config(height="2", bg="#0094D5")
linea_superior.pack(fill="x")

def update_clock():

	"""
	"update_clock" actualiza cada 1 segundo
	el reloj que se encuentra en "barra_superior".
	"""

	update= time.strftime("%H:%M:%S")
	reloj_superior.configure(text=update)
	barra_superior.after(1000, update_clock)

def dark_mode():

	"""
	"dark_mode" cambia a color oscuro algunos
	elementos de la interfaz.
	"""
	
	reloj_superior.config(bg="#333333")
	barra_superior.config(bg="#333333")
	linea_superior.config(bg="#141414")
	root.config(bg="#141414")