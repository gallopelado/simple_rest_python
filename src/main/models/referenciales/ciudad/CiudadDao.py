from src.main.db.ConexionDb import ConexionDb

class CiudadDao:
    
    def listarTodos(self):
        conexion = ConexionDb()
        try:
            cursor = conexion.con.cursor()
            cursor.execute("SELECT id, descripcion FROM public.ciudades")
            items = cursor.fetchall()
            lista = []
            for item in items:
                lista.append(dict(ciu_id=item[0], ciu_descripcion=item[1]))
            cursor.close()
            conexion.con.close()
            return lista
        except conexion.con.Error as e:
            print(e.pgerror)

    def agregar(self, descripcion):
        try:
            conexion = ConexionDb()
            cursor = conexion.con.cursor()
            cursor.execute("INSERT INTO public.ciudades(descripcion) VALUES(%s)", (descripcion.upper(),))
            conexion.con.commit()
            cursor.close()
            conexion.con.close()
            return True
        except conexion.con.Error as e:
            print(e.pgerror)

    def modificar(self, idciudad, descripcion):
        try:
            conexion = ConexionDb()
            cursor = conexion.con.cursor()
            cursor.execute("UPDATE public.ciudades SET descripcion = %s WHERE id = %s", (descripcion.upper(), idciudad,))
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
            cursor.execute("SELECT id, descripcion FROM public.ciudades WHERE id = %s", (id,))
            item = cursor.fetchone()
            cursor.close()
            conexion.con.close()
            return dict(ciu_id=item[0], ciu_descripcion=item[1])
        except conexion.con.Error as e:
            return e.pgerror

    def eliminar(self, id):
        try:
            conexion = ConexionDb()
            cursor = conexion.con.cursor()
            cursor.execute("DELETE FROM public.ciudades WHERE id = %s", (id,))
            conexion.con.commit()
            cursor.close()
            conexion.con.close()
            return True
        except conexion.con.Error as e:
            return e.pgerror