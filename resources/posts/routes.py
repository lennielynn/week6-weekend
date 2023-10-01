from flask import request
from uuid import uuid4 # imports universally unique identifiers(4 creates the most random of the identefiers)
from flask.views import MethodView # Dispatches request methods to the corresponding instance methods. For example, if you implement a get method, it will be used to handle GET requests.
from flask_smorest import abort #imports function abort from smorest library (abort is used when an error code is responded)
from sqlalchemy.exc import IntegrityError
from flask_jwt_extended import jwt_required, get_jwt_identity

from resources.users import models

from .PostModel import PostModel
from schemas import PostSchema
from . import bp
#^^^^^^imports blueprint from __init__

@bp.route('/')
class PostList(MethodView):
  
  @jwt_required()
  @bp.response(200, PostSchema(many=True))
  def get(self):
    return PostModel.query.all()

  @jwt_required()
  @bp.arguments(PostSchema)
  @bp.response(200, PostSchema)
  def post(self, post_data):
    user_id = get_jwt_identity()
    p = PostModel(**post_data)
    try:
      p.save()
      return p
    except IntegrityError:
      abort(400, message="Invalid User Id")

@bp.route('/<post_id>')
class Post(MethodView):
  
  @jwt_required()
  @bp.response(200, PostSchema)
  def get(self, post_id):
    p = PostModel.query.get(post_id)
    if p:
      return p
    abort(400, message='Invalid Post Id')

  @jwt_required()
  @bp.arguments(PostSchema)
  @bp.response(200, PostSchema)
  def put(self, post_data, post_id):
    p = PostModel.query.get(post_id)
    if p and post_data['body']:
      user_id = get_jwt_identity()
      if p.user_id == user_id:
        p.body = post_data['body']
        p.save()
        return p
      else:
        abort(401, message='Unauthorized')
    abort(400, message='Invalid Post Data')

  @jwt_required()
  def delete(self, post_id):
     user_id = get_jwt_identity()
     p = PostModel.query.get(post_id)
     if p:
       if p.user_id == user_id:
        p.delete()
        return {'message' : 'Post Deleted'}, 202
       abort(401, message='User doesn\'t have rights')
     abort(400, message='Invalid Post Id')