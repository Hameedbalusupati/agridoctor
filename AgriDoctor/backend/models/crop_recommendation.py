from ..database.db import db


class CropRecommendation(db.Model):
    __tablename__ = "crop_recommendations"

    id = db.Column(db.Integer, primary_key=True)
    farmer_id = db.Column(db.Integer, db.ForeignKey("farmers.id"), nullable=False)
    recommended_crops = db.Column(db.Text)
    input_conditions = db.Column(db.Text)
    model_scores = db.Column(db.Text)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), onupdate=db.func.now())

    farmer = db.relationship("Farmer", back_populates="crop_recommendations")
