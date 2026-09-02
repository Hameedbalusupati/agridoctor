def build_smart_recommendation(disease, soil, weather, crop_name):
    risk = "MEDIUM"
    if weather.get("humidity", 0) > 75 or "rain" in str(weather.get("forecast", "")).lower():
        risk = "HIGH"

    return {
        "current_crop": crop_name,
        "disease": disease,
        "soil": soil,
        "weather": weather,
        "risk_level": risk,
        "recommendation": [
            "Inspect nearby plants for signs of spread.",
            "Remove severely infected leaves.",
            "Improve air circulation in the field.",
            "Avoid unnecessary leaf wetness during irrigation.",
            "Follow verified treatment guidance and local agricultural authority instructions.",
            "Recheck plants after rainfall or high humidity events."
        ]
    }
