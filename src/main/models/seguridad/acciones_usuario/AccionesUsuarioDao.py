from src.main.db.ConexionDb import ConexionDb
from src.main.models.seguridad.acciones_usuario.AccionesUsuarioDto import AccionesUsuarioDto

class AccionesUsuarioDao:
    
    def listarTodos(self):
        conexion = ConexionDb()
        try:
            cursor = conexion.con.cursor()
            cursor.execute("SELECT id, accion, descripcion FROM public.acciones_usuario")
            items = cursor.fetchall()
            lista = []
            for item in items:
                lista.append(AccionesUsuarioDto(item[0], item[1], item[2]))
            cursor.close()
            conexion.con.close()
            return lista
        except conexion.con.Error as e:
            print(e.pgerror)

    def agregar(self, accion, descripcion):
        try:
            conexion = ConexionDb()
            cursor = conexion.con.cursor()
            cursor.execute("INSERT INTO public.acciones_usuario(accion, descripcion) VALUES(%s, %s)", (accion, descripcion,))
            conexion.con.commit()
            cursor.close()
            conexion.con.close()
            return True
        except conexion.con.Error as e:
            print(e.pgerror)

    def modificarAccion(self, id, accion):
        try:
            conexion = ConexionDb()
            cursor = conexion.con.cursor()
            cursor.execute("UPDATE public.acciones_usuario SET accion = %s WHERE id = %s", (accion, id,))
            conexion.con.commit()
            cursor.close()
            conexion.con.close()
            return True
        except conexion.con.Error as e:
            return e.pgerror
        
    def modificarDescripcion(self, id, descripcion):
        try:
            conexion = ConexionDb()
            cursor = conexion.con.cursor()
            cursor.execute("UPDATE public.acciones_usuario SET descripcion = %s WHERE id = %s", (descripcion, id,))
            conexion.con.commit()
            cursor.close()
            conexion.con.close()
            return True
        except conexion.con.Error as e:
            return e.pgerror

    def getById(self, id):
        try:
            conexion = ConexionDb()
            cursor = conexion.con.cursor()
            cursor.execute("SELECT id, accion, descripcion FROM public.acciones_usuario WHERE id = %s", (id,))
            item = cursor.fetchone()
            cursor.close()
            conexion.con.close()
            return AccionesUsuarioDto(item[0], item[1], item[2])
        except conexion.con.Error as e:
            return e.pgerror

    def eliminar(self, id):
        try:
            conexion = ConexionDb()
            cursor = conexion.con.cursor()
            cursor.execute("DELETE FROM public.acciones_usuario WHERE id = %s", (id,))
            conexion.con.commit()
            cursor.close()
            conexion.con.close()
            return True
        except conexion.con.Error as e:
            return e.pgerror