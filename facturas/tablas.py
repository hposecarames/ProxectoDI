import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from baseDatos.metodosBD import BaseDatos


class Facturas(Gtk.Window):

    def __init__(self):

        Gtk.Window.__init__(self, title="Facturas")
        self.set_default_size(400, 400)
        self.set_border_width(10)
        self.caixa = Gtk.Box()
        self.caixa.set_orientation(Gtk.Orientation.VERTICAL)
        self.add(self.caixa)

        self.columna_cliente = ['Dni', 'Nome', 'Apelidos', 'Direccion', 'Telefono', 'Codigo Postal', 'Sexo']
        self.store = Gtk.ListStore(str, str, str, str, str, str, str)
        self.lista = []
        self.treeView = Gtk.TreeView(self.store)

        self.caixa.add(self.treeView)
        con = BaseDatos.conectar()
        datos = BaseDatos.obter_datos(con)

        for dato in datos:
            self.lista.append([dato[0], dato[1], dato[2], dato[3], dato[4], dato[5], dato[6]])

        for nome in self.lista:
            self.store.append(nome)

        for i in range(len(self.columna_cliente)):
            celda = Gtk.CellRendererText()
            self.columna = Gtk.TreeViewColumn(self.columna_cliente[i], celda, text=i)
            self.treeView.append_column(self.columna)



fact = Facturas()
fact.connect("destroy", Gtk.main_quit)
fact.show_all()
Gtk.main()