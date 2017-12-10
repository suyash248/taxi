from taxi import db
import datetime
import enum

class ReqStatus(enum.Enum):
    WAITING = "WAITING"
    ONGOING = "ONGOING"
    COMPLETED = "COMPLETED"

class Request(db.Model):
    __tablename__ = "requests"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    customer_id = db.Column(db.String, nullable=False)
    driver_id = db.Column(db.String, nullable=True)
    req_status = db.Column(db.Enum(ReqStatus), default=ReqStatus.WAITING)
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    picked_up = db.Column(db.DateTime, nullable=True)
    completed_at = db.Column(db.DateTime, nullable=True)

    def __init__(self, customer_id):
        self.customer_id = customer_id

    def create(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def all(cls):
        return db.session.query(cls).all()

    @classmethod
    def filter(cls, filter_args=None):
        res = db.session.query(cls).filter_by(**filter_args)
        return res

    def as_dict(self):
        return {
            "request_id": self.id,
            "customer_id": self.customer_id,
            "driver_id": self.driver_id,
            "req_status": str(self.req_status.name),
            "created_at": self.created_at.isoformat()+'Z',
            "picked_up": self.picked_up.isoformat()+'Z' if self.picked_up is not None else None,
            "completed_at": self.completed_at.isoformat()+'Z' if self.completed_at is not None else None
        }

