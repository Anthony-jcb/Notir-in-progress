import time
import tkinter as tk
import sqlite3

root=tk.Tk()
root.title("Notir")
root.config(bg="white")
frame=tk.Frame()
frame.config(bg="white")
frame.pack()

pantalla_reloj=tk.Label(frame, text="", font=("ArcaMajora3-Bold", 30), bg="white", fg="gray")
pantalla_reloj.grid(row="0", column="0")

"""
Para almacenar las alarmas necesitaría utilizar una base de datos
MongoDB será el lenguaje que empezaré a aprender ahora mismo para
implementarlo en este proyecto, espero no tardar más de lo creo.

"""

def update_clock():

	update= time.strftime("%H:%M:%S")
	pantalla_reloj.configure(text=update)
	frame.after(1000, update_clock)

def conect_database():

	conection= sqlite3.connect("notir_database")
	cursor= conection.cursor()

	#"En proceso"# cursor.execute("CREATE TABLE Alarma")

update_clock()
root.mainloop()