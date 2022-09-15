import os
from flask import Flask

app = Flask(__name__)

# Definimos rutas estáticas
app.config['APPLICATION_PROPERTIES'] = os.path.join(os.path.abspath(os.getcwd()), 'src/resources/application.properties.yaml')


# Modulos de referenciales
from src.main.rutas.referenciales.ciudad.ciudad_routes import ciudadMod

# Modulos de seguridad
from src.main.rutas.seguridad.acciones_usuario.acciones_usuario_routes import aur


# Raiz
api = "/apiv1"

# Registrar modulos de referenciales
modulo0 = f"{api}/referenciales"
app.register_blueprint(ciudadMod, url_prefix=f"{modulo0}/ciudad")

# Registrar modulos de seguridad
modulo0 = f"{api}/seguridad"
app.register_blueprint(aur, url_prefix=f"{modulo0}/acciones")

