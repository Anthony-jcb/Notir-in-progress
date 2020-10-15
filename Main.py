import time
from tkinter import Tk, Frame, Label
import sqlite3
from tkinter import messagebox

#-------------------------------------------#
# Módulo de Inferfaz ########################

root= Tk()
root.title("Notir")
root.geometry("750x510")
frame_alarmas= Frame(root)
frame_alarmas.config(pady=5, padx=5)
frame_alarmas.pack(fill="x")


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
	
###########################################
	
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

def alarm_label(name,description, row, column):

	"""
	"alarm_label" obtiene sus parámetros al ser
	invocada desde "database_alarms".

	Su función es mostrar en pantalla las alarmas
	que recibe desde "database_alarms". 
	"""

	frame_label_alarmas=Frame(frame_alarmas, padx=5)
	frame_label_alarmas.pack(side="left")

	label_nombre= Label(frame_label_alarmas, 
		text=str(name).strip()[2:-3],
		justify="left", 
		font=("Calibri bold", 11), 
		fg="#0092CB",
		bg="white",  
		padx=10, 
		pady=10)
	label_nombre.grid(row=row, column=column, sticky="w")

	label_descripcion= Label(frame_label_alarmas, 
		text=str(description).strip()[2:-3], 
		justify="left", 
		font=("Calibri", 9), 
		bg="white", 
		fg="gray", 
		padx=10, 
		pady=10)
	label_descripcion.grid(row=row+1, column=column, sticky="w")

#############################################

#-------------------------------------------#

# Módulo de base de datos ###################
  
def connect_database():

	"""
	"connect_database" crea la base de datos
	donde se almacena la tabla con los valores
	"ID","Nombre","Descripción" y más.
	"""

	conection= sqlite3.connect("notir_database")
	cursor= conection.cursor()

	try:
		cursor.execute("CREATE TABLE ALARMAS(ID INTEGER PRIMARY KEY AUTOINCREMENT, NOMBRE VARCHAR(20), DESCRIPCION VARCHAR(70), AVISAR VARCHAR(5), FECHA VARCHAR(10), CREADA VARCHAR(8))")
	
	except sqlite3.OperationalError:
		return "conectado a base de datos ya existente."
	
	cursor.close()
	conection.close()
	
def create_alarm():

	"""
	"create_alarm" cumple la función de crear una 
	alarma en la tabla hecha por "connect_database"
	donde almacena en forma de tupla los valores.

	*Sigue en desarrollo*, por ahora la alarma que crea
	es fija, pero en el futuro habrá un botón para
	crear la alarma de forma visual y dinámica.
	"""

	conection= sqlite3.connect("notir_database")
	cursor= conection.cursor()

	create_date= time.strftime("%H:%M:%S")
	alarm_clock= "23:00"
	alarm_date=	"2020-09-26"
	tupla_values="Estudiar JavaScript", "Necesito hacerlo porque quiero hacer páginas web", alarm_clock, alarm_date, create_date
	

	cursor.execute("INSERT INTO ALARMAS VALUES(NULL,?,?,?,?,?)", tupla_values)
	
	messagebox.showinfo("Crear alarma", "¡Alarma creada!")

	conection.commit()
	cursor.close()
	conection.close()


def database_alarms():

	"""
	"database_alarms" toma las alarmas que
	se encuentran en la tabla "Notir"
	guardandolas en variables para luego invocar 
	la función "alarm_label" pasandole los
	valores guardados, todo este proceso con 
	cada alarma guardada en la base de datos.
	"""

	conection= sqlite3.connect("notir_database")
	cursor= conection.cursor()

	cursor.execute("SELECT ID FROM ALARMAS")
	alarma_id= cursor.fetchall()
	cursor.execute("SELECT NOMBRE FROM ALARMAS")
	alarma_nombre= cursor.fetchall()
	cursor.execute("SELECT DESCRIPCION FROM ALARMAS")
	alarma_descripcion= cursor.fetchall()
	"""
	cursor.execute("SELECT AVISAR FROM ALARMAS")
	alarma_avisar= cursor.fetchall()
	cursor.execute("SELECT FECHA FROM ALARMAS")
	alarma_fecha= cursor.fetchall()
	cursor.execute("SELECT CREADA FROM ALARMAS")
	larma_creada= cursor.fetchall()
	"""

	index=0
	fila=2
	siguiente_fila=0
	columna=0

	for alarma in alarma_id:

		alarm_label(alarma_nombre[index], alarma_descripcion[index], fila, columna)

		if siguiente_fila == 2:
			fila=fila+1
			siguiente_fila=0

		else:
			siguiente_fila=siguiente_fila+1

		index=index+1
		
		
	conection.commit()
	cursor.close()
	conection.close()

#############################################

database_alarms()
update_clock()
root.mainloop()