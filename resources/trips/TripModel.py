from app import db
from datetime import datetime

class TripModel(db.Model):
    
    __tablename__ = 'trips'
    
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable = False)
    trip_date = db.Column(db.String, nullable = False)
    location = db.Column(db.String, nullable = False)
    body = db.Column(db.String, nullable = False)
    keywords = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable = False)
    timestamp = db.Column(db.String, default = datetime.utcnow)
    
#     class TripSchema(Schema):
#   id = fields.Str(dump_only = True)
#   timestamp = fields.Str(dump_only = True)
#   trip_date = fields.Str(required = True)
#   location = fields.Str(required = True)
#   user_id = fields.Str(required = True)
#   body = fields.Str()


    def __repr__(self):
        return f'Trip: {self.body}'
    
    def save(self):
        db.session.add(self)
        db.session.commit()
        
    def delete(self):
        db.session.delete(self)
        db.session.commit()