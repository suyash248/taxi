from taxi import db
import datetime
import enum

class ReqStatus(enum.Enum):
    WAITING = "WAITING"
    ONGOING = "ONGOING"
    COMPLETED = "COMPLETED"

class Request(db.Model):
    __tablename__ = "requests"
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, primary_key=True)
    driver_id = db.Column(db.Integer, primary_key=True)
    req_status = db.Column(db.Enum(ReqStatus))
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def __init__(self, customer_id):
        self.customer_id = customer_id

    # def __repr__(self):
    #     return

