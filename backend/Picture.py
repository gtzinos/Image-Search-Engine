from app import db
from sqlalchemy_utils import TSVectorType

from sqlalchemy.dialects.postgresql import TSVECTOR
from sqlalchemy.dialects import postgresql

# Create our database model
class Picture(db.Model):
    __tablename__ = "pictures"
    id = db.Column(db.Integer, primary_key=True)
    kp = db.Column(postgresql.ARRAY(db.Float()))
    features = db.Column(postgresql.ARRAY(db.Float()))
    cut_kp = db.Column(postgresql.ARRAY(db.Float()))
    cut_features = db.Column(postgresql.ARRAY(db.Float()))
    filename = db.Column(db.String(120), unique=True)

    # &&&&&&&&********       Column("data", postgresql.ARRAY(Integer, dimensions=2))
    #http://docs.sqlalchemy.org/en/latest/dialects/postgresql.html#sqlalchemy.dialects.postgresql.ARRAY
    def __init__(self, kp, features, cut_kp, cut_features, filename):
        self.kp = kp
        self.features = features
        self.cut_kp = cut_kp
        self.cut_features = cut_features
        self.filename = filename