import sqlite3
import os

class BaseDatos:

    @staticmethod
    def conectar():
        """
        Método que crea unha conexion a base de datos

        :return: Obxeto conexion
        """

        try:
            path = os.path.dirname(os.path.abspath(__file__))
            bd = os.path.join(path, 'database.db')
            con = sqlite3.connect(bd)

        except sqlite3.DatabaseError as erro_conexion:
            print(erro_conexion)
        return con

    @staticmethod
    def crear_taboas():
        """
        Método que crea as táboas da base de datos

        :return: Non devolve ningún parámetro
        """

        try:
            cursor_obx = BaseDatos.conectar()
            cursor_obx.execute(("""CREATE TABLE IF NOT EXISTS usuarios(
                                usuario TEXT PRIMARY KEY,
                                contrasinal TEXT NOT NULL)"""))

            cursor_obx.execute("""CREATE TABLE IF NOT EXISTS clientes(
                            dni TEXT PRIMARY KEY,
                            nome TEXT NOT NULL,
                            apelidos TEXT NOT NULL,
                            direccion TEXT NOT NULL,
                            telefono TEXT NOT NULL,
                            cp TEXT NOT NULL,
                            sexo TEXT NOT NULL)""")

            cursor_obx.execute("""CREATE TABLE IF NOT EXISTS productos(
                                        codigo TEXT PRIMARY KEY,
                                        nome TEXT NOT NULL,
                                        prezo INTEGER NOT NULL)""")

            cursor_obx.execute("""CREATE TABLE IF NOT EXISTS pedidos(
                                        id INTEGER PRIMARY KEY,                            
                                        dni TEXT NOT NULL,
                                        codigo TEXT NOT NULL,
                                        cantidade INTEGER NOT NULL,
                                        FOREIGN KEY (dni) REFERENCES clientes(dni),
                                        FOREIGN KEY (codigo) REFERENCES productos(codigo))""")


            cursor_obx.commit()
            cursor_obx.close()

        except sqlite3.DatabaseError as erro_crear_taboa:
            print("Erro o crear a táboa " + str(erro_crear_taboa))

    def insertar_usuario(self, ususario, contrasinal):
        """
        Método que inserta un usuario

        :param ususario: Usuario
        :param contrasinal: Contrasinal do usuario
        :return: True se inserta o usuario ou False se faltan datos ou hai datos errados
        """

        try:
            cursor_obx = BaseDatos.conectar()
            cursor_obx.execute("""INSERT INTO usuarios(usuario, contrasinal)
                                VALUES (?,?)""", (ususario, contrasinal))
            cursor_obx.commit()
            cursor_obx.close()
            return True
        except sqlite3.DatabaseError as erro_login:
            print("Erro no login" + str(erro_login))
            return False

    def insertar_cliente(self, dni, nome, apelidos, direccion, telefono, cp, sexo):
        """
        Método para insertar un cliente na base de datos
        :param dni: Dni do cliente
        :param nome: Nome do cliente
        :param apelidos: Apelidos do cliente
        :param direccion: Dirección do cliente
        :param telefono: Teléfono do cliente
        :param cp: Código postal do cliente
        :param sexo: Sexo do cliente
        :return: True se inserta o cliente ou False se faltan datos ou hai datos errados
        """

        try:
            if (dni != "" and nome != "" and apelidos != "" and direccion != "" and telefono != "" and cp != "" and sexo != ""):
                cursor_obx = BaseDatos.conectar()
                cursor_obx.execute("""INSERT INTO clientes(dni, nome, apelidos, direccion, telefono, cp, sexo)
                                    VALUES (?,?,?,?,?,?,?)""", (dni, nome, apelidos, direccion, telefono, cp, sexo))
                cursor_obx.commit()
                cursor_obx.close()
                return True



        except sqlite3.DatabaseError as erro_cliente:
            print("Erro o insertar o cliente " + str(erro_cliente))
            return False

    def insertar_producto(self, codigo, nome, prezo):
        """
        Método para insertar un producto na base de datos
        :param codigo: Código do producto
        :param nome: Nome do producto
        :param prezo: Prezo do producto
        :return: True se inserta o cliente ou False se faltan datos ou hai datos errados
        """

        try:
            if (codigo != "" and nome != "" and prezo != ""):
                cursor_obx = BaseDatos.conectar()
                cursor_obx.execute("""INSERT INTO productos(codigo, nome, prezo)
                                    VALUES (?,?,?)""", (codigo, nome, prezo))
                cursor_obx.commit()
                cursor_obx.close()
                return True

        except sqlite3.DatabaseError as erro_producto:
            print("Erro o insertar o producto " + str(erro_producto))
            return False

    def insertar_pedido(self, dni, codigo, cantidade):
        """
        Método para insertar un pedido na base de datos
        :param dni: Dni do cliente
        :param codigo: Código do producto
        :param cantidade: Cantidade do producto
        :return: True se inserta o pedido ou False se faltan datos ou hai datos errados
        """

        try:
            if(dni != "" and codigo != "" and cantidade != ""):
                cursor_obx = BaseDatos.conectar()
                cursor_obx.execute("""INSERT INTO pedidos(dni, codigo, cantidade)
                                    VALUES (?,?,?)""", (dni, codigo, cantidade))
                cursor_obx.commit()
                cursor_obx.close()
                return True

        except sqlite3.DatabaseError as erro_pedido:
            print("Erro o insertar o pedido " + str(erro_pedido))
            return False

    def modificar_cliente(self, nome, apelidos, direccion, telefono, cp, sexo, dni):
        """
        Método para modificar un cliente
        :param nome: Nome do cliente
        :param apelidos: Apelidos do cliente
        :param direccion: Dirección do cliente
        :param telefono: Teléfono do cliente
        :param cp: Código Postal do cliente
        :param sexo: Sexo do cliente
        :param dni: Dni do cliente
        :return: True se modifica o cliente ou False se faltan datos ou hai datos errados
        """

        if (nome != "" and apelidos != "" and direccion != "" and telefono != "" and cp != "" and sexo != "" and dni != ""):
            try:
                cursor_obx = BaseDatos.conectar()
                cursor_obx.execute("""UPDATE clientes SET nome=?, apelidos=?, direccion=?, telefono=?, cp=?, sexo=? 
                                    WHERE dni=?""",(nome, apelidos, direccion, telefono, cp, sexo, dni))
                cursor_obx.commit()
                cursor_obx.close()
                return True

            except sqlite3.DatabaseError as erro_modificar:
                print("Erro o modificar o cliente " + str(erro_modificar))
                return False

    def modificar_producto(self, codigo, nome, prezo):
        """
        Método para modificar un producto
        :param codigo: Código do producto
        :param nome: Nome do producto
        :param prezo: Prezo do producto
        :return: True se modica o producto ou False se faltan datos ou hai datos errados
        """

        if (codigo != "" and nome != "" and prezo != ""):
            try:
                cursor_obx = BaseDatos.conectar()
                cursor_obx.execute("""UPDATE productos SET nome=?, prezo=? WHERE codigo=?""", (nome, prezo, codigo))
                cursor_obx.commit()
                cursor_obx.close()
                return True

            except sqlite3.DatabaseError as erro_modificar:
                print("Erro o modicar o producto " + str(erro_modificar))
                return False

    def modificar_pedido(self, id, dni, codigo, cantidade):
        """
        Método para modificar un pedido
        :param id: ID do pedido
        :param dni: Dni do cliente
        :param codigo: Código do producto
        :param cantidade: Cantidade do producto
        :return: True se modica o pedido ou False se faltan datos ou hai datos errados
        """

        if (id != "" and dni != "" and codigo != "" and cantidade != ""):
            try:
                cursor_obx = BaseDatos.conectar()
                cursor_obx.execute("""UPDATE productos SET dni=?, codigo=?, cantidade=? WHERE id=?""", (dni, codigo, cantidade, id))
                cursor_obx.commit()
                cursor_obx.close()
                return True

            except sqlite3.DatabaseError as erro_modificar:
                print("Erro o modicar o pedido " + str(erro_modificar))
                return False


    def eliminar_cliente(self, dni):
        """
        Método para eliminar un cliente
        :param dni: Dni do cliente
        :return: True se elimina o cliente ou False se faltan datos ou hai datos errados
        """

        if dni != "":
            try:
                cursor_obx = BaseDatos.conectar()
                cursor_obx.execute("DELETE FROM clientes WHERE dni = '"+ dni +"'")
                cursor_obx.commit()
                cursor_obx.close()
                return True

            except sqlite3.DatabaseError as erro_eliminar:
                print("Erro o eliminar o cliente " + str(erro_eliminar))
                return False

    def eliminar_producto(self, codigo):
        """
        Método para eliminar un producto
        :param codigo: Código do producto
        :return: True se elimina o producto ou False se faltan datos ou hai datos errados
        """

        if codigo != "":
            try:
                cursor_obx = BaseDatos.conectar()
                cursor_obx.execute("DELETE FROM productos WHERE codigo = '"+ codigo +"'")
                cursor_obx.commit()
                cursor_obx.close()
                return True

            except sqlite3.DatabaseError as erro_eliminar:
                print("Erro o eliminar o producto " + str(erro_eliminar))
                return False

    def eliminar_pedido(self, id):
        """
        Método para eliminar un pedido
        :param id: ID do pedido
        :return: True se elimina o pedido ou False se faltan datos ou hai datos errados
        """

        if id != "":
            try:
                cursor_obx = BaseDatos.conectar()
                cursor_obx.execute("DELETE FROM pedidos WHERE id = '"+ id +"'")
                cursor_obx.commit()
                cursor_obx.close()
                return True

            except sqlite3.DatabaseError as erro_eliminar:
                print("Erro o eliminar o pedido " + str(erro_eliminar))
                return False


    def obter_datos(self):
        """
        Método para listar tódolos datos dos clientes
        :return: Lista de tódolos  datos dos clientes
        """

        try:
            cursor_obx = BaseDatos.conectar()
            consulta = cursor_obx.execute("SELECT * FROM clientes")
            datos = consulta.fetchall()
            return datos

        except sqlite3.DatabaseError as erro_datos:
            print("Erro o obter os datos " + str(erro_datos))

        finally:
            cursor_obx.close()

    def obter_pedidos(self, dni):
        """
        Método para listar tódolos pedidos de un cliente
        :param dni: Dni do cliente
        :return: Lista de tódolos pedidos feitos por ese cliente
        """

        try:
            cursor_obx = BaseDatos.conectar()
            consulta = cursor_obx.execute("SELECT * FROM pedidos WHERE dni = '"+ dni +"'")
            datos = consulta.fetchall()

            return datos

        except sqlite3.DatabaseError as erro_pedido:
            print("Erro o obter o pedido " + str(erro_pedido))

        finally:
            cursor_obx.close()

    def obter_usuario(self, usuario, contrasinal):
        """
        Método para contar se hai algún usuario con ese nome e contrasinal
        :param usuario: Identificador do usuario
        :param contrasinal: Contrasinal do usuario
        :return: 1 se econtra algún usuario e contrasinal que coincida ou 0 se non encontra nada
        """

        try:
            cursor_obx = BaseDatos.conectar()
            consulta = cursor_obx.execute("SELECT count(*) FROM usuarios WHERE usuario = ? and contrasinal = ?", (usuario, contrasinal))
            datos = consulta.fetchall()
            return datos

        except sqlite3.DatabaseError as erro_usuario:
            print("Usuario ou contrasinal erróneos" + str(erro_usuario))

