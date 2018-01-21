from app import db
from sqlalchemy_utils import TSVectorType

# Create our database model
class Picture(db.Model):
    __tablename__ = "pictures"
    id = db.Column(db.Integer, primary_key=True)
    vector = db.Column(TSVectorType, unique=True)
    path = db.Column(db.String(120), unique=True)
    
    def __init__(self, vector, path):
        self.vector = vector
        self.path = path