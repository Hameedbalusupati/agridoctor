from ..ml_models.crop_model.crop_predictor import CropPredictor

crop_predictor = CropPredictor()


def recommend_crops(data):
    return crop_predictor.predict(data)
