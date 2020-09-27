import time
import tkinter as tk
import sqlite3
from tkinter import messagebox
"""
root=tk.Tk()
root.title("Notir")
root.config(bg="white")
frame=tk.Frame()
frame.config(bg="white")
frame.pack()

pantalla_reloj=tk.Label(frame, text="", font=("ArcaMajora3-Bold", 30), bg="white", fg="gray")
pantalla_reloj.grid(row="0", column="0")
"""
"""
Investigando un poco me dí cuenta que mongoDB no es
una buena opción para este proyecto, y debido a que
no necesito usuarios decidí usar SQlite3.

"""

def update_clock():

	update= time.strftime("%H:%M:%S")
	pantalla_reloj.configure(text=update)
	frame.after(1000, update_clock)

def connect_database():

	conection= sqlite3.connect("notir_database")
	cursor= conection.cursor()

	try:
		cursor.execute("CREATE TABLE ALARMAS(NOMBRE VARCHAR(20), DESCRIPCION VARCHAR(70), AVISAR VARCHAR(5), FECHA VARCHAR(10), CREADA VARCHAR(8))")
	
	except sqlite3.OperationalError:
		return "conectado a base de datos ya existente."
	
	cursor.close()
	conection.close()
	
def create_alarm():

	conection= sqlite3.connect("notir_database")
	cursor= conection.cursor()

	create_date= time.strftime("%H:%M:%S")
	alarm_clock= "23:00"
	alarm_date=	"2020-09-26"

	tupla_values="Estudiar JavaScript", "Necesito hacerlo porque quiero hacer páginas web", alarm_clock, alarm_date, create_date
	cursor.execute("INSERT INTO ALARMAS VALUES(?,?,?,?,?)",(tupla_values))
	
	messagebox.showinfo("Crear alarma", "¡Alarma creada!")

	conection.commit()
	cursor.close()
	conection.close()


#update_clock()
connect_database()
create_alarm()
#root.mainloop()