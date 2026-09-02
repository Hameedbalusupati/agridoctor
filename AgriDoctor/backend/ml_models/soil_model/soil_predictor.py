class SoilPredictor:
    def predict(self, data):
        ph = float(data.get("ph", 7.0))
        if ph < 6.0:
            condition = "Slightly acidic"
        elif ph > 7.5:
            condition = "Slightly alkaline"
        else:
            condition = "Balanced"

        return {
            "soil_condition": condition,
            "nutrient_status": "N and K values should be reviewed against crop stage and local recommendations.",
            "suitable_crops": ["Rice", "Maize", "Groundnut"],
            "recommendations": [
                "Apply organic matter to improve soil structure.",
                "Use balanced nutrient management based on crop stage.",
                "Test soil again after rainfall or heavy irrigation."
            ],
            "is_demo": True
        }
