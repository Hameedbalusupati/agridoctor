from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from ..database.db import db
from ..models.user import User
from ..models.soil_record import SoilRecord
from ..services.soil_service import analyze_soil

soil_bp = Blueprint("soil", __name__)


@soil_bp.route("/analyze", methods=["POST"])
@jwt_required()
def analyze():
    data = request.get_json(silent=True) or {}
    required = ["nitrogen", "phosphorus", "potassium", "ph", "moisture", "temperature", "rainfall"]
    missing = [field for field in required if field not in data]
    if missing:
        return jsonify({"error": f"Missing soil fields: {', '.join(missing)}"}), 400

    user = User.query.get(get_jwt_identity())
    result = analyze_soil({
        "nitrogen": data["nitrogen"],
        "phosphorus": data["phosphorus"],
        "potassium": data["potassium"],
        "ph": data["ph"],
        "moisture": data["moisture"],
        "temperature": data["temperature"],
        "rainfall": data["rainfall"]
    })
    record = SoilRecord(
        farmer_id=user.farmer_profile.id if user and user.farmer_profile else 1,
        nitrogen=data["nitrogen"],
        phosphorus=data["phosphorus"],
        potassium=data["potassium"],
        ph=data["ph"],
        moisture=data["moisture"],
        temperature=data["temperature"],
        rainfall=data["rainfall"],
        soil_condition=result.get("soil_condition"),
        nutrient_status=result.get("nutrient_status"),
        suitable_crops=str(result.get("suitable_crops", [])),
        recommendations=str(result.get("recommendations", []))
    )
    db.session.add(record)
    db.session.commit()

    return jsonify({"message": "Soil analysis complete", "result": result})


@soil_bp.route("/history", methods=["GET"])
@jwt_required()
def history():
    user = User.query.get(get_jwt_identity())
    if not user or not user.farmer_profile:
        return jsonify({"history": []})
    records = SoilRecord.query.filter_by(farmer_id=user.farmer_profile.id).order_by(SoilRecord.created_at.desc()).all()
    return jsonify({"history": [{
        "id": r.id,
        "N": r.nitrogen,
        "P": r.phosphorus,
        "K": r.potassium,
        "pH": r.ph,
        "soil_condition": r.soil_condition,
        "created_at": r.created_at.isoformat()
    } for r in records]})
