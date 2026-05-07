# ==========================================================
# SOFTWARE FJ
# INTERFAZ - CUSTOMTKINTER
# ==========================================================

from abc import ABC, abstractmethod
from datetime import datetime
import customtkinter as ctk
from tkinter import ttk, messagebox

# ==========================================================
# CONFIGURACIÓN VISUAL
# ==========================================================

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# ==========================================================
# LOGS
# ==========================================================

def registrar_log(mensaje):

    with open("logs.txt", "a", encoding="utf-8") as archivo:
        archivo.write(f"{datetime.now()} - {mensaje}\n")


# ==========================================================
# EXCEPCIONES
# ==========================================================

class ClienteError(Exception):
    pass


class ServicioError(Exception):
    pass


class ReservaError(Exception):
    pass


# ==========================================================
# CLASE ABSTRACTA
# ==========================================================

class Entidad(ABC):

    @abstractmethod
    def mostrar_info(self):
        pass


# ==========================================================
# CLIENTE
# ==========================================================

class Cliente(Entidad):

    def __init__(self, nombre, correo, telefono):

        if not nombre.strip():
            raise ClienteError("Nombre inválido")

        if "@" not in correo:
            raise ClienteError("Correo inválido")

        if not telefono.isdigit():
            raise ClienteError("Teléfono inválido")

        self.__nombre = nombre
        self.__correo = correo
        self.__telefono = telefono

    def get_nombre(self):
        return self.__nombre

    def mostrar_info(self):

        return (
            f"{self.__nombre} - "
            f"{self.__correo}"
        )


# ==========================================================
# SERVICIO ABSTRACTO
# ==========================================================

class Servicio(ABC):

    def __init__(self, nombre_servicio):

        self.nombre_servicio = nombre_servicio

    @abstractmethod
    def calcular_costo(self, duracion):
        pass


# ==========================================================
# SERVICIOS
# ==========================================================

class ReservaSala(Servicio):

    def calcular_costo(self, horas):

        if horas <= 0:
            raise ServicioError("Horas inválidas")

        return horas * 50000


class AlquilerEquipo(Servicio):

    def calcular_costo(self, dias):

        if dias <= 0:
            raise ServicioError("Días inválidos")

        return dias * 80000


class AsesoriaEspecializada(Servicio):

    def calcular_costo(self, horas):

        if horas <= 0:
            raise ServicioError("Horas inválidas")

        return horas * 120000


# ==========================================================
# RESERVA
# ==========================================================

class Reserva:

    contador = 1

    def __init__(self, cliente, servicio, duracion):

        if duracion <= 0:
            raise ReservaError("Duración inválida")

        self.id_reserva = Reserva.contador
        Reserva.contador += 1

        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.estado = "Confirmada"

    def costo(self):

        return self.servicio.calcular_costo(
            self.duracion
        )


# ==========================================================
# SISTEMA
# ==========================================================

class SistemaGestion:

    def __init__(self):

        self.clientes = []
        self.reservas = []

        self.servicios = [
            ReservaSala("Sala Empresarial"),
            AlquilerEquipo("Equipos"),
            AsesoriaEspecializada("Asesoría")
        ]

    def agregar_cliente(self, cliente):

        self.clientes.append(cliente)

    def agregar_reserva(self, reserva):

        self.reservas.append(reserva)


# ==========================================================
# APP PROFESIONAL
# ==========================================================

