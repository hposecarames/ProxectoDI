import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from baseDatos.metodosBD import BaseDatos
from menu import menus
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import os


class Facturas(Gtk.Window):

    def __init__(self):
        """
        Método constructor, aquí definimos tódolos elementos que constituen a ventá de FormularioPedido
        """

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

        self.btn_imprimir = Gtk.Button("Imprimir")
        self.btn_volver = Gtk.Button("VOLVER")
        self.btn_imprimir.connect('clicked', self.on_imprimir_clicked)
        self.btn_volver.connect("clicked", self.on_volver_clicked)


        self.opcions = ["Ficha Cliente", "Pedidos Cliente"]
        self.combo = Gtk.ComboBoxText()
        for i in self.opcions:
            self.combo.append_text(i)
        self.grid = Gtk.Grid()
        self.grid.set_border_width(10)
        self.grid.set_column_spacing(20)
        self.grid.set_row_spacing(20)
        self.grid.add(self.combo)
        self.grid.attach_next_to(self.btn_imprimir, self.combo, Gtk.PositionType.RIGHT, 1, 1)
        self.grid.attach_next_to(self.btn_volver, self.btn_imprimir, Gtk.PositionType.RIGHT, 10, 1)
        self.caixa.pack_end(self.grid, False, False, 0)

        con = BaseDatos.conectar()
        datos = BaseDatos.obter_datos(con)

        self.connect("destroy", Gtk.main_quit)
        self.show_all()

        for dato in datos:
            self.lista.append([dato[0], dato[1], dato[2], dato[3], dato[4], dato[5], dato[6]])

        for nome in self.lista:
            self.store.append(nome)

        for i in range(len(self.columna_cliente)):
            celda = Gtk.CellRendererText()
            self.columna = Gtk.TreeViewColumn(self.columna_cliente[i], celda, text=i)
            self.treeView.append_column(self.columna)
            self.columna.set_sort_column_id(i)

        self.fila_seleccionada = self.treeView.get_selection()
        self.fila_seleccionada.connect("changed", self.seleccion)

    def seleccion(self, selection):
        """
        Método que recolle a fila seleccionada do Treeview
        :param selection: fila seleccionada
        :return: Nada
        """
        self.modelo, self.fila = selection.get_selected()

    def on_imprimir_clicked(self, button):
        """
        Método que crea un pdf ca ficha ou os pedidos do cliente que recollemos ca fila seleccionada
        :param button: boton
        :return: Nada
        """

        if self.combo.get_active_text()=="Ficha Cliente" and self.modelo[self.fila][0] is not None:
            filename = self.modelo[self.fila][0] + ".pdf"
            w, h = A4
            pdf = canvas.Canvas(filename, pagesize=A4)
            path = os.path.dirname(os.path.abspath(__file__))
            lp = os.path.join(path, 'logo.jpg')
            pdf.drawImage(lp, 0, h-200, width=250, height=200)
            texto = pdf.beginText(50, h-300)
            texto.setFont("Helvetica", 18)
            texto.textLine("Dni: " + self.modelo[self.fila][0])
            texto.textLine("Nome: " + self.modelo[self.fila][1])
            texto.textLine("Apelidos: " + self.modelo[self.fila][2])
            texto.textLine("Direccion: " + self.modelo[self.fila][3])
            texto.textLine("Telefono: " + self.modelo[self.fila][4])
            texto.textLine("Codigo Postal: " + self.modelo[self.fila][5])
            texto.textLine("Sexo: " + self.modelo[self.fila][6])
            pdf.drawText(texto)
            pdf.showPage()
            pdf.save()
            mensaxe = Gtk.MessageDialog(self, 0, Gtk.MessageType.INFO, Gtk.ButtonsType.OK, "PDF Ficha Cliente creado")
            mensaxe.run()
            mensaxe.destroy()

        if self.combo.get_active_text()=="Pedidos Cliente" and self.modelo[self.fila][0] is not None:
            dni = str(self.modelo[self.fila][0])


            pedidos = BaseDatos.obter_pedidos(self, dni)
            listas = []

            for pedido in pedidos:
                listas.append(pedido)




            filename = self.modelo[self.fila][0] +"-pedido" + ".pdf"
            w, h = A4
            pdf = canvas.Canvas(filename, pagesize=A4)
            path = os.path.dirname(os.path.abspath(__file__))
            lp = os.path.join(path, 'logo.jpg')
            pdf.drawImage(lp, 0, h-200, width=250, height=200)
            texto = pdf.beginText(50, h-300)
            texto.setFont("Helvetica", 18)
            for lista in listas:
                texto.textLine("ID: " + str(lista[0]))
                texto.textLine("Dni: " + lista[1])
                texto.textLine("Codigo: " + lista[2])
                texto.textLine("Cantidade: " + str(lista[3]))
                texto.textLine("---------------------------------------------------------------")
            pdf.drawText(texto)
            pdf.showPage()
            pdf.save()
            mensaxe = Gtk.MessageDialog(self, 0, Gtk.MessageType.INFO, Gtk.ButtonsType.OK, "PDF Pedidos Cliente creado")
            mensaxe.run()
            mensaxe.destroy()



    def on_volver_clicked(self, button):
        """
        Método para cerrar a ventá actual e volver a pantalla Menu
        :param button: boton
        :return: Nada
        """
        menus.Menu()
        self.set_visible(False)



