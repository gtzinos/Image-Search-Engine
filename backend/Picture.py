from app import db
from sqlalchemy_utils import TSVectorType
from sqlalchemy.dialects import postgresql

# Create our database model
class Picture(db.Model):
    __tablename__ = "pictures"
    id = db.Column(db.Integer, primary_key=True)
    vector = db.Column(postgresql.ARRAY(db.Float), unique=True)
    path = db.Column(db.String(120), unique=True)
    # &&&&&&&&********       Column("data", postgresql.ARRAY(Integer, dimensions=2))
#http://docs.sqlalchemy.org/en/latest/dialects/postgresql.html#sqlalchemy.dialects.postgresql.ARRAY
    def __init__(self, vector, path):
        self.vector = vector
        self.path = path