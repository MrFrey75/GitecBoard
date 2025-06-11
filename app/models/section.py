# app/models/section.py

from app.main import db

class Section(db.Model):
    __tablename__ = 'section' # Renamed to avoid conflict with the SectionAssignment model
    id = db.Column(db.Integer, primary_key=True) # Unique identifier for the section
    type = db.Column(db.String(20)) # Type of the section (e.g., 'text', 'image', 'video', etc.)
    title = db.Column(db.String(100), nullable=False) # Title of the section
    content = db.Column(db.Text) # Content of the section, can be text, HTML, etc.
    meta = db.Column(db.String(100), nullable=True) # Metadata for the section, can be JSON or any other format
    start_time = db.Column(db.DateTime, nullable=True) # Start time for the section
    end_time = db.Column(db.DateTime, nullable=True) # End time for the section
    created_at = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp()) # Timestamp for when the section was created
    is_deleted = db.Column(db.Boolean, default=False) # Indicates if the section is deleted
    is_system = db.Column(db.Boolean, default=False) # Indicates if this is a system section - do not allow deletion

    section_assignments = db.relationship('SectionAssignment', back_populates='section', cascade='all, delete-orphan') # Relationship to SectionAssignment


