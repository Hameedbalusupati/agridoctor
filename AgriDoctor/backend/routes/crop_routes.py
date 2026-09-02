from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from ..database.db import db
from ..models.user import User
from ..models.crop_recommendation import CropRecommendation
from ..services.crop_service import recommend_crops

crop_bp = Blueprint("crop", __name__)


@crop_bp.route("/recommend", methods=["POST"])
@jwt_required()
def recommend():
    data = request.get_json(silent=True) or {}
    if not all(key in data for key in ["nitrogen", "phosphorus", "potassium", "temperature", "humidity", "ph", "rainfall"]):
        return jsonify({"error": "Missing crop recommendation fields"}), 400
    user = User.query.get(get_jwt_identity())
    prediction = recommend_crops(data)
    farmer_id = user.farmer_profile.id if user and user.farmer_profile else 1
    record = CropRecommendation(
        farmer_id=farmer_id,
        recommended_crops=str(prediction["top_crops"]),
        input_conditions=str(data),
        model_scores=str({item["crop"]: item["score"] for item in prediction["top_crops"]})
    )
    db.session.add(record)
    db.session.commit()
    return jsonify({"message": "Recommendations generated", "result": prediction})


@crop_bp.route("/history", methods=["GET"])
@jwt_required()
def history():
    user = User.query.get(get_jwt_identity())
    if not user or not user.farmer_profile:
        return jsonify({"history": []})
    records = CropRecommendation.query.filter_by(farmer_id=user.farmer_profile.id).order_by(CropRecommendation.created_at.desc()).all()
    return jsonify({"history": [{"id": r.id, "recommended_crops": r.recommended_crops, "input_conditions": r.input_conditions, "created_at": r.created_at.isoformat()} for r in records]})
