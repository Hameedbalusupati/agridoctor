import json
from pathlib import Path


class DiseasePredictor:
    def __init__(self):
        self.model_dir = Path(__file__).resolve().parent
        self.class_names = self._load_class_names()

    def _load_class_names(self):
        path = self.model_dir / "class_names.json"
        if path.exists():
            with open(path, "r", encoding="utf-8") as fh:
                return json.load(fh)
        return ["Tomato___Early_Blight", "Tomato___Late_Blight", "Tomato___Healthy", "Potato___Early_Blight"]

    def predict(self, image_path):
        class_name = self.class_names[0] if self.class_names else "Tomato___Early_Blight"
        crop, disease = class_name.split("___") if "___" in class_name else ("Tomato", "Early Blight")
        confidence = 0.94
        return {
            "crop": crop,
            "disease": disease,
            "confidence": f"{confidence * 100:.1f}%",
            "severity": "Moderate",
            "symptoms": "Brown lesions on leaves with concentric rings or irregular spotting.",
            "causes": "High humidity, poor airflow, and repeated leaf wetness can favor fungal spread.",
            "management": "Remove affected leaves, improve ventilation, and avoid unnecessary irrigation overhead.",
            "treatment": "Follow verified treatment guidance and registered label instructions for the target crop and disease.",
            "weather_risk": "HIGH",
            "is_demo": True,
            "message": "This application provides AI-based decision support. Always verify treatment recommendations with the product label and local agricultural experts or authorities."
        }
