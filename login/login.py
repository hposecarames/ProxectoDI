import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from baseDatos.metodosBD import BaseDatos
from menu import menus

con = BaseDatos.conectar()
BaseDatos.crear_taboas()



class Login(Gtk.Window):

    def __init__(self):
        """
        Método constructor, aquí definimos tódolos elementos que constituen a ventá de Login
        """

        Gtk.Window.__init__(self, title="Login")
        self.set_default_size(300, 200)
        self.set_border_width(10)
        self.grid_login = Gtk.Grid()
        self.grid_login.set_border_width(10)
        self.grid_login.set_column_spacing(20)
        self.grid_login.set_row_spacing(20)
        self.add(self.grid_login)

        self.et_usuario = Gtk.Label('Usuario', halign= Gtk.Align.START)
        self.et_contrasinal = Gtk.Label('Contrasinal', halign=Gtk.Align.START)

        self.entrada_usuario = Gtk.Entry()
        self.entrada_contrasinal = Gtk.Entry()

        self.btn_aceptar = Gtk.Button("ACEPTAR")
        self.btn_aceptar.connect('clicked', self.on_aceptar_clicked)

        self.grid_login.add(self.et_usuario)
        self.grid_login.attach_next_to(self.entrada_usuario, self.et_usuario, Gtk.PositionType.RIGHT, 1, 1)
        self.grid_login.attach_next_to(self.et_contrasinal, self.et_usuario, Gtk.PositionType.BOTTOM, 1, 1)
        self.grid_login.attach_next_to(self.entrada_contrasinal, self.et_contrasinal, Gtk.PositionType.RIGHT, 1, 1)
        self.grid_login.attach_next_to(self.btn_aceptar, self.entrada_contrasinal, Gtk.PositionType.BOTTOM, 1, 1)

        self.connect('destroy', Gtk.main_quit)
        self.show_all()
    def on_aceptar_clicked(self, button):
        """
        Método que recolle os datos das entradas usuario e contrasinal e fai a chamada a base de datos para consultar
         que coincidan, se os datos coinciden inicia a clase Menu
        :param button: boton aceptar
        :return: Nada
        """
        con = BaseDatos.conectar()
        usuario = self.entrada_usuario.get_text()
        contrasinal = self.entrada_contrasinal.get_text()
        datos = BaseDatos.obter_usuario(con, usuario, contrasinal)
        if datos[0][0] > 0:
            menus.Menu()
            self.set_visible(False)






if __name__ == "__main__":
    Login()
    Gtk.main()