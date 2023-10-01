from flask_smorest import Blueprint

#any route ("/") with the bp prefix will use the url listed
bp = Blueprint('trip', __name__, url_prefix='/trip')

#Importing Files
from . import routes