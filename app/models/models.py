# app/models/models.py

from app.main import db

class MediaAsset(db.Model):
    __tablename__ = 'media_asset' # Renamed to avoid conflict with the Media model
    id = db.Column(db.Integer, primary_key=True) # Unique identifier for the media asset
    file_path = db.Column(db.String(255), nullable=False) # Path to the media file
    created_at = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp()) # Timestamp for when the media asset was created
    media_type = db.Column(db.Enum('image', 'video', name='media_type_enum'), nullable=False) # Type of media (image, video, etc.)

class AppSetting(db.Model):
    __tablename__ = 'app_settings' # Renamed to avoid conflict with the Settings model
    id = db.Column(db.Integer, primary_key=True) # Unique identifier for the app setting
    key = db.Column(db.String(50), unique=True, nullable=False) # Key for the app setting
    value = db.Column(db.String(255), nullable=False) # Value for the app setting
    description = db.Column(db.String(255), nullable=True) # Description of the app setting
    created_at = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp()) # Timestamp for when the app setting was created

    def __repr__(self):
        return f"<AppSettings {self.key}: {self.value}>"