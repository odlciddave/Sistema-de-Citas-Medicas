import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import os

# Creacion de los archivos CSV necesarios para el sistema
archivos = ["doctores.csv", "pacientes.csv", "citas.csv", "horarios.csv"]
for archivo in archivos:
    if not os.path.exists(archivo):
        with open(archivo, "a"):
            pass

class SistemaCitas(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sistema de Citas Médicas")
        self.geometry("400x550") # Hice la ventana un poco más alta para que quepa el nuevo botón
        self.config(bg="#f0f0f0")

        # Título principal
        tk.Label(self, text="Sistema de Citas Médicas", font=("Arial", 16, "bold"), bg="#f0f0f0").pack(pady=20)

        # Botones del menú
        botones = [
            ("Registrar Doctor", self.abrir_registro_doctor),
            ("Registrar Paciente", self.abrir_registro_paciente),
            ("Registrar Horario", self.abrir_registro_horario),
            ("Agendar Cita", self.abrir_agendar_cita),
            ("Consultar Historial", self.abrir_consultar_historial),
            ("Reportes por Doctor", self.abrir_reportes),
            ("Ver Lista de Doctores", self.abrir_lista_doctores) # <-- NUEVO BOTON AGREGADO AQUI
        ]

        for texto, comando in botones:
            tk.Button(self, text=texto, command=comando, width=30, font=("Arial", 12)).pack(pady=5)

        tk.Button(self, text="Salir", command=self.quit, width=30, font=("Arial", 12), bg="#ff4d4d", fg="white").pack(pady=20)

    # --- MODULO 1: REGISTRAR DOCTOR ---
    def abrir_registro_doctor(self):
        ventana = tk.Toplevel(self)
        ventana.title("Registrar Doctor")
        ventana.geometry("300x250")

        tk.Label(ventana, text="ID del Doctor:").pack(pady=5)
        entry_id = tk.Entry(ventana)
        entry_id.pack()

        tk.Label(ventana, text="Nombre del Doctor:").pack(pady=5)
        entry_nombre = tk.Entry(ventana)
        entry_nombre.pack()

        tk.Label(ventana, text="Especialidad:").pack(pady=5)
        entry_especialidad = tk.Entry(ventana)
        entry_especialidad.pack()

        def guardar_doctor():
            id_doc = entry_id.get().strip()
            nombre = entry_nombre.get().strip()
            especialidad = entry_especialidad.get().strip()

            if not id_doc or not nombre or not especialidad:
                messagebox.showwarning("Error", "Todos los campos son obligatorios.")
                return

            existe = False
            with open("doctores.csv", "r") as f:
                for linea in f:
                    datos = linea.strip().split(",")
                    if len(datos) >= 1 and datos[0] == id_doc:
                        existe = True
                        break

            if existe:
                messagebox.showerror("Error", "El ID del doctor ya existe.")
            else:
                with open("doctores.csv", "a") as f:
                    f.write(f"{id_doc},{nombre},{especialidad}\n")
                messagebox.showinfo("Éxito", "Doctor registrado correctamente.")
                ventana.destroy()

        tk.Button(ventana, text="Guardar", command=guardar_doctor).pack(pady=15)

    # --- MODULO 2: REGISTRAR PACIENTE ---
    def abrir_registro_paciente(self):
        ventana = tk.Toplevel(self)
        ventana.title("Registrar Paciente")
        ventana.geometry("300x250")

        tk.Label(ventana, text="Carnet del Paciente:").pack(pady=5)
        entry_carnet = tk.Entry(ventana)
        entry_carnet.pack()

        tk.Label(ventana, text="Nombre:").pack(pady=5)
        entry_nombre = tk.Entry(ventana)
        entry_nombre.pack()

        tk.Label(ventana, text="Edad:").pack(pady=5)
        entry_edad = tk.Entry(ventana)
        entry_edad.pack()

        def guardar_paciente():
            carnet = entry_carnet.get().strip()
            nombre = entry_nombre.get().strip()
            edad = entry_edad.get().strip()

            if not carnet or not nombre or not edad:
                messagebox.showwarning("Error", "Todos los campos son obligatorios.")
                return

            existe = False
            with open("pacientes.csv", "r") as f:
                for linea in f:
                    datos = linea.strip().split(",")
                    if len(datos) >= 1 and datos[0] == carnet:
                        existe = True
                        break

            if existe:
                messagebox.showerror("Error", "El carnet ya está registrado.")
            else:
                with open("pacientes.csv", "a") as f:
                    f.write(f"{carnet},{nombre},{edad}\n")
                messagebox.showinfo("Éxito", "Paciente registrado.")
                ventana.destroy()

        tk.Button(ventana, text="Guardar", command=guardar_paciente).pack(pady=15)

    # --- MODULO 3: REGISTRAR HORARIO ---
    def abrir_registro_horario(self):
        ventana = tk.Toplevel(self)
        ventana.title("Registrar Horario")
        ventana.geometry("300x250")

        tk.Label(ventana, text="ID del Doctor:").pack(pady=5)
        entry_id = tk.Entry(ventana)
        entry_id.pack()

        tk.Label(ventana, text="Fecha (DD-MM-AAAA):").pack(pady=5)
        entry_fecha = tk.Entry(ventana)
        entry_fecha.pack()

        tk.Label(ventana, text="Hora (HH:MM):").pack(pady=5)
        entry_hora = tk.Entry(ventana)
        entry_hora.pack()

        def guardar_horario():
            id_doc = entry_id.get().strip()
            fecha = entry_fecha.get().strip()
            hora = entry_hora.get().strip()

            doctor_existe = False
            with open("doctores.csv", "r") as f:
                for linea in f:
                    datos = linea.strip().split(",")
                    if len(datos) >= 1 and datos[0] == id_doc:
                        doctor_existe = True
                        break
            
            if not doctor_existe:
                 messagebox.showerror("Error", "El doctor no existe.")
                 return

            with open("horarios.csv", "a") as f:
                f.write(f"{id_doc},{fecha},{hora}\n")
            messagebox.showinfo("Éxito", "Horario registrado.")
            ventana.destroy()

        tk.Button(ventana, text="Guardar", command=guardar_horario).pack(pady=15)

    # --- MODULO 4: AGENDAR CITA ---
    def abrir_agendar_cita(self):
        ventana = tk.Toplevel(self)
        ventana.title("Agendar Cita")
        ventana.geometry("300x350")

        tk.Label(ventana, text="Carnet del Paciente:").pack(pady=5)
        entry_carnet = tk.Entry(ventana)
        entry_carnet.pack()

        tk.Label(ventana, text="ID del Doctor:").pack(pady=5)
        entry_id_doc = tk.Entry(ventana)
        entry_id_doc.pack()

        tk.Label(ventana, text="Fecha (DD-MM-AAAA):").pack(pady=5)
        entry_fecha = tk.Entry(ventana)
        entry_fecha.pack()
        
        tk.Label(ventana, text="Hora (HH:MM):").pack(pady=5)
        entry_hora = tk.Entry(ventana)
        entry_hora.pack()

        def agendar():
            carnet = entry_carnet.get().strip()
            id_doc = entry_id_doc.get().strip()
            fecha = entry_fecha.get().strip()
            hora = entry_hora.get().strip()
            
            if not carnet or not id_doc or not fecha or not hora:
                messagebox.showwarning("Error", "Llene todos los campos.")
                return
            
            # 1. Validar Paciente
            paciente_existe = False
            with open("pacientes.csv", "r") as f:
                for linea in f:
                    datos = linea.strip().split(",")
                    if len(datos) >= 3 and datos[0] == carnet:
                        paciente_existe = True
                        break
            if not paciente_existe:
                messagebox.showerror("Error", "El paciente no está registrado.")
                return

            # 2. Validar Doctor
            doctor_existe = False
            with open("doctores.csv", "r") as f:
                for linea in f:
                    datos = linea.strip().split(",")
                    if len(datos) >= 3 and datos[0] == id_doc:
                        doctor_existe = True
                        break
            if not doctor_existe:
                messagebox.showerror("Error", "El doctor no existe.")
                return

            # 3. Validar Horario habilitado
            horario_existe = False
            with open("horarios.csv", "r") as f:
                for linea in f:
                    datos = linea.strip().split(",")
                    if len(datos) >= 3 and datos[0] == id_doc and datos[1] == fecha and datos[2] == hora:
                        horario_existe = True
                        break
            if not horario_existe:
                messagebox.showerror("Error", "El doctor no tiene ese horario disponible.")
                return

            # 4. Validar Traslape
            cita_ocupada = False
            with open("citas.csv", "r") as f:
                for linea in f:
                    datos = linea.strip().split(",")
                    if len(datos) >= 4 and datos[1] == id_doc and datos[2] == fecha and datos[3] == hora:
                        cita_ocupada = True
                        break
            if cita_ocupada:
                messagebox.showerror("Error", "Este horario ya está ocupado (Traslape).")
                return

            # Si pasa todas las validaciones, se guarda
            with open("citas.csv", "a") as f:
                f.write(f"{carnet},{id_doc},{fecha},{hora}\n")
            messagebox.showinfo("Éxito", "Cita agendada exitosamente.")
            ventana.destroy()

        tk.Button(ventana, text="Agendar", command=agendar).pack(pady=15)

    # --- MODULO 5: CONSULTAR HISTORIAL ---
    def abrir_consultar_historial(self):
        ventana = tk.Toplevel(self)
        ventana.title("Historial de Paciente")
        ventana.geometry("450x350")

        tk.Label(ventana, text="Ingrese Carnet del Paciente:").pack(pady=5)
        entry_carnet = tk.Entry(ventana)
        entry_carnet.pack()

        lbl_nombre = tk.Label(ventana, text="", font=("Arial", 10, "bold"))
        
        tabla = ttk.Treeview(ventana, columns=("Doctor", "Fecha", "Hora"), show="headings")
        tabla.heading("Doctor", text="ID Doctor")
        tabla.heading("Fecha", text="Fecha")
        tabla.heading("Hora", text="Hora")

        def buscar():
            carnet = entry_carnet.get().strip()
            
            for item in tabla.get_children():
                tabla.delete(item)

            paciente_existe = False
            nombre_paciente = ""
            
            with open("pacientes.csv", "r") as f:
                for linea in f:
                    datos = linea.strip().split(",")
                    if len(datos) >= 3 and datos[0] == carnet:
                        paciente_existe = True
                        nombre_paciente = datos[1]
                        break

            if not paciente_existe:
                messagebox.showerror("Error", "El paciente no está registrado.")
                lbl_nombre.config(text="")
                return
            
            lbl_nombre.config(text=f"Historial de: {nombre_paciente}")
            
            tiene_citas = False
            with open("citas.csv", "r") as f:
                for linea in f:
                    datos = linea.strip().split(",")
                    if len(datos) >= 4 and datos[0] == carnet:
                        tabla.insert("", tk.END, values=(datos[1], datos[2], datos[3]))
                        tiene_citas = True
            
            if not tiene_citas:
                messagebox.showinfo("Info", "El paciente no tiene citas registradas.")

        tk.Button(ventana, text="Buscar", command=buscar).pack(pady=5)
        lbl_nombre.pack(pady=5)
        tabla.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
         
    # --- MODULO 6: REPORTES ---
    def abrir_reportes(self):
        ventana = tk.Toplevel(self)
        ventana.title("Reporte por Doctor")
        ventana.geometry("450x400")

        frame_inputs = tk.Frame(ventana)
        frame_inputs.pack(pady=10)

        tk.Label(frame_inputs, text="ID del Doctor:").grid(row=0, column=0, pady=5)
        entry_id = tk.Entry(frame_inputs)
        entry_id.grid(row=0, column=1, pady=5)

        tk.Label(frame_inputs, text="Fecha (DD-MM-AAAA):").grid(row=1, column=0, pady=5)
        entry_fecha = tk.Entry(frame_inputs)
        entry_fecha.grid(row=1, column=1, pady=5)

        lbl_info = tk.Label(ventana, text="", font=("Arial", 10, "bold"))

        tabla = ttk.Treeview(ventana, columns=("Carnet", "Hora"), show="headings")
        tabla.heading("Carnet", text="Carnet Paciente")
        tabla.heading("Hora", text="Hora")

        def buscar():
            id_doc = entry_id.get().strip()
            fecha = entry_fecha.get().strip()
            
            for item in tabla.get_children():
                tabla.delete(item)

            doctor_existe = False
            nombre_doctor = ""
            
            with open("doctores.csv", "r") as f:
                for linea in f:
                    datos = linea.strip().split(",")
                    if len(datos) >= 3 and datos[0] == id_doc:
                        doctor_existe = True
                        nombre_doctor = datos[1]
                        break

            if not doctor_existe:
                messagebox.showerror("Error", "El doctor no está registrado.")
                lbl_info.config(text="")
                return

            lbl_info.config(text=f"Agenda Dr. {nombre_doctor} para el {fecha}")

            tiene_citas = False
            with open("citas.csv", "r") as f:
                for linea in f:
                    datos = linea.strip().split(",")
                    if len(datos) >= 4 and datos[1] == id_doc and datos[2] == fecha:
                        tabla.insert("", tk.END, values=(datos[0], datos[3]))
                        tiene_citas = True

            if not tiene_citas:
                messagebox.showinfo("Info", "El doctor no tiene citas agendadas para este día.")

        tk.Button(frame_inputs, text="Buscar Agenda", command=buscar).grid(row=2, columnspan=2, pady=10)
        lbl_info.pack(pady=5)
        tabla.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    # --- NUEVO MODULO: VER LISTA DE DOCTORES ---
    def abrir_lista_doctores(self):
        ventana = tk.Toplevel(self)
        ventana.title("Lista de Doctores Registrados")
        ventana.geometry("500x350")

        tk.Label(ventana, text="Doctores Registrados", font=("Arial", 14, "bold")).pack(pady=10)

        # Crear la tabla para los doctores
        tabla = ttk.Treeview(ventana, columns=("ID", "Nombre", "Especialidad"), show="headings")
        tabla.heading("ID", text="ID Doctor")
        tabla.heading("Nombre", text="Nombre del Doctor")
        tabla.heading("Especialidad", text="Especialidad")
        
        # Ajustar el ancho de las columnas
        tabla.column("ID", width=80, anchor="center")
        tabla.column("Nombre", width=200, anchor="w")
        tabla.column("Especialidad", width=180, anchor="w")

        # Leer el archivo doctores.csv y agregarlos a la tabla
        with open("doctores.csv", "r") as f:
            for linea in f:
                datos = linea.strip().split(",")
                if len(datos) >= 3:
                    tabla.insert("", tk.END, values=(datos[0], datos[1], datos[2]))

        tabla.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

if __name__ == "__main__":
    app = SistemaCitas()
    app.mainloop()