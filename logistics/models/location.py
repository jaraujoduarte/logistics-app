from logistics import db
from logistics.models.base import BaseModel

class Location(db.Model, BaseModel):
    """Location model"""

    __tablename__ = "locations"

    name = db.Column(db.String(20), nullable=True)
    loc_type = db.Column('type', db.String(50), nullable=False)

    # one to many
    events = db.relationship("Event", back_populates="location")

    def __repr__(self):
        return "{name}".format(name=self.name)