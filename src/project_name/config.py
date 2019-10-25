import os


class BaseConfig:
    """Base flask configuration."""

    CONFIG_FILE = os.path.abspath(__file__)
    CONFIG_DIR = os.path.dirname(CONFIG_FILE)
    BASE_DIR = os.path.abspath(os.path.join(CONFIG_DIR, '..'))

    SQLALCHEMY_DATABASE_URI = os.getenv('EXAMPLE_DB_URI',
                                        'sqlite:///census.sqlite')
    SQLALCHEMY_MIGRATE_REPO = os.path.join(CONFIG_DIR, 'db_repository')

    DEBUG = False
    TESTING = False
    HOST = 'localhost'
    PORT = 8000


class DevelopmentConfig(BaseConfig):
    """Flask configuration for devserver."""

    DEBUG = True
    TESTING = False


class ProductionConfig(BaseConfig):
    """Flask configuration for production."""

    DEBUG = False
    TESTING = False


class TestingConfig(BaseConfig):
    """Flask configuration for tests."""

    SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/test.db'

    DEBUG = False
    TESTING = True
    PORT = 9091


CONFIG = {
    'default': 'project_name.config.DevelopmentConfig'
}


def configure_app(app, config_name):
    """Configure flask app."""
    app.config.from_object(CONFIG[config_name])
