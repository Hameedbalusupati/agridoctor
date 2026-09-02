from ..ml_models.disease_model.disease_predictor import DiseasePredictor

disease_predictor = DiseasePredictor()


def predict_disease_from_image(image_path):
    return disease_predictor.predict(image_path)
