from tkinter import Tk, Frame, Label

root= Tk()
root.title("Notir")
root.geometry("750x510")
frame_alarmas= Frame(root)
frame_alarmas.config(pady=5, padx=5)
frame_alarmas.pack(fill="x")

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