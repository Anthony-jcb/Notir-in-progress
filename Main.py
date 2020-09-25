import time
import tkinter as tk

root=tk.Tk()
root.title("Notif")
root.config(bg="white")
frame=tk.Frame()
frame.config(bg="white")
frame.pack()

pantalla_reloj=tk.Label(frame, text="", font=("ArcaMajora3-Bold", 30), bg="white", fg="gray")
pantalla_reloj.grid(row="0", column="0")

def update_clock():

		update= time.strftime("%H:%M:%S")
		pantalla_reloj.configure(text=update)
		frame.after(1000, update_clock)

update_clock()
root.mainloop()