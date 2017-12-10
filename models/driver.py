from taxi import db
import datetime

class Driver(db.Model):
    __tablename__ = "drivers"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    driver_id = db.Column(db.String, nullable=True)
    loc_x = db.Column(db.Integer, nullable=False)
    loc_y = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def __init__(self, driver_id):
        self.driver_id = driver_id

    def create(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def all(cls):
        return db.session.query(cls).all()

    @classmethod
    def by_id(cls, id):
        return db.session.query(cls).get(id)

    @classmethod
    def filter(cls, filter_args=None):
        res = db.session.query(cls).filter_by(**filter_args)
        return res

    @classmethod
    def filter_and_update(cls, filter_args=None, updated_args=None):
        res = db.session.query(cls).filter_by(**filter_args).update(updated_args)
        db.session.commit()
        return res

    def as_dict(self):
        return {
            "id": self.id,
            "driver_id": self.driver_id,
            "created_at": self.created_at.isoformat() + 'Z'
        }

