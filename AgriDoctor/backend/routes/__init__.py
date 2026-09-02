from .auth_routes import auth_bp
from .farmer_routes import farmer_bp
from .disease_routes import disease_bp
from .crop_routes import crop_bp
from .soil_routes import soil_bp
from .weather_routes import weather_bp
from .recommendation_routes import recommendation_bp
from .notification_routes import notification_bp
from .admin_routes import admin_bp


def register_blueprints(app):
    app.register_blueprint(auth_bp, url_prefix="/api/auth")
    app.register_blueprint(farmer_bp, url_prefix="/api/farmer")
    app.register_blueprint(disease_bp, url_prefix="/api/disease")
    app.register_blueprint(crop_bp, url_prefix="/api/crop")
    app.register_blueprint(soil_bp, url_prefix="/api/soil")
    app.register_blueprint(weather_bp, url_prefix="/api/weather")
    app.register_blueprint(recommendation_bp, url_prefix="/api")
    app.register_blueprint(notification_bp, url_prefix="/api")
    app.register_blueprint(admin_bp, url_prefix="/api/admin")
