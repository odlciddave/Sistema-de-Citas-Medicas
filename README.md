# 🏥 Sistema de Citas Médicas

Un sistema de gestión de agendas clínicas desarrollado en Python. Este proyecto utiliza persistencia de datos mediante archivos planos (CSV) e incluye una interfaz gráfica de usuario (GUI) amigable para automatizar el control de pacientes y médicos.

## 🚀 Características Principales

- **Registro de Entidades:** Creación de perfiles para doctores y pacientes.
- **Gestión de Disponibilidad:** Registro de horarios laborales para cada médico.
- **Agendamiento con Validaciones:** Sistema anti-traslapes que verifica la disponibilidad exacta de fecha y hora antes de confirmar una cita para evitar cruces.
- **Historial Transaccional:** Registro acumulado de consultas por paciente.
- **Reportes de Agenda:** Filtro de citas por doctor y día específico.
- **Doble Interfaz:** Incluye la lógica pura en versión de consola y una versión visual interactiva con ventanas emergentes y tablas de datos.

## 🛠️ Tecnologías Utilizadas

- **Lenguaje:** Python 3
- **Interfaz Gráfica:** Tkinter (Módulos `ttk.Treeview`, `messagebox`)
- **Persistencia de Datos:** Archivos Planos (CSV) gestionados nativamente.

## 📂 Estructura del Proyecto

- `citas_gui.py` - Archivo principal para ejecutar la Interfaz Gráfica (GUI).
- `citas_medicas.py` - Archivo secundario para ejecutar la versión de terminal/consola.
- `doctores.csv`, `pacientes.csv`, `horarios.csv`, `citas.csv` - Archivos de almacenamiento que operan como base de datos (se generan automáticamente al iniciar el programa si no existen).

## ⚙️ Cómo Ejecutar el Proyecto

1. Clona este repositorio en tu máquina local:
   ```bash
   git clone [https://github.com/odlciddave/Sistema-de-Citas-Medicas.git](https://github.com/odlciddave/Sistema-de-Citas-Medicas.git)
