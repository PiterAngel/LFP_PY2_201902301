from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import tkinter
from tkinter import scrolledtext

top = tkinter.Tk()  # Declaracion del GUI ,
top.title("La Liga Bot")  # Mensaje en el GUI
top.iconbitmap('fondoss.ico')
top.resizable(0, 0)
top['bg'] = '#49A'


def send(event=None):  # Enviamos Mensaje
    mensaje = mi_ms.get()
    mi_ms.set("")  # limpia despues de enviar
    #client_socket.send(bytes(mensaje, "utf8"))
    # Insertamos el mensaje que escribimos en relacion al Gui
    mensaje_list.insert(tkinter.END, mensaje)


# =====================BOTON=============================
boton1 = tkinter.Button(top, text="Reporte de errores",
                        width=18, height=3, bg="gray", fg="black")
boton1.place(x=650, y=10)
# =====================BOTON=============================
boton2 = tkinter.Button(top, text="Limpiar log de errores",
                        width=18, height=3, bg="gray")
boton2.place(x=650, y=70)
# =====================BOTON=============================
boton3 = tkinter.Button(top, text="Reporte de Tokens",
                        width=18, height=3, bg="gray")
boton3.place(x=650, y=130)
# =====================BOTON=============================
boton4 = tkinter.Button(top, text="Limpiar log de Tokens",
                        width=18, height=3, bg="gray")
boton4.place(x=650, y=190)
# =====================BOTON=============================
boton5 = tkinter.Button(top, text="Manual de Usuario",
                        width=18, height=3, bg="gray")
boton5.place(x=650, y=250)
# =====================BOTON=============================
boton6 = tkinter.Button(top, text="Manual Técnico",
                        width=18, height=3, bg="gray")
boton6.place(x=650, y=310)

# top = scrolledtext.ScrolledText(
#    top, width=100, height=20,)
#top.grid(column=0, row=0, padx=100, pady=100)
top.geometry("800x500")
messages_frame = tkinter.Frame(top)  # Insertamos en el area de texto
mi_ms = tkinter.StringVar()  # Espera mensaje
mi_ms.set("")
scrollbar = tkinter.Scrollbar(messages_frame)  # Barra deslisable

# Contenido del area de mensaje
mensaje_list = tkinter.Listbox(
    messages_frame, height=25, width=100, yscrollcommand=scrollbar.set)  # Propiedades del Gui
scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
mensaje_list.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
mensaje_list.pack()
messages_frame.pack()
messages_frame.place(x=20, y=20)

# Area o campo para escribir y boton enviar
entry_field = tkinter.Entry(top, textvariable=mi_ms)
entry_field.bind("<Return>", send)
entry_field.pack()
entry_field.place(x=20, y=430)
entry_field.place(width=600, height=25)
send_button = tkinter.Button(top, text="ENVIAR", command=send)
# BOTON
send_button.pack()
send_button.place(x=650, y=430)
send_button.place(width=100, height=25)


tkinter.mainloop()  # Ejecuta el modo grafico
