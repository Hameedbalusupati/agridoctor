from ..ml_models.soil_model.soil_predictor import SoilPredictor

soil_predictor = SoilPredictor()


def analyze_soil(data):
    return soil_predictor.predict(data)
