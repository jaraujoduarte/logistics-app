from datetime import datetime
from logistics import db
from logistics.utils import SerializerMixin

class BaseModel(SerializerMixin):
    """Base object for shared behavior across models"""

    id = db.Column(db.Integer, primary_key=True)
    created_date = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
    updated_date = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

    @classmethod
    def create(cls, **kwargs):
        """Adds new model to database"""
        model = cls(**kwargs)
        db.session.add(model)
        db.session.commit()
        return model

    @classmethod
    def update(cls, model):
        model.updated_date = datetime.utcnow()
        db.session.commit()
        return model