from flask import Flask

app = Flask(__name__)

from . import routes  # Importa las rutas de tu aplicación

