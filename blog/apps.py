from django.apps import AppConfig


class BlogConfig(AppConfig):
    """App configuration for the Music Corner blog app."""
    default_auto_field = "django.db.models.BigAutoField"
    name = "blog"