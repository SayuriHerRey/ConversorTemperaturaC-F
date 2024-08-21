
import tkinter as tk
def reset():
    tbCelcius.delete(0, tk.END)
    tbCelcius.insert(0, "0.0")
    tbFahrenheit.delete(0, tk.END)
    tbFahrenheit.insert(0, "0.0")

def Fahrenheit_celsius():
    Fahrenheit = float(tbFahrenheit.get())
    Celsius = (Fahrenheit-32)*5/9
    tbCelcius.delete(0,tk.END)
    tbCelcius.insert(0, f"{Celsius: .2f}")
    
def Celcius_Fahrenheit():
    Celcius = float(tbCelcius.get())
    Fahrenheit = (Celcius*9/5)+32
    tbFahrenheit.delete(0,tk.END)
    tbFahrenheit.insert(0, f"{Fahrenheit: .2f}")

ventana = tk.Tk()
ventana.title("Actividad 03 - Coneversor de Temperatura - Python")

lbFahrenheit = tk.Label(ventana, text="Fahrenheit: ")
lbFahrenheit.grid(row=0, column=0)

tbFahrenheit = tk.Entry(ventana)
tbFahrenheit.grid(row=0, column=1)
    
btnFahrenheit = tk.Button(ventana, text= "  Convertir a Celsius", command=Fahrenheit_celsius)
btnFahrenheit.grid(row=0, column=2)

lbCelcius = tk.Label(ventana, text="Celcius: ")
lbCelcius.grid(row=1, column=0)

tbCelcius = tk.Entry(ventana)
tbCelcius.grid(row=1, column=1)
    
btnCelcius = tk.Button(ventana, text= "Convertir a Fahrenheit", command=Celcius_Fahrenheit)
btnCelcius.grid(row=1, column=2)

btnRestablecer = tk.Button(ventana, text= "Restablecer", command=reset)
btnRestablecer.grid(row=2, column=1)

ventana.mainloop()