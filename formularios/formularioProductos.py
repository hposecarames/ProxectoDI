import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from baseDatos import metodosBD
from menu import menus


class FormularioProducto(Gtk.Window):

    def __init__(self):

        Gtk.Window.__init__(self, title="FormularioProducto")
        self.set_default_size(300, 380)
        self.set_border_width(10)

        self.paginas = Gtk.Notebook()
        self.add(self.paginas)

        self.grid_insertar = Gtk.Grid()
        self.grid_insertar.set_border_width(10)
        self.grid_insertar.set_column_spacing(20)
        self.grid_insertar.set_row_spacing(20)

        self.paginas.append_page(self.grid_insertar, Gtk.Label("Insertar"))

        self.et_codigo = Gtk.Label("Codigo: ", halign=Gtk.Align.START)
        self.et_nome = Gtk.Label("Nome: ", halign=Gtk.Align.START)
        self.et_prezo = Gtk.Label("Prezo ", halign=Gtk.Align.START)

        self.entrada_codigo = Gtk.Entry()
        self.entrada_nome = Gtk.Entry()
        self.entrada_prezo = Gtk.Entry()


        self.btn_insertar = Gtk.Button("INSERTAR")
        self.btn_volver = Gtk.Button("VOLVER")
        self.btn_insertar.connect("clicked", self.on_insertar_clicked)
        self.btn_volver.connect("clicked", self.on_volver_clicked)

        self.grid_insertar.add(self.et_codigo)
        self.grid_insertar.attach_next_to(self.entrada_codigo, self.et_codigo, Gtk.PositionType.RIGHT, 1, 1)
        self.grid_insertar.attach_next_to(self.et_nome, self.et_codigo, Gtk.PositionType.BOTTOM, 1, 1)
        self.grid_insertar.attach_next_to(self.entrada_nome, self.et_nome, Gtk.PositionType.RIGHT, 1, 1)
        self.grid_insertar.attach_next_to(self.et_prezo, self.et_nome, Gtk.PositionType.BOTTOM, 1, 1)
        self.grid_insertar.attach_next_to(self.entrada_prezo, self.et_prezo, Gtk.PositionType.RIGHT, 1, 1)
        self.grid_insertar.attach_next_to(self.btn_insertar, self.entrada_prezo, Gtk.PositionType.BOTTOM, 1, 1)
        self.grid_insertar.attach_next_to(self.btn_volver, self.btn_insertar, Gtk.PositionType.LEFT, 1, 1)

        self.grid_modificar = Gtk.Grid()
        self.grid_modificar.set_border_width(10)
        self.grid_modificar.set_row_spacing(20)
        self.grid_modificar.set_column_spacing(20)

        self.paginas.append_page(self.grid_modificar, Gtk.Label("Modificar"))

        self.et_codigo_m = Gtk.Label("Codigo: ", halign=Gtk.Align.START)
        self.et_nome_m = Gtk.Label("Nome: ", halign=Gtk.Align.START)
        self.et_prezo_m = Gtk.Label("Prezo: ", halign=Gtk.Align.START)


        self.entrada_codigo_m = Gtk.Entry()
        self.entrada_nome_m = Gtk.Entry()
        self.entrada_prezo_m = Gtk.Entry()

        self.btn_modificar = Gtk.Button("MODIFICAR")
        self.btn_modificar.connect("clicked", self.on_modificar_clicked)

        self.grid_modificar.add(self.et_codigo_m)
        self.grid_modificar.attach_next_to(self.entrada_codigo_m, self.et_codigo_m, Gtk.PositionType.RIGHT, 1, 1)
        self.grid_modificar.attach_next_to(self.et_nome_m, self.et_codigo_m, Gtk.PositionType.BOTTOM, 1, 1)
        self.grid_modificar.attach_next_to(self.entrada_nome_m, self.et_nome_m, Gtk.PositionType.RIGHT, 1, 1)
        self.grid_modificar.attach_next_to(self.et_prezo_m, self.et_nome_m, Gtk.PositionType.BOTTOM, 1, 1)
        self.grid_modificar.attach_next_to(self.entrada_prezo_m, self.et_prezo_m, Gtk.PositionType.RIGHT, 1, 1)
        self.grid_modificar.attach_next_to(self.btn_modificar, self.entrada_prezo_m, Gtk.PositionType.BOTTOM, 1, 1)

        self.grid_eliminar = Gtk.Grid()
        self.grid_eliminar.set_border_width(10)
        self.grid_eliminar.set_row_spacing(20)
        self.grid_eliminar.set_column_spacing(20)

        self.paginas.append_page(self.grid_eliminar, Gtk.Label("Eliminar"))

        self.et_codigo_e = Gtk.Label("Codigo: ", halign=Gtk.Align.START)
        self.entrada_codigo_e = Gtk.Entry()
        self.btn_eliminar = Gtk.Button("ELIMINAR")
        self.btn_eliminar.connect("clicked", self.on_eliminar_clicked)
        self.grid_eliminar.add(self.et_codigo_e)
        self.grid_eliminar.attach_next_to(self.entrada_codigo_e, self.et_codigo_e, Gtk.PositionType.RIGHT, 1, 1)
        self.grid_eliminar.attach_next_to(self.btn_eliminar, self.entrada_codigo_e, Gtk.PositionType.BOTTOM, 1, 1)

        self.connect('destroy', Gtk.main_quit)
        self.show_all()


    def on_insertar_clicked(self, button):

        codigo = self.entrada_codigo.get_text()
        nome = self.entrada_nome.get_text()
        prezo = self.entrada_prezo.get_text()


        if metodosBD.BaseDatos.insertar_producto(self, codigo, nome, prezo) == True:

            mensaxe = Gtk.MessageDialog(self, 0, Gtk.MessageType.INFO, Gtk.ButtonsType.OK, "Producto insertado")
            mensaxe.run()
            mensaxe.destroy()
            self.entrada_codigo.set_text("")
            self.entrada_nome.set_text("")
            self.entrada_prezo.set_text("")
        else:

            mensaxe = Gtk.MessageDialog(self, 0, Gtk.MessageType.INFO, Gtk.ButtonsType.OK,
                                        "Faltan datos ou algún é erróneo")
            mensaxe.run()
            mensaxe.destroy()



    def on_modificar_clicked(self, button):

        codigo = self.entrada_codigo_m.get_text()
        nome = self.entrada_nome_m.get_text()
        prezo = self.entrada_prezo_m.get_text()

        if metodosBD.BaseDatos.modificar_producto(self, codigo, nome, prezo) == True:

            mensaxe = Gtk.MessageDialog(self, 0, Gtk.MessageType.INFO, Gtk.ButtonsType.OK, "Producto modificado")
            mensaxe.run()
            mensaxe.destroy()
            self.entrada_codigo_m.set_text("")
            self.entrada_nome_m.set_text("")
            self.entrada_prezo_m.set_text("")
        else:

            mensaxe = Gtk.MessageDialog(self, 0, Gtk.MessageType.INFO, Gtk.ButtonsType.OK,
                                        "Faltan datos ou algún é erróneo")
            mensaxe.run()
            mensaxe.destroy()

    def on_eliminar_clicked(self, button):

        codigo = self.entrada_codigo_e.get_text()

        if metodosBD.BaseDatos.eliminar_producto(self, codigo) == True:

            mensaxe = Gtk.MessageDialog(self, 0, Gtk.MessageType.INFO, Gtk.ButtonsType.OK, "Producto eliminado")
            mensaxe.run()
            mensaxe.destroy()
            self.entrada_codigo_e.set_text("")
        else:

            mensaxe = Gtk.MessageDialog(self, 0, Gtk.MessageType.INFO, Gtk.ButtonsType.OK,
                                        "Faltan datos ou algún é erróneo")
            mensaxe.run()
            mensaxe.destroy()

    def on_volver_clicked(self, button):
        menus.Menu()
        self.set_visible(False)
