"""Flask application factory."""

from pathlib import Path

from flask import Flask

from ..config import Config
from ..storage.database import Database


def create_app(config_path: str = "config.yaml") -> Flask:
    """Create and configure the Flask application."""
    app = Flask(
        __name__,
        template_folder="templates",
        static_folder="../static",
    )

    # Load config and initialize database
    cfg = Config.from_yaml(config_path)
    app.config["DATABASE"] = Database(cfg.database_path)
    app.config["APP_CONFIG"] = cfg

    # Register routes
    from . import routes

    app.register_blueprint(routes.bp)

    # Register custom Jinja filters
    @app.template_filter("truncate_smart")
    def truncate_smart(text: str | None, length: int = 150) -> str:
        """Truncate text at word boundary."""
        if not text or len(text) <= length:
            return text or ""
        truncated = text[:length].rsplit(" ", 1)[0]
        return truncated + "..." if len(truncated) < len(text) else text

    @app.template_filter("domain_display")
    def domain_display(domain: str) -> str:
        """Clean up domain for display."""
        if domain.startswith("www."):
            return domain[4:]
        return domain

    return app
