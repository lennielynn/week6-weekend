from flask import Flask # - flask algorithm imported
from flask_smorest import Api # - smorest - a flask extention that allows us to create APIs
from flask_sqlalchemy import SQLAlchemy # - SQLAlchemy - how Flask connects to a database
from flask_migrate import Migrate  # - Migrate - the git of databases
from flask_jwt_extended import JWTManager


from Config import Config # import configuration file for our Flask instance (Config)
app = Flask(__name__) # - assignes Flask Algorithm to the name 'app'
app.config.from_object(Config) 

db = SQLAlchemy(app) # - assigning name 'db' to SQLAlchamy with the application of Flask algorithm (app)
migrate = Migrate(app, db) # - assigning name 'migrate' to imported Migrate function with the application of the DataBase(db) and Flask algorithm(app)
api = Api(app) # - assigning the name 'api' to the imported API with the application of Flask (app)
jwt = JWTManager(app)

from resources.users import bp as user_bp # importing Blueprints(user_bp)
api.register_blueprint(user_bp) # applying blueprint to api
from resources.posts import bp as post_bp # importing Blueprints(post_bp)
api.register_blueprint(post_bp) # applying blueprint to api
from resources.trips import bp as trip_bp
api.register_blueprint(trip_bp)

#Importing Files/creating tables
from resources.users import routes
from resources.posts import routes
from resources.trips import routes

from resources.users.models import UserModel
from resources.posts.PostModel import PostModel
from resources.trips.TripModel import TripModel