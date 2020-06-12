import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from formularios import formularioCliente
from formularios import formularioProductos
from formularios import formularioPedidos

class Menu(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title='Menu')

        self.set_default_size(300, 200)
        self.set_border_width(10)
        self.grid_menu = Gtk.Grid()
        self.grid_menu.set_border_width(10)
        self.grid_menu.set_column_spacing(20)
        self.grid_menu.set_row_spacing(20)
        self.grid_menu.set_row_homogeneous(True)
        self.grid_menu.set_column_homogeneous(True)
        self.add(self.grid_menu)

        self.btn_clientes = Gtk.Button('CLIENTES')
        self.btn_productos = Gtk.Button('PRODUCTOS')
        self.btn_pedidos = Gtk.Button('PEDIDOS')
        self.btn_consultas = Gtk.Button('CONSULTAS')
        self.btn_sair = Gtk.Button('SAIR')

        self.btn_clientes.set_vexpand(True)
        self.btn_productos.set_vexpand(True)
        self.btn_pedidos.set_hexpand(True)
        self.btn_consultas.set_hexpand(True)
        self.btn_sair.set_hexpand(True)

        self.btn_clientes.connect('clicked', self.on_cliente_clicked)
        self.btn_productos.connect('clicked', self.on_producto_clicked)
        self.btn_pedidos.connect('clicked', self.on_pedido_clicked)

        self.grid_menu.add(self.btn_clientes)
        self.grid_menu.attach_next_to(self.btn_productos, self.btn_clientes, Gtk.PositionType.BOTTOM, 1, 1)
        self.grid_menu.attach_next_to(self.btn_pedidos, self.btn_productos, Gtk.PositionType.BOTTOM, 1, 1)
        self.grid_menu.attach_next_to(self.btn_consultas, self.btn_pedidos, Gtk.PositionType.BOTTOM, 1, 1)
        self.grid_menu.attach_next_to(self.btn_sair, self.btn_consultas, Gtk.PositionType.BOTTOM, 1, 1)

        self.connect('destroy', Gtk.main_quit)
        self.show_all()

    def on_cliente_clicked(self, button):
        formularioCliente.FormularioCliente()
        self.set_visible(False)

    def on_producto_clicked(self, button):
        formularioProductos.FormularioProducto()
        self.set_visible(False)

    def on_pedido_clicked(self, button):
        formularioPedidos.FormularioPedido()
        self.set_visible(False)


