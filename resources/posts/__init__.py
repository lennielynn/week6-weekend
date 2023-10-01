from flask_smorest import Blueprint

#any route ("/") with the bp prefix will use the url listed
bp = Blueprint('posts', __name__, url_prefix='/post')

#Importing Files
from . import routes