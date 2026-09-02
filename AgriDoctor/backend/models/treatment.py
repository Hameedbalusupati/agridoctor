from ..database.db import db


class Treatment(db.Model):
    __tablename__ = "treatments"

    id = db.Column(db.Integer, primary_key=True)
    disease_id = db.Column(db.Integer, db.ForeignKey("diseases.id"), nullable=False)
    crop = db.Column(db.String(120), nullable=False)
    disease = db.Column(db.String(180), nullable=False)
    treatment_category = db.Column(db.String(120))
    active_ingredient = db.Column(db.String(120))
    product_name = db.Column(db.String(180))
    application_guidance = db.Column(db.Text)
    safety_precautions = db.Column(db.Text)
    pre_harvest_interval = db.Column(db.String(120))
    region = db.Column(db.String(120))
    source = db.Column(db.String(200))
    last_updated = db.Column(db.String(50))
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), onupdate=db.func.now())

    disease_obj = db.relationship("Disease", back_populates="treatments")
