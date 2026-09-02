from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required
from ..services.recommendation_service import build_smart_recommendation

recommendation_bp = Blueprint("recommendations", __name__)


@recommendation_bp.route("/recommendations", methods=["GET"])
@jwt_required()
def recommendations():
    result = build_smart_recommendation(
        "Early Blight",
        {"pH": 6.4},
        {"humidity": 82, "forecast": "Rain expected"},
        "Tomato"
    )
    return jsonify({"recommendations": [result]})


@recommendation_bp.route("/recommendations/<int:recommendation_id>", methods=["GET"])
@jwt_required()
def recommendation_detail(recommendation_id):
    return jsonify({"id": recommendation_id, "recommendation": "Follow verified treatment guidance and recheck after rainfall."})
