from ..database.db import db


class Farmer(db.Model):
    __tablename__ = "farmers"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False, unique=True)
    district = db.Column(db.String(120))
    village = db.Column(db.String(120))
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), onupdate=db.func.now())

    user = db.relationship("User", back_populates="farmer_profile")
    farms = db.relationship("Farm", back_populates="farmer")
    predictions = db.relationship("DiseasePrediction", back_populates="farmer")
    soil_records = db.relationship("SoilRecord", back_populates="farmer")
    crop_recommendations = db.relationship("CropRecommendation", back_populates="farmer")
    notifications = db.relationship("Notification", back_populates="farmer")
