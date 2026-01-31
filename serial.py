import tkinter as tk
import serial
# Kommunikation
daten = serial.Serial('COM3', 9600)
# Function
def ledSchalten():
    if ledButton["text"] == "EIN":
        ledButton["text"] = "AUS"
        daten.write(bytes('e1' + '\r', 'utf-8'))
    else:
        ledButton["text"] = "EIN"
        daten.write(bytes('a1' + '\r', 'utf-8'))
# Display
window = tk.Tk()
window.title("LED Steuerung")
ledButton = tk.Button(bg = 'GREY', text = "KLICKEN HIER!", width = 40, command = ledSchalten)
ledButton.pack()
# Loop
window.mainloop()
