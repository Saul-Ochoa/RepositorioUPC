from tkinter import Tk,LabelFrame
import tkinter.messagebox as mb
import tkinter as tk
import sqlite3
import tkinter.messagebox as messagebox

class Menu:
    def __init__(self, root):
        self.menu = root
        self.menu.title("Productos")
        self.menu.geometry("450x500")
        self.ventana_secundaria = None
        self.ventana_usuario=None
        self.ventana_ayuda=None
        
        # Obtener las dimensiones de la pantalla
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        
        # Calcular las coordenadas x e y para centrar la ventana
        x = (screen_width - 450) // 2
        y = (screen_height - 500) // 2
        # Establecer la geometría para centrar la ventana
        self.menu.geometry(f"450x500+{x}+{y}")
        
        # Primer LabelFrame
        Frame1 = tk.LabelFrame(self.menu, text='Información del Producto', font=('Calibri', 12), bg="#f2e2cd")
        Frame1.pack(fill='both', expand=True, padx=20, pady=10)
        
        # Segundo LabelFrame dentro del primer LabelFrame
        Frame2 = tk.LabelFrame(Frame1, text='Detalles', font=('Calibri', 12), bg="#f2e2cd")
        Frame2.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Crear los botones y colocarlos en el segundo LabelFrame (Frame2) usando grid
        boton_1 = tk.Button(Frame2, text='Atributos', width=20, height=10, command=self.abrir_ventana_secundaria)
        boton_1.grid(row=2, column=1, pady=20, padx=20, sticky='nsew')
        
        boton_2 = tk.Button(Frame2, text='Usuarios', width=20, height=10, command=self.menu_usuario)
        boton_2.grid(row=2, column=2, pady=20, padx=20, sticky='nsew')
        
        boton_3 = tk.Button(Frame2, text='Salir', width=20, height=10, command=self.confirmar_salida)
        boton_3.grid(row=3, column=1, pady=20, padx=20, sticky='nsew')
        
        boton_4 = tk.Button(Frame2, text='Ayuda', width=20, height=10,command=self.abrir_ventana_ayuda)
        boton_4.grid(row=3, column=2, pady=20, padx=20, sticky='nsew')
        
    def abrir_ventana_secundaria(self):
        if not self.ventana_secundaria:
            self.ventana_secundaria = tk.Toplevel(self.menu)
            self.ventana_secundaria.title('Atributos')
            self.ventana_secundaria.geometry('650x650')
            screen_width = root.winfo_screenwidth()
            screen_height = root.winfo_screenheight()
            # Calcular las coordenadas x e y para centrar la ventana
            x = (screen_width - 650) // 2
            y = (screen_height - 650) // 2
            # Establecer la geometría para centrar la ventana
            self.ventana_secundaria.geometry(f"650x650+{x}+{y}")
            label1_secundaria = tk.Label(self.ventana_secundaria, text='Esta es la ventana secundaria')
            label1_secundaria.pack()
            self.ventana_secundaria.protocol("WM_DELETE_WINDOW", self.cerrar_ventana_secundaria)
        
    def cerrar_ventana_secundaria(self):
        if self.ventana_secundaria:
            self.ventana_secundaria.destroy()
            self.ventana_secundaria = None
        
    def menu_usuario(self):
        if not self.ventana_usuario:
            self.ventana_usuario=tk.Toplevel(self.menu)
            self.ventana_usuario.title('Usuarios')
            self.ventana_usuario.geometry('650x650')
            screen_width = root.winfo_screenwidth()
            screen_height = root.winfo_screenheight()
            # Calcular las coordenadas x e y para centrar la ventana
            x = (screen_width - 650) // 2
            y = (screen_height - 650) // 2
            # Establecer la geometría para centrar la ventana
            self.ventana_usuario.geometry(f"650x650+{x}+{y}")
            label1_secundaria=tk.Label(self.ventana_usuario,text='Esta es la ventana del menu Usuario')
            label1_secundaria.pack()
            self.ventana_usuario.protocol('WM_DELETE_WINDOW',self.cerrar_menu_usuario)
     
    def cerrar_menu_usuario(self):
        if self.ventana_usuario:
            self.ventana_usuario.destroy()
            self.ventana_usuario=None
            
    def abrir_ventana_ayuda(self):
        if not self.ventana_ayuda:
            self.ventana_ayuda=tk.Toplevel(self.menu)
            self.ventana_ayuda.title('Menu-Ayuda')
            self.ventana_ayuda.geometry('650x650')
            screen_width = root.winfo_screenwidth()
            screen_height = root.winfo_screenheight()
            # Calcular las coordenadas x e y para centrar la ventana
            x = (screen_width - 650) // 2
            y = (screen_height - 650) // 2
            # Establecer la geometría para centrar la ventana
            self.ventana_ayuda.geometry(f"650x650+{x}+{y}")
            label1_secundaria=tk.Label(self.ventana_ayuda,text='Esta es la ventana del menu Usuario')
            label1_secundaria.pack()
            self.ventana_ayuda.protocol('WM_DELETE_WINDOW',self.cerrar_ventana_ayuda)
             
    def cerrar_ventana_ayuda(self):
        if self.ventana_ayuda:
            self.ventana_ayuda.destroy()
            self.ventana_ayuda=None
            
    def confirmar_salida(self):
        respuesta=messagebox.askyesno("Confirmar Salida","¿Estas seguro que quieres Salir?")
        if respuesta:
            self.menu.quit()

if __name__ == '__main__':
    root = Tk()
    product = Menu(root)
    root.mainloop()
