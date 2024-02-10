from tkinter import ttk
from tkinter import *
import tkinter.messagebox as mb
import sqlite3

class Productos:
    base='D:\Python\Tkinter\Aplicación de escritorio en python\productos.db'
    def __init__(self, root):
        self.menu = root
        self.menu.title("Productos")
        self.menu.geometry("850x600")

        # Crear marcos
        frame1 = LabelFrame(self.menu, text="Información del Producto", font=('Calibri', 12), bg="#f2e2cd")
        frame1.pack(fill='both', expand='yes', padx=20, pady=10)

        frame2 = LabelFrame(self.menu, text="Datos del Producto", font=('Calibri', 12), bg="#f2e2cd")
        frame2.pack(fill='both', expand='yes', padx=20, pady=10)

        # Crear Treeview en el primer marco
        self.trv = ttk.Treeview(frame1, columns=(1, 2, 3, 4), show='headings', height='5')
        self.trv.pack(side="left", fill="both", expand=True)

        # Crear Scrollbar en un marco diferente dentro de frame1
        scrollbar_frame = Frame(frame1)
        scrollbar_frame.pack(side="right", fill="y")

        scrollbar_y = ttk.Scrollbar(scrollbar_frame, orient="vertical", command=self.trv.yview)
        scrollbar_y.pack(fill="y")

        # Configurar la interacción entre el Scrollbar y el Treeview
        self.trv.configure(yscrollcommand=scrollbar_y.set)

        # Definir los encabezados del Treeview
        self.trv.heading(1, text='ID del Producto')
        self.trv.heading(2, text="Nombre del Producto")
        self.trv.heading(3, text="Precio del Producto")
        self.trv.heading(4, text="Cantidad del Producto")

        # Llamar al método consulta() (asumiendo que está definido en tu clase)
        self.consulta()
        
        label1=Label(frame2,text='ID del Producto')
        label1.grid(row=0,column=0,padx=5,pady=3)
        label2=Label(frame2,text='Nombre del Producto')
        label2.grid(row=1,column=0,padx=5,pady=3)
        label3=Label(frame2,text='Precio del Producto')
        label3.grid(row=2,column=0,padx=5,pady=3)
        label4=Label(frame2,text='Cantidad del Producto')
        label4.grid(row=3,column=0,padx=5,pady=3)
        
        self.entry1=Entry(frame2)
        self.entry1.grid(row=0,column=1,padx=5,pady=3)
        self.entry2=Entry(frame2)
        self.entry2.grid(row=1,column=1,padx=5,pady=3)
        self.entry3=Entry(frame2)
        self.entry3.grid(row=2,column=1,padx=5,pady=3)
        self.entry4=Entry(frame2)
        self.entry4.grid(row=3,column=1,padx=5,pady=3)
        
        button1=Button(frame2,text='Agregar',width=12,height=2,command=self.agregar,bg="#FF6666",fg="#ffffff")
        button1.grid(row=0,column=3,padx=10, pady=6)
        button2=Button(frame2,text='Eliminar',width=12,height=2,bg="#FF6666",command=self.eliminar,fg="#ffffff")
        button2.grid(row=1,column=3,padx=10,pady=6)
        button3=Button(frame2,text='Actualizar',width=12,height=2,bg="#FF6666",command=self.Actualizar,fg="#ffffff")
        button3.grid(row=2,column=3,padx=10,pady=6)
        
          
    def run_query(self,query,parameters=()):
        with sqlite3.connect(self.base) as conn:
            cursor=conn.cursor()
            result=cursor.execute(query,parameters)
            conn.commit()
            return result
        
    def consulta(self):
        book=self.trv.get_children()
        for element in book:
            self.trv.delete(element)
        query='SELECT id,nombre,precio,cantidad FROM Articulos'
        rows=self.run_query(query)
        for row in rows:
            self.trv.insert('',0,text=row[1],values=row)
        
    def validation(self):
        return len(self.entry1.get()) !=0 and len(self.entry2.get()) !=0 and len(self.entry3.get())  !=0 and len(self.entry4.get())  !=0
        
    def agregar(self):
        if self.validation():
            query='INSERT INTO Articulos VALUES(?,?,?,?)'
            parameters=(self.entry1.get(),self.entry2.get(),self.entry3.get(),self.entry4.get())
            self.run_query(query,parameters)
            self.entry1.delete(0,END)
            self.entry2.delete(0,END)
            self.entry3.delete(0,END)
            self.entry4.delete(0,END)
        else:
            mb.showwarning("Advertencia", "Los datos no están completos. Por favor, complete todos los campos.")
        self.consulta()
        
    def eliminar(self):
        try:
            item = self.trv.selection()
            if not item:
                raise IndexError("No hay elementos seleccionados.")
            
            nombre = self.trv.item(item)['text']
            
            # Mostrar un cuadro de diálogo de confirmación
            respuesta = mb.askyesno("Confirmar eliminación", f"¿Estás seguro de que deseas eliminar '{nombre}'?")
            
            if respuesta:
                query = 'DELETE FROM Articulos WHERE nombre = ?'
                self.run_query(query, (nombre,)) 
                self.consulta() 
        except IndexError as e:
            return            
    ## Mejorar el codigo de Actualizar
    def Actualizar(self):
        if not self.trv.selection():
            mb.showwarning("Advertencia","Debes seleccionar un dato para actualizar.")
            return  
        try:
            precio = self.trv.item(self.trv.selection())['values'][2]
            cantidad = self.trv.item(self.trv.selection())['values'][3] 
            self.edit_wind = Toplevel()
            self.edit_wind.title("Actualizar")
            self.edit_wind.geometry("400x300")

            frame = LabelFrame(self.edit_wind, text="Actualizar Producto",  font=("Calibri", 12))
            frame.pack(fill="both", expand="yes", padx=20, pady=10)  

            Label(frame, text="Antiguo Precio:", width=15, font=("Calibri", 10)).grid(row=2, column=1, padx=10, pady=20)
            Entry(frame, textvariable = StringVar(frame, value = precio), state = 'readonly').grid(row=2, column=2)

            Label(frame, text="Nuevo Precio", width=15, font=("Calibri", 10)).grid(row=3, column=1)
            nue_vo = Entry(frame)
            nue_vo.grid(row=3, column=2)

            Label(frame, text="Antigua Cantidad:", width=15, font=("Calibri", 10)).grid(row=4, column=1, padx=10, pady=20)
            Entry(frame, textvariable = StringVar(frame, value = cantidad), state = 'readonly').grid(row=4, column=2)


            Label(frame, text="Nueva Cantidad", width=15, font=("Calibri", 10)).grid(row=5, column=1)
            nueva = Entry(frame)
            nueva.grid(row=5, column=2)

            Button(frame, text="Actualizar", command = lambda: self.edit_record(nue_vo.get(), precio, nueva.get(), cantidad), width=12, height=2).grid(row=7, column=2, pady=20)
        except IndexError as e:
            mb.showwarning("Advertencia","Debes selecionar un dato valido para actualizar")

    def edit_record(self, nue_vo, precio, nueva, cantidad): 
        query = 'UPDATE articulos SET precio = ?, cantidad = ? WHERE precio = ? AND cantidad = ?'
        parameters = (nue_vo, nueva, precio, cantidad) 
        self.run_query(query, parameters)
        self.edit_wind.destroy()
        self.consulta()  
    
if __name__ == '__main__':
    root=Tk()
    product=Productos(root)
    root.mainloop()