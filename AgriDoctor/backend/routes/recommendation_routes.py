from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from ..services.recommendation_service import build_smart_recommendation

recommendation_bp = Blueprint("recommendations", __name__)


@recommendation_bp.route("/recommendations", methods=["GET"])
@jwt_required()
def recommendations():
    disease = request.args.get("disease", "Early Blight")
    crop_name = request.args.get("crop", "Tomato")
    try:
        humidity = float(request.args.get("humidity", 82))
    except (TypeError, ValueError):
        humidity = 82
    forecast = request.args.get("forecast", "Rain expected")
    result = build_smart_recommendation(
        disease,
        {"pH": 6.4},
        {"humidity": humidity, "forecast": forecast},
        crop_name
    )
    return jsonify({"recommendations": [result]})


@recommendation_bp.route("/recommendations/<int:recommendation_id>", methods=["GET"])
@jwt_required()
def recommendation_detail(recommendation_id):
    return jsonify({"id": recommendation_id, "recommendation": "Follow verified treatment guidance and recheck after rainfall."})
