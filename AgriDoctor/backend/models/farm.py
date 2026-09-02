from ..database.db import db


class Farm(db.Model):
    __tablename__ = "farms"

    id = db.Column(db.Integer, primary_key=True)
    farmer_id = db.Column(db.Integer, db.ForeignKey("farmers.id"), nullable=False)
    farm_name = db.Column(db.String(120), nullable=False)
    location = db.Column(db.String(200))
    state = db.Column(db.String(120))
    district = db.Column(db.String(120))
    village = db.Column(db.String(120))
    area = db.Column(db.Float)
    soil_type = db.Column(db.String(100))
    irrigation_type = db.Column(db.String(100))
    current_crop = db.Column(db.String(100))
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), onupdate=db.func.now())

    farmer = db.relationship("Farmer", back_populates="farms")
