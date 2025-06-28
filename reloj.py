import tkinter as tk
import time

ventana = tk.Tk()
ventana.title('Reloj simple')
ventana.state('zoomed')  # Para pantalla completa
ventana.config(bg='#929790')

formato = tk.StringVar(ventana)
formato.set("24h")

reloj = tk.Label(ventana, font=('Arial', 120), bg="#110000", fg="#43fa04")

def hora():
    if formato.get() == "24h":
        tiempo_actual = time.strftime('%H:%M:%S')  # Formato 24 horas
    else:
        tiempo_actual = time.strftime('%I:%M:%S %p')  # Formato 12 horas con AM/PM
    reloj.config(text=tiempo_actual)
    ventana.after(1000, hora)

def cambiar_formato_automatico():
    if formato.get() == "24h":
        formato.set("12h")
    else:
        formato.set("24h")
    ventana.after(5000, cambiar_formato_automatico)

reloj.place(relx=0.5, rely=0.5, anchor='center')

cambiar_formato_automatico()
hora()
ventana.mainloop()