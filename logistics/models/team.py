from logistics import db
from logistics.models.base import BaseModel

class Team(db.Model, BaseModel):
    """Team model"""

    __tablename__ = "teams"

    name = db.Column(db.String(20), nullable=False)
    abbreviation = db.Column(db.DateTime, nullable=False)

    # one to many
    requests = db.relationship("Request", back_populates="team")

    def __repr__(self):
        return "{name} - {abbreviation}".format(name=self.name, abbreviation=self.abbreviation)