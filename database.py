# Módulo de base de datos ###################
import sqlite3
import time
from tkinter import messagebox
from interfaz import alarm_label

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
		print("Conexión realizada")
	
	cursor.close()
	conection.close()

#############################################

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

#############################################

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