from logistics import db
from logistics.models.base import BaseModel

class Event(db.Model, BaseModel):
    """Event model"""

    __tablename__ = "events"

    name = db.Column(db.String(20), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    requests = db.Column(db.String(50), nullable=False)

    # many to one
    location_id = db.Column(db.Integer, db.ForeignKey('locations.id'))
    location = db.relationship("Location", back_populates="events")

    # one to many
    requests = db.relationship("Request", back_populates="event")

    def __repr__(self):
        return "{name} - {location} - {date}".format(name=self.name, location=self.location,
                                                           date=self.date)