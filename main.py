import tkinter

ventana = tkinter.Tk()  # Declaracion del GUI ,
ventana.title("La Liga Bot")  # Mensaje en el GUI
ventana.iconbitmap('fondoss.ico')
ventana.resizable(0, 0)
ventana['bg'] = '#49A'


def send():  # Enviamos Mensaje
    mensaje = mi_mensaje.get()
    mi_mensaje.set("")  # limpiar despues de enviar un mensaje
    mensaje_list.insert(tkinter.END, mensaje)


# =====================BOTON=============================
boton1 = tkinter.Button(ventana, text="Reporte de errores",
                        width=18, height=3, bg="gray", fg="black")
boton1.place(x=650, y=10)
# =====================BOTON=============================
boton2 = tkinter.Button(ventana, text="Limpiar log de errores",
                        width=18, height=3, bg="gray")
boton2.place(x=650, y=70)
# =====================BOTON=============================
boton3 = tkinter.Button(ventana, text="Reporte de Tokens",
                        width=18, height=3, bg="gray")
boton3.place(x=650, y=130)
# =====================BOTON=============================
boton4 = tkinter.Button(ventana, text="Limpiar log de Tokens",
                        width=18, height=3, bg="gray")
boton4.place(x=650, y=190)
# =====================BOTON=============================
boton5 = tkinter.Button(ventana, text="Manual de Usuario",
                        width=18, height=3, bg="gray")
boton5.place(x=650, y=250)
# =====================BOTON=============================
boton6 = tkinter.Button(ventana, text="Manual Técnico",
                        width=18, height=3, bg="gray")
boton6.place(x=650, y=310)

# PARA EL FONDO
ventana.geometry("800x500")
messages_frame = tkinter.Frame(ventana)
mi_mensaje = tkinter.StringVar()
mi_mensaje.set("")
scrollbar = tkinter.Scrollbar(messages_frame)

# PARA VER LOS MENSAJES
mensaje_list = tkinter.Listbox(
    messages_frame, height=25, width=100, yscrollcommand=scrollbar.set)
scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
mensaje_list.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
mensaje_list.pack()
messages_frame.pack()
messages_frame.place(x=20, y=20)

# PARA ESCRIBIR TEXT
entry_field = tkinter.Entry(ventana, textvariable=mi_mensaje)
entry_field.bind("<Return>", send)
entry_field.pack()
entry_field.place(x=20, y=430)
entry_field.place(width=600, height=25)
boton_enviar = tkinter.Button(ventana, text="ENVIAR", command=send)
# BOTON PARA ENVIAR MENSAJE
boton_enviar.pack()
boton_enviar.place(x=650, y=430)
boton_enviar.place(width=100, height=25)


tkinter.mainloop()  # Ejecuta el modo gráfico
