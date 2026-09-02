from ..database.db import db


class DiseasePrediction(db.Model):
    __tablename__ = "disease_predictions"

    id = db.Column(db.Integer, primary_key=True)
    farmer_id = db.Column(db.Integer, db.ForeignKey("farmers.id"), nullable=False)
    crop_name = db.Column(db.String(120))
    disease_name = db.Column(db.String(180))
    confidence = db.Column(db.Float, default=0.0)
    severity = db.Column(db.String(60))
    symptoms = db.Column(db.Text)
    management = db.Column(db.Text)
    treatment = db.Column(db.Text)
    risk_level = db.Column(db.String(30), default="MEDIUM")
    image_path = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), onupdate=db.func.now())

    farmer = db.relationship("Farmer", back_populates="predictions")
