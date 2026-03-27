import tkinter as tk

from ui.app_tkinter import AppTkinter


if __name__ == "__main__":
    ventana_principal = tk.Tk()
    aplicacion = AppTkinter(ventana_principal)
    ventana_principal.mainloop()