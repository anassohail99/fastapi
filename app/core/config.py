"""Application configuration loaded from environment."""

from typing import List, Optional

from pydantic_settings import BaseSettings, SettingsConfigDict

# Default CORS origins (always included when FRONTEND_ORIGIN is set)
DEFAULT_CORS_ORIGINS = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]


class Settings(BaseSettings):
    """Settings loaded from .env. Use for CORS, auth, and feature flags."""

    # App
    app_name: str = "Portfolio API"
    debug: bool = False

    # CORS: primary frontend URL; added to allowed_origins
    frontend_origin: Optional[str] = None

    # Auth: Firebase (optional until you implement Firebase)
    google_application_credentials: Optional[str] = None
    firebase_credentials: Optional[str] = None

    # Auth: JWT (optional if you use JWT instead of Firebase)
    jwt_secret: Optional[str] = None

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

    @property
    def allowed_origins(self) -> List[str]:
        """CORS allowed origins: defaults + frontend_origin if set."""
        origins = list(DEFAULT_CORS_ORIGINS)
        if self.frontend_origin and self.frontend_origin not in origins:
            origins.append(self.frontend_origin)
        return origins


# Single instance for the app to import
settings = Settings()
