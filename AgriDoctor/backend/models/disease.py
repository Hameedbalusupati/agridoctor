from ..database.db import db


class Disease(db.Model):
    __tablename__ = "diseases"

    id = db.Column(db.Integer, primary_key=True)
    crop = db.Column(db.String(120), nullable=False)
    disease_name = db.Column(db.String(180), nullable=False)
    symptoms = db.Column(db.Text)
    causes = db.Column(db.Text)
    severity = db.Column(db.String(50))
    prevention = db.Column(db.Text)
    management = db.Column(db.Text)
    weather_risk_factors = db.Column(db.Text)
    treatment_category = db.Column(db.String(120))
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), onupdate=db.func.now())

    treatments = db.relationship("Treatment", back_populates="disease_obj")
