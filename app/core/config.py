from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    """Manages application settings."""
    PROJECT_NAME: str = "Image Fetcher Project"
    
    # --- THIS IS THE FIX ---
    # We add the BASE_URL setting, with a default for local development.
    # When deployed, it will use the value from the Render environment variables.
    BASE_URL: str = "http://127.0.0.1:8000"
    
    CLIP_FILTER_THRESHOLD: float = 0.28
    PEXELS_API_KEY: str = "YOUR_DEFAULT_KEY_IF_NOT_IN_ENV"

    # Email Configuration
    MAIL_USERNAME: str
    MAIL_PASSWORD: str
    MAIL_FROM: str
    MAIL_PORT: int = 587
    MAIL_SERVER: str = "smtp.sendgrid.net"
    MAIL_STARTTLS: bool = True
    MAIL_SSL_TLS: bool = False
    USE_CREDENTIALS: bool = True
    VALIDATE_CERTS: bool = False # Keep False to avoid SSL issues
    MAIL_BACKEND: str = "smtp"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()
