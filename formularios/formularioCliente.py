import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from baseDatos import metodosBD
from menu import menus


class FormularioCliente(Gtk.Window):

    def __init__(self):

        Gtk.Window.__init__(self, title="FormularioCliente")
        self.set_default_size(300, 380)
        self.set_border_width(10)

        self.paginas = Gtk.Notebook()
        self.add(self.paginas)

        self.grid_insertar = Gtk.Grid()
        self.grid_insertar.set_border_width(10)
        self.grid_insertar.set_column_spacing(20)
        self.grid_insertar.set_row_spacing(20)

        self.paginas.append_page(self.grid_insertar, Gtk.Label("Insertar"))

        self.et_dni = Gtk.Label("Dni: ", halign=Gtk.Align.START)
        self.et_nome = Gtk.Label("Nome: ", halign=Gtk.Align.START)
        self.et_apelidos = Gtk.Label("Apelidos: ", halign=Gtk.Align.START)
        self.et_direccion = Gtk.Label("Direccion: ", halign=Gtk.Align.START)
        self.et_telefono = Gtk.Label("Telefono: ", halign=Gtk.Align.START)
        self.et_cp = Gtk.Label("Codigo Postal: ", halign=Gtk.Align.START)
        self.et_sexo = Gtk.Label("Sexo: ", halign=Gtk.Align.START)

        self.entrada_dni = Gtk.Entry()
        self.entrada_nome = Gtk.Entry()
        self.entrada_apelidos = Gtk.Entry()
        self.entrada_direccion = Gtk.Entry()
        self.entrada_telefono = Gtk.Entry()
        self.entrada_cp = Gtk.Entry()

        self.btn_sexo = Gtk.RadioButton.new_with_label_from_widget(None, "Home")
        self.btn_sexo.connect("toggled", self.on_button_toggled, "1")
        self.btn_sexo2 = Gtk.RadioButton.new_from_widget(self.btn_sexo)
        self.btn_sexo2.set_label("Muller")
        self.btn_sexo2.connect("toggled", self.on_button_toggled, "2")
        self.caixa_sexo = Gtk.Box()
        self.caixa_sexo.add(self.btn_sexo)
        self.caixa_sexo.add(self.btn_sexo2)
        self.btn_insertar = Gtk.Button("INSERTAR")
        self.btn_volver = Gtk.Button("VOLVER")
        self.btn_insertar.connect("clicked", self.on_insertar_clicked)
        self.btn_volver.connect("clicked", self.on_volver_clicked)

        self.grid_insertar.add(self.et_dni)
        self.grid_insertar.attach_next_to(self.entrada_dni, self.et_dni, Gtk.PositionType.RIGHT, 1, 1)
        self.grid_insertar.attach_next_to(self.et_nome, self.et_dni, Gtk.PositionType.BOTTOM, 1, 1)
        self.grid_insertar.attach_next_to(self.entrada_nome, self.et_nome, Gtk.PositionType.RIGHT, 1, 1)
        self.grid_insertar.attach_next_to(self.et_apelidos, self.et_nome, Gtk.PositionType.BOTTOM, 1, 1)
        self.grid_insertar.attach_next_to(self.entrada_apelidos, self.et_apelidos, Gtk.PositionType.RIGHT, 1, 1)
        self.grid_insertar.attach_next_to(self.et_direccion, self.et_apelidos, Gtk.PositionType.BOTTOM, 1, 1)
        self.grid_insertar.attach_next_to(self.entrada_direccion, self.et_direccion, Gtk.PositionType.RIGHT, 1, 1)
        self.grid_insertar.attach_next_to(self.et_telefono, self.et_direccion, Gtk.PositionType.BOTTOM, 1, 1)
        self.grid_insertar.attach_next_to(self.entrada_telefono, self.et_telefono, Gtk.PositionType.RIGHT, 1, 1)
        self.grid_insertar.attach_next_to(self.et_cp, self.et_telefono, Gtk.PositionType.BOTTOM, 1, 1)
        self.grid_insertar.attach_next_to(self.entrada_cp, self.et_cp, Gtk.PositionType.RIGHT, 1, 1)
        self.grid_insertar.attach_next_to(self.et_sexo, self.et_cp, Gtk.PositionType.BOTTOM, 1, 1)
        self.grid_insertar.attach_next_to(self.caixa_sexo, self.entrada_cp, Gtk.PositionType.BOTTOM, 1, 1)
        self.grid_insertar.attach_next_to(self.btn_insertar, self.caixa_sexo, Gtk.PositionType.BOTTOM, 1, 1)
        self.grid_insertar.attach_next_to(self.btn_volver, self.btn_insertar, Gtk.PositionType.LEFT, 1, 1)

        self.grid_modificar = Gtk.Grid()
        self.grid_modificar.set_border_width(10)
        self.grid_modificar.set_row_spacing(20)
        self.grid_modificar.set_column_spacing(20)

        self.paginas.append_page(self.grid_modificar, Gtk.Label("Modificar"))

        self.et_dni_m = Gtk.Label("Dni: ", halign=Gtk.Align.START)
        self.et_nome_m = Gtk.Label("Nome: ", halign=Gtk.Align.START)
        self.et_apelidos_m = Gtk.Label("Apelidos: ", halign=Gtk.Align.START)
        self.et_direccion_m = Gtk.Label("Direccion: ", halign=Gtk.Align.START)
        self.et_telefono_m = Gtk.Label("Telefono: ", halign=Gtk.Align.START)
        self.et_cp_m = Gtk.Label("Codigo Postal: ", halign=Gtk.Align.START)
        self.et_sexo_m = Gtk.Label("Sexo: ", halign=Gtk.Align.START)

        self.entrada_dni_m = Gtk.Entry()
        self.entrada_nome_m = Gtk.Entry()
        self.entrada_apelidos_m = Gtk.Entry()
        self.entrada_direccion_m = Gtk.Entry()
        self.entrada_telefono_m = Gtk.Entry()
        self.entrada_cp_m = Gtk.Entry()

        self.btn_sexo_m = Gtk.RadioButton.new_with_label_from_widget(None, "Home")
        self.btn_sexo_m.connect("toggled", self.on_button_toggled, "1")
        self.btn_sexo2_m = Gtk.RadioButton.new_from_widget(self.btn_sexo_m)
        self.btn_sexo2_m.set_label("Muller")
        self.btn_sexo2_m.connect("toggled", self.on_button_toggled, "2")
        self.caixa_sexo_m = Gtk.Box()
        self.caixa_sexo_m.add(self.btn_sexo_m)
        self.caixa_sexo_m.add(self.btn_sexo2_m)
        self.btn_modificar = Gtk.Button("MODIFICAR")
        self.btn_modificar.connect("clicked", self.on_modificar_clicked)

        self.grid_modificar.add(self.et_dni_m)
        self.grid_modificar.attach_next_to(self.entrada_dni_m, self.et_dni_m, Gtk.PositionType.RIGHT, 1, 1)
        self.grid_modificar.attach_next_to(self.et_nome_m, self.et_dni_m, Gtk.PositionType.BOTTOM, 1, 1)
        self.grid_modificar.attach_next_to(self.entrada_nome_m, self.et_nome_m, Gtk.PositionType.RIGHT, 1, 1)
        self.grid_modificar.attach_next_to(self.et_apelidos_m, self.et_nome_m, Gtk.PositionType.BOTTOM, 1, 1)
        self.grid_modificar.attach_next_to(self.entrada_apelidos_m, self.et_apelidos_m, Gtk.PositionType.RIGHT, 1, 1)
        self.grid_modificar.attach_next_to(self.et_direccion_m, self.et_apelidos_m, Gtk.PositionType.BOTTOM, 1, 1)
        self.grid_modificar.attach_next_to(self.entrada_direccion_m, self.et_direccion_m, Gtk.PositionType.RIGHT, 1, 1)
        self.grid_modificar.attach_next_to(self.et_telefono_m, self.et_direccion_m, Gtk.PositionType.BOTTOM, 1, 1)
        self.grid_modificar.attach_next_to(self.entrada_telefono_m, self.et_telefono_m, Gtk.PositionType.RIGHT, 1, 1)
        self.grid_modificar.attach_next_to(self.et_cp_m, self.et_telefono_m, Gtk.PositionType.BOTTOM, 1, 1)
        self.grid_modificar.attach_next_to(self.entrada_cp_m, self.et_cp_m, Gtk.PositionType.RIGHT, 1, 1)
        self.grid_modificar.attach_next_to(self.et_sexo_m, self.et_cp_m, Gtk.PositionType.BOTTOM, 1, 1)
        self.grid_modificar.attach_next_to(self.caixa_sexo_m, self.entrada_cp_m, Gtk.PositionType.BOTTOM, 1, 1)
        self.grid_modificar.attach_next_to(self.btn_modificar, self.caixa_sexo_m, Gtk.PositionType.BOTTOM, 1, 1)

        self.grid_eliminar = Gtk.Grid()
        self.grid_eliminar.set_border_width(10)
        self.grid_eliminar.set_row_spacing(20)
        self.grid_eliminar.set_column_spacing(20)

        self.paginas.append_page(self.grid_eliminar, Gtk.Label("Eliminar"))

        self.et_dni_e = Gtk.Label("Dni: ", halign=Gtk.Align.START)
        self.entrada_dni_e = Gtk.Entry()
        self.btn_eliminar = Gtk.Button("ELIMINAR")
        self.btn_eliminar.connect("clicked", self.on_eliminar_clicked)
        self.grid_eliminar.add(self.et_dni_e)
        self.grid_eliminar.attach_next_to(self.entrada_dni_e, self.et_dni_e, Gtk.PositionType.RIGHT, 1, 1)
        self.grid_eliminar.attach_next_to(self.btn_eliminar, self.entrada_dni_e, Gtk.PositionType.BOTTOM, 1, 1)

        self.connect('destroy', Gtk.main_quit)
        self.show_all()

    def on_button_toggled(self, button, label):
        if button.get_active():
            state = "on"
        else:
            state = "off"

    def on_insertar_clicked(self, button):
        con = metodosBD.BaseDatos.conectar()
        dni = self.entrada_dni.get_text()
        nome = self.entrada_nome.get_text()
        apelidos = self.entrada_apelidos.get_text()
        direccion = self.entrada_direccion.get_text()
        telefono = self.entrada_telefono.get_text()
        cp = self.entrada_cp.get_text()
        if self.btn_sexo.get_active():
            sexo = self.btn_sexo.get_label()
        else:
            sexo = self.btn_sexo2.get_label()

        metodosBD.BaseDatos.insertar_cliente(con, dni, nome, apelidos, direccion, telefono, cp, sexo)

        mensaxe = Gtk.MessageDialog(self, 0, Gtk.MessageType.INFO, Gtk.ButtonsType.OK, "Cliente insertado")
        mensaxe.run()
        mensaxe.destroy()

    def on_modificar_clicked(self, button):
        con = metodosBD.BaseDatos.conectar()
        dni = self.entrada_dni_m.get_text()
        nome = self.entrada_nome_m.get_text()
        apelidos = self.entrada_apelidos_m.get_text()
        direccion = self.entrada_direccion_m.get_text()
        telefono = self.entrada_telefono_m.get_text()
        cp = self.entrada_cp_m.get_text()
        if self.btn_sexo_m.get_active():
            sexo = self.btn_sexo_m.get_label()
        else:
            sexo = self.btn_sexo2_m.get_label()

        metodosBD.BaseDatos.modificar_cliente(con, nome, apelidos, direccion, telefono, cp, sexo, dni)

    def on_eliminar_clicked(self, button):
        con = metodosBD.BaseDatos.conectar()
        dni = self.entrada_dni_e.get_text()

        metodosBD.BaseDatos.eliminar_cliente(con, dni)

    def on_volver_clicked(self, button):
        menus.Menu()
        self.set_visible(False)
