import sqlite3
import os

class BaseDatos:

    @staticmethod
    def conectar():

        try:
            path = os.path.dirname(os.path.abspath(__file__))
            bd = os.path.join(path, 'database.db')
            con = sqlite3.connect(bd)

        except sqlite3.DatabaseError as erro_conexion:
            print(erro_conexion)
        return con

    @staticmethod
    def crear_taboas():

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

        try:
            if (dni != "" and nome != "" and apelidos != "" and direccion != "" and telefono != "" and cp != "" and sexo != ""):
                cursor_obx = BaseDatos.conectar()
                cursor_obx.execute("""INSERT INTO clientes(dni, nome, apelidos, direccion, telefono, cp, sexo)
                                    VALUES (?,?,?,?,?,?,?)""", (dni, nome, apelidos, direccion, telefono, cp, sexo))
                cursor_obx.commit()
                cursor_obx.close()



        except sqlite3.DatabaseError as erro_cliente:
            print("Erro o insertar o cliente " + str(erro_cliente))

    def insertar_producto(self, codigo, nome, prezo):

        try:
            if (codigo != "" and nome != "" and prezo != ""):
                cursor_obx = BaseDatos.conectar()
                cursor_obx.execute("""INSERT INTO productos(codigo, nome, prezo)
                                    VALUES (?,?,?)""", (codigo, nome, prezo))
                cursor_obx.commit()
                cursor_obx.close()

        except sqlite3.DatabaseError as erro_producto:
            print("Erro o insertar o producto " + str(erro_producto))

    def insertar_pedido(self, dni, codigo, cantidade):

        try:
            if(dni != "" and codigo != "" and cantidade != ""):
                cursor_obx = BaseDatos.conectar()
                cursor_obx.execute("""INSERT INTO pedidos(dni, codigo, cantidade)
                                    VALUES (?,?,?)""", (dni, codigo, cantidade))
                cursor_obx.commit()
                cursor_obx.close()

        except sqlite3.DatabaseError as erro_pedido:
            print("Erro o insertar o pedido " + str(erro_pedido))


    def modificar_cliente(self, nome, apelidos, direccion, telefono, cp, sexo, dni):

        if (nome != "" and apelidos != "" and direccion != "" and telefono != "" and cp != "" and sexo != "" and dni != ""):
            try:
                cursor_obx = BaseDatos.conectar()
                cursor_obx.execute("""UPDATE clientes SET nome=?, apelidos=?, direccion=?, telefono=?, cp=?, sexo=? 
                                    WHERE dni=?""",(nome, apelidos, direccion, telefono, cp, sexo, dni))
                cursor_obx.commit()
                cursor_obx.close()

            except sqlite3.DatabaseError as erro_modificar:
                print("Erro o modificar o cliente " + str(erro_modificar))

    def modificar_producto(self, codigo, nome, prezo):

        if (codigo != "" and nome != "" and prezo != ""):
            try:
                cursor_obx = BaseDatos.conectar()
                cursor_obx.execute("""UPDATE productos SET nome=?, prezo=? WHERE codigo=?""", (nome, prezo, codigo))
                cursor_obx.commit()
                cursor_obx.close()

            except sqlite3.DatabaseError as erro_modificar:
                print("Erro o modicar o producto " + str(erro_modificar))

    def modificar_pedido(self, id, dni, codigo, cantidade):

        if (id != "" and dni != "" and codigo != "" and cantidade != ""):
            try:
                cursor_obx = BaseDatos.conectar()
                cursor_obx.execute("""UPDATE productos SET dni=?, codigo=?, cantidade=? WHERE id=?""", (dni, codigo, cantidade, id))
                cursor_obx.commit()
                cursor_obx.close()

            except sqlite3.DatabaseError as erro_modificar:
                print("Erro o modicar o pedido " + str(erro_modificar))


    def eliminar_cliente(self, dni):

        if dni != "":
            try:
                cursor_obx = BaseDatos.conectar()
                cursor_obx.execute("DELETE FROM clientes WHERE dni = '"+ dni +"'")
                cursor_obx.commit()
                cursor_obx.close()

            except sqlite3.DatabaseError as erro_eliminar:
                print("Erro o eliminar o cliente " + str(erro_eliminar))

    def eliminar_producto(self, codigo):

        if codigo != "":
            try:
                cursor_obx = BaseDatos.conectar()
                cursor_obx.execute("DELETE FROM productos WHERE codigo = '"+ codigo +"'")
                cursor_obx.commit()
                cursor_obx.close()

            except sqlite3.DatabaseError as erro_eliminar:
                print("Erro o eliminar o producto " + str(erro_eliminar))


    def obter_datos(self):

        try:
            cursor_obx = BaseDatos.conectar()
            consulta = cursor_obx.execute("SELECT * FROM clientes")
            datos = consulta.fetchall()
            return datos

        except sqlite3.DatabaseError as erro_datos:
            print("Erro o obter os datos" + str(erro_datos))

        finally:
            cursor_obx.close()

    def obter_usuario(self, usuario, contrasinal):

        try:
            cursor_obx = BaseDatos.conectar()
            consulta = cursor_obx.execute("SELECT count(*) FROM usuarios WHERE usuario = ? and contrasinal = ?", (usuario, contrasinal))
            datos = consulta.fetchall()
            print(datos[0][0])
            return datos

        except sqlite3.DatabaseError as erro_usuario:
            print("Usuario ou contrasinal erróneos" + str(erro_usuario))

