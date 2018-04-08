from logistics import db
from logistics.models.base import BaseModel

class Request(db.Model, BaseModel):
    """Request model"""

    __tablename__ = "requests"

    owner = db.Column(db.String(20), nullable=False)
    team = db.Column(db.String(20), nullable=False)

    # many to one
    event_id = db.Column(db.Integer, db.ForeignKey('events.id'))
    event = db.relationship("Event", back_populates="requests")

    team_id = db.Column(db.Integer, db.ForeignKey('teams.id'))
    team = db.relationship("Team", back_populates="requests")

    def __repr__(self):
        return "{event} - {team}".format(event=self.event, team=self.team)