class App(ctk.CTk):

    def __init__(self):

        super().__init__()

        self.sistema = SistemaGestion()

        # ==================================================
        # CONFIG VENTANA
        # ==================================================

        self.title("SOFTWARE FJ")

        self.geometry("1400x800")

        self.minsize(1200, 700)

        # ==================================================
        # GRID
        # ==================================================

        self.grid_columnconfigure(1, weight=1)

        self.grid_rowconfigure(0, weight=1)

        # ==================================================
        # SIDEBAR
        # ==================================================

        self.sidebar = ctk.CTkFrame(
            self,
            width=250,
            corner_radius=0
        )

        self.sidebar.grid(
            row=0,
            column=0,
            sticky="ns"
        )

        # ==================================================
        # LOGO
        # ==================================================

        self.logo = ctk.CTkLabel(
            self.sidebar,
            text="SOFTWARE FJ",
            font=("Arial", 28, "bold")
        )

        self.logo.pack(
            pady=40
        )

        # ==================================================
        # BOTONES SIDEBAR
        # ==================================================

        self.btn_dashboard = ctk.CTkButton(
             self.sidebar,
             text="Dashboard",
             height=45,
             corner_radius=12,
             command=self.mostrar_dashboard
        )
        
        self.btn_dashboard.pack(
             pady=10,
             padx=20,
             fill="x"
        )

        self.btn_clientes = ctk.CTkButton(
            self.sidebar,
            text="Clientes",
            height=45,
            corner_radius=12,
            command=self.mostrar_clientes
        )

        self.btn_clientes.pack(
            pady=10,
            padx=20,
            fill="x"
        )

        self.btn_reservas = ctk.CTkButton(
            self.sidebar,
            text="Reservas",
            height=45,
            corner_radius=12,
            command=self.mostrar_reservas
        )

        self.btn_reservas.pack(
            pady=10,
            padx=20,
            fill="x"
        )

        # ==================================================
        # MAIN
        # ==================================================

        self.main = ctk.CTkFrame(
            self,
            corner_radius=0
        )

        self.main.grid(
            row=0,
            column=1,
            sticky="nsew"
        )

        # ==================================================
        # TÍTULO
        # ==================================================

        self.titulo = ctk.CTkLabel(
            self.main,
            text="Sistema Integral de Gestión",
            font=("Arial", 35, "bold")
        )

        self.titulo.pack(
            pady=30
        )

        # ==================================================
        # CARDS
        # ==================================================

        self.cards_frame = ctk.CTkFrame(
            self.main,
            fg_color="transparent"
        )

        self.cards_frame.pack(
            pady=20
        )

        self.card1 = ctk.CTkFrame(
            self.cards_frame,
            width=250,
            height=130,
            corner_radius=20
        )

        self.card1.grid(
            row=0,
            column=0,
            padx=20
        )

        self.card2 = ctk.CTkFrame(
            self.cards_frame,
            width=250,
            height=130,
            corner_radius=20
        )

        self.card2.grid(
            row=0,
            column=1,
            padx=20
        )

        self.card3 = ctk.CTkFrame(
            self.cards_frame,
            width=250,
            height=130,
            corner_radius=20
        )

        self.card3.grid(
            row=0,
            column=2,
            padx=20
        )

        # ==================================================
        # TEXTO CARDS
        # ==================================================

        self.lbl_clientes = ctk.CTkLabel(
            self.card1,
            text="Clientes\n0",
            font=("Arial", 24, "bold")
        )

        self.lbl_clientes.place(
            relx=0.5,
            rely=0.5,
            anchor="center"
        )

        self.lbl_reservas = ctk.CTkLabel(
            self.card2,
            text="Reservas\n0",
            font=("Arial", 24, "bold")
        )

        self.lbl_reservas.place(
            relx=0.5,
            rely=0.5,
            anchor="center"
        )

        self.lbl_servicios = ctk.CTkLabel(
            self.card3,
            text="Servicios\n3",
            font=("Arial", 24, "bold")
        )

        self.lbl_servicios.place(
            relx=0.5,
            rely=0.5,
            anchor="center"
        )

        # ==================================================
        # FORMULARIO
        # ==================================================

        self.form = ctk.CTkFrame(
            self.main,
            corner_radius=20
        )

        self.form.pack(
            pady=30,
            padx=30,
            fill="x"
        )

        self.form_title = ctk.CTkLabel(
            self.form,
            text="Registrar Cliente",
            font=("Arial", 24, "bold")
        )

        self.form_title.pack(
            pady=20
        )

        self.entry_nombre = ctk.CTkEntry(
            self.form,
            placeholder_text="Nombre"
        )

        self.entry_nombre.pack(
            pady=10,
            padx=20,
            fill="x"
        )

        self.entry_correo = ctk.CTkEntry(
            self.form,
            placeholder_text="Correo"
        )

        self.entry_correo.pack(
            pady=10,
            padx=20,
            fill="x"
        )

        self.entry_telefono = ctk.CTkEntry(
            self.form,
            placeholder_text="Teléfono"
        )

        self.entry_telefono.pack(
            pady=10,
            padx=20,
            fill="x"
        )

        self.btn_registrar = ctk.CTkButton(
            self.form,
            text="Registrar Cliente",
            height=45,
            corner_radius=15,
            command=self.registrar_cliente
        )

        self.btn_registrar.pack(
            pady=20,
            padx=20,
            fill="x"
        )

        # ==================================================
        # TABLA
        # ==================================================

        self.tabla_frame = ctk.CTkFrame(
            self.main,
            corner_radius=20
        )

        self.tabla_frame.pack(
            padx=30,
            pady=20,
            fill="both",
            expand=True
        )

        self.tabla_titulo = ctk.CTkLabel(
            self.tabla_frame,
            text="Clientes Registrados",
            font=("Arial", 22, "bold")
        )

        self.tabla_titulo.pack(
            pady=20
        )

        self.tabla = ttk.Treeview(
            self.tabla_frame,
            columns=(
                "Nombre",
                "Correo",
                "Telefono"
            ),
            show="headings",
            height=10
        )

        self.tabla.heading(
            "Nombre",
            text="Nombre"
        )

        self.tabla.heading(
            "Correo",
            text="Correo"
        )

        self.tabla.heading(
            "Telefono",
            text="Teléfono"
        )

        self.tabla.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=20
        )

    # ======================================================
    # REGISTRAR CLIENTE
    # ======================================================

    def registrar_cliente(self):

        try:

            nombre = self.entry_nombre.get()

            correo = self.entry_correo.get()

            telefono = self.entry_telefono.get()

            cliente = Cliente(
                nombre,
                correo,
                telefono
            )

            self.sistema.agregar_cliente(
                cliente
            )

            self.tabla.insert(
                "",
                "end",
                values=(
                    nombre,
                    correo,
                    telefono
                )
            )

            self.actualizar_cards()

            messagebox.showinfo(
                "Éxito",
                "Cliente registrado"
            )

            self.entry_nombre.delete(0, "end")
            self.entry_correo.delete(0, "end")
            self.entry_telefono.delete(0, "end")

        except Exception as e:

            messagebox.showerror(
                "Error",
                str(e)
            )

    # ======================================================
    # ACTUALIZAR CARDS
    # ======================================================

    def actualizar_cards(self):

        self.lbl_clientes.configure(
            text=f"Clientes\n{len(self.sistema.clientes)}"
        )

 # ======================================================
 # MOSTRAR DASHBOARD
 # ======================================================
   
    def mostrar_dashboard(self):

        self.titulo.configure(
            text="Sistema Integral de Gestión"
        )
        
        self.form.pack(
            pady=30,
            padx=30,
            fill="x"
        )

        self.tabla_frame.pack(
            padx=30,
            pady=20,
            fill="both",
            expand=True
        )

# ======================================================
# MOSTRAR CLIENTES
# ======================================================
    def mostrar_clientes(self):

        self.titulo.configure(
            text="Gestión de Clientes"
        )

        self.form.pack(
            pady=30,
            padx=30,
            fill="x"
        )

        self.tabla_frame.pack(
            padx=30,
            pady=20,
            fill="both",
            expand=True
        )

    # ======================================================
    # MOSTRAR RESERVAS
    # ======================================================

    def mostrar_reservas(self):

        self.titulo.configure(
            text="Panel de Reservas"
        )

        self.form.pack_forget()

        self.tabla_frame.pack_forget()

        self.tabla_frame.pack(
            padx=30,
            pady=20,
            fill="both",
            expand=True
        )

# ==========================================================
# EJECUCIÓN
# ==========================================================

if __name__ == "__main__":

    app = App()

    app.mainloop()