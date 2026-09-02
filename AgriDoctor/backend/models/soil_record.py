from ..database.db import db


class SoilRecord(db.Model):
    __tablename__ = "soil_records"

    id = db.Column(db.Integer, primary_key=True)
    farmer_id = db.Column(db.Integer, db.ForeignKey("farmers.id"), nullable=False)
    nitrogen = db.Column(db.Float)
    phosphorus = db.Column(db.Float)
    potassium = db.Column(db.Float)
    ph = db.Column(db.Float)
    moisture = db.Column(db.Float)
    temperature = db.Column(db.Float)
    rainfall = db.Column(db.Float)
    soil_condition = db.Column(db.String(120))
    nutrient_status = db.Column(db.Text)
    suitable_crops = db.Column(db.Text)
    recommendations = db.Column(db.Text)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), onupdate=db.func.now())

    farmer = db.relationship("Farmer", back_populates="soil_records")
