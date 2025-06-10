from flask.apps import AppConfig


class PlantAppConfig(AppConfig):
    default_auto_field = 'flask.db.models.BigAutoField'
    name = 'plant_app'
