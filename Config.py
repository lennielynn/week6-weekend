#configuration of Flask instance
import os

class Config:
  PROPAGATE_EXCEPTIONS = True
  #if the ai gets any bugs it send it to us
  API_TITLE = 'TBug Rest Api'
  API_VERSION = 'v1'
  OPENAPI_VERSION = '3.0.3'
  OPENAPI_URL_PREFIX = '/' #required
  OPENAPI_SWAGGER_UI_PATH = '/'
# how we navigate to our documentation through our local server
  OPENAPI_SWAGGER_UI_URL = 'https://cdn.jsdelivr.net/npm/swagger-ui-dist/'
  SQLALCHEMY_DATABASE_URI = os.environ.get('SQLDATABASE_URL')
  JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY")
  SECRET_KEY = os.environ.get('SECRET_KEY')