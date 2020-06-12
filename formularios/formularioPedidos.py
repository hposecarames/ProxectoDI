import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from baseDatos import metodosBD
from menu import menus


class FormularioPedido(Gtk.Window):

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
        self.et_codigo = Gtk.Label("Codigo: ", halign=Gtk.Align.START)
        self.et_cantidade = Gtk.Label("Cantidade: ", halign=Gtk.Align.START)


        self.entrada_dni = Gtk.Entry()
        self.entrada_codigo = Gtk.Entry()
        self.entrada_cantidade = Gtk.Entry()

        self.btn_insertar = Gtk.Button("INSERTAR")
        self.btn_volver = Gtk.Button("VOLVER")
        self.btn_insertar.connect("clicked", self.on_insertar_clicked)
        self.btn_volver.connect("clicked", self.on_volver_clicked)

        self.grid_insertar.add(self.et_dni)
        self.grid_insertar.attach_next_to(self.entrada_dni, self.et_dni, Gtk.PositionType.RIGHT, 1, 1)
        self.grid_insertar.attach_next_to(self.et_codigo, self.et_dni, Gtk.PositionType.BOTTOM, 1, 1)
        self.grid_insertar.attach_next_to(self.entrada_codigo, self.et_codigo, Gtk.PositionType.RIGHT, 1, 1)
        self.grid_insertar.attach_next_to(self.et_cantidade, self.et_codigo, Gtk.PositionType.BOTTOM, 1, 1)
        self.grid_insertar.attach_next_to(self.entrada_cantidade, self.et_cantidade, Gtk.PositionType.RIGHT, 1, 1)
        self.grid_insertar.attach_next_to(self.btn_insertar, self.entrada_cantidade, Gtk.PositionType.BOTTOM, 1, 1)
        self.grid_insertar.attach_next_to(self.btn_volver, self.btn_insertar, Gtk.PositionType.LEFT, 1, 1)

        self.grid_modificar = Gtk.Grid()
        self.grid_modificar.set_border_width(10)
        self.grid_modificar.set_row_spacing(20)
        self.grid_modificar.set_column_spacing(20)

        self.paginas.append_page(self.grid_modificar, Gtk.Label("Modificar"))

        self.et_id_m = Gtk.Label("ID: ", halign=Gtk.Align.START)
        self.et_dni_m = Gtk.Label("Dni: ", halign=Gtk.Align.START)
        self.et_codigo_m = Gtk.Label("Codigo: ", halign=Gtk.Align.START)
        self.et_cantidade_m = Gtk.Label("Cantidade: ", halign=Gtk.Align.START)


        self.entrada_dni_m = Gtk.Entry()
        self.entrada_codigo_m = Gtk.Entry()
        self.entrada_cantidade_m = Gtk.Entry()


        self.btn_modificar = Gtk.Button("MODIFICAR")
        self.btn_modificar.connect("clicked", self.on_modificar_clicked)

        self.grid_modificar.add(self.et_dni_m)
        self.grid_modificar.attach_next_to(self.entrada_dni_m, self.et_dni_m, Gtk.PositionType.RIGHT, 1, 1)
        self.grid_modificar.attach_next_to(self.et_codigo_m, self.et_dni_m, Gtk.PositionType.BOTTOM, 1, 1)
        self.grid_modificar.attach_next_to(self.entrada_codigo_m, self.et_codigo_m, Gtk.PositionType.RIGHT, 1, 1)
        self.grid_modificar.attach_next_to(self.et_cantidade_m, self.et_codigo_m, Gtk.PositionType.BOTTOM, 1, 1)
        self.grid_modificar.attach_next_to(self.entrada_cantidade_m, self.et_cantidade_m, Gtk.PositionType.RIGHT, 1, 1)
        self.grid_modificar.attach_next_to(self.btn_modificar, self.entrada_cantidade_m, Gtk.PositionType.BOTTOM, 1, 1)

        self.grid_eliminar = Gtk.Grid()
        self.grid_eliminar.set_border_width(10)
        self.grid_eliminar.set_row_spacing(20)
        self.grid_eliminar.set_column_spacing(20)

        self.paginas.append_page(self.grid_eliminar, Gtk.Label("Eliminar"))

        self.et_id_e = Gtk.Label("ID: ", halign=Gtk.Align.START)
        self.entrada_id_e = Gtk.Entry()
        self.btn_eliminar = Gtk.Button("ELIMINAR")
        self.btn_eliminar.connect("clicked", self.on_eliminar_clicked)
        self.grid_eliminar.add(self.et_id_e)
        self.grid_eliminar.attach_next_to(self.entrada_id_e, self.et_id_e, Gtk.PositionType.RIGHT, 1, 1)
        self.grid_eliminar.attach_next_to(self.btn_eliminar, self.entrada_id_e, Gtk.PositionType.BOTTOM, 1, 1)

        self.connect('destroy', Gtk.main_quit)
        self.show_all()



    def on_insertar_clicked(self, button):

        con = metodosBD.BaseDatos.conectar()
        dni = self.entrada_dni.get_text()
        codigo = self.entrada_codigo.get_text()
        cantidade = self.entrada_cantidade.get_text()

        metodosBD.BaseDatos.insertar_pedido(con, dni, codigo, cantidade)

        mensaxe = Gtk.MessageDialog(self, 0, Gtk.MessageType.INFO, Gtk.ButtonsType.OK, "Pedido insertado")
        mensaxe.run()
        mensaxe.destroy()

    def on_modificar_clicked(self, button):
        con = metodosBD.BaseDatos.conectar()
        dni = self.entrada_dni_m.get_text()
        codigo = self.entrada_nome_m.get_text()
        cantidade = self.entrada_cantidade_m.get_text()


        metodosBD.BaseDatos.modificar_pedido(con, id, dni, codigo, cantidade)

    def on_eliminar_clicked(self, button):
        con = metodosBD.BaseDatos.conectar()
        dni = self.entrada_dni_e.get_text()

        metodosBD.BaseDatos.eliminar_p(con, dni)

    def on_volver_clicked(self, button):
        menus.Menu()
        self.set_visible(False)
