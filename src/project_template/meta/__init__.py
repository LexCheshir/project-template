from .env_settings import Settings
from .logging import configure_logging

__all__ = [
    "settings",
]

app_name = "project-template"
settings = Settings(app_name=app_name)

configure_logging(settings=settings)
