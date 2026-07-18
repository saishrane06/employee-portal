import os

from .development import DevelopmentConfig
from .docker import DockerConfig
from .testing import TestingConfig
from .production import ProductionConfig

config = {

    "development": DevelopmentConfig,

    "docker": DockerConfig,

    "testing": TestingConfig,

    "production": ProductionConfig,

    "default": DevelopmentConfig
}

config_name = os.getenv("FLASK_CONFIG", "default")

Config = config[config_name]