from flask import request
from uuid import uuid4 # imports universally unique identifiers(4 creates the most random of the identefiers)
from flask.views import MethodView # Dispatches request methods to the corresponding instance methods. For example, if you implement a get method, it will be used to handle GET requests.
from flask_smorest import abort #imports function abort from smorest library (abort is used when an error code is responded)
from sqlalchemy.exc import IntegrityError
from flask_jwt_extended import jwt_required, get_jwt_identity

from resources.users import models

from .TripModel import TripModel
from schemas import TripSchema
from . import bp
#^^^^^^imports blueprint from __init__

@bp.route('/')
class TripList(MethodView):
  
  @jwt_required()
  @bp.response(200, TripSchema(many=True))
  def get(self):
    return TripModel.query.all()

  @jwt_required()
  @bp.arguments(TripSchema)
  @bp.response(200, TripSchema)
  def post(self, trip_data):
    user_id = get_jwt_identity()
    trip = TripModel(**trip_data)
    try:
      trip.save()
      return trip
    except IntegrityError:
      abort(400, message="Invalid User Id")

@bp.route('/<trip_id>')
class Trip(MethodView):
  
  @jwt_required()
  @bp.response(200, TripSchema)
  def get(self, trip_id):
    trip = TripModel.query.get(trip_id)
    if trip:
      return trip
    abort(400, message='Invalid Trip Id')

  @jwt_required()
  @bp.arguments(TripSchema)
  @bp.response(200, TripSchema)
  def put(self, trip_data, trip_id):
    trip = TripModel.query.get(trip_id)
    if trip and trip_data['body']:
      user_id = get_jwt_identity()
      if trip.user_id == user_id:
        trip.body = trip_data['body']
        trip.save()
        return trip
      else:
        abort(401, message='Unauthorized')
    abort(400, message='Invalid Trip Data')

  @jwt_required()
  def delete(self, trip_id):
     user_id = get_jwt_identity()
     trip = TripModel.query.get(trip_id)
     if trip:
       if trip.user_id == user_id:
        trip.delete()
        return {'message' : 'Trip Deleted'}, 202
       abort(401, message='User doesn\'t have rights')
     abort(400, message='Invalid Trip Id')