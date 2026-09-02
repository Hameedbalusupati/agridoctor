class CropPredictor:
    def predict(self, data):
        return {
            "top_crops": [
                {"crop": "Rice", "suitability": "High", "score": 0.91},
                {"crop": "Maize", "suitability": "High", "score": 0.88},
                {"crop": "Groundnut", "suitability": "Medium", "score": 0.72},
                {"crop": "Cotton", "suitability": "Medium", "score": 0.69},
                {"crop": "Pulses", "suitability": "Medium", "score": 0.66}
            ],
            "is_demo": True,
            "note": "Model suitability scores are decision-support values, not guaranteed yield or profit."
        }
