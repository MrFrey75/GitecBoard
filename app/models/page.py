# app/models/page.py

from app.main import db

class Page(db.Model):
    __tablename__ = 'page'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    slug_identifier = db.Column(db.String(100), nullable=False, unique=True)

    start_time = db.Column(db.DateTime, nullable=True)
    end_time = db.Column(db.DateTime, nullable=True)

    created_at = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())

    is_published = db.Column(db.Boolean, default=False) # Indicates if the page is published
    is_deleted = db.Column(db.Boolean, default=False) # Indicates if the page is deleted

    is_system = db.Column(db.Boolean, default=False) # Indicates if this is a system page - do not allow deletion

class SectionAssignment(db.Model):
    __tablename__ = 'section_assignment' # Renamed to avoid conflict with the Section model
    id = db.Column(db.Integer, primary_key=True) # Unique identifier for the section assignment
    page_id = db.Column(db.Integer, db.ForeignKey('page.id'), nullable=False) # Foreign key to the page this section assignment belongs to
    section_id = db.Column(db.Integer, db.ForeignKey('section.id'), nullable=False) # Foreign key to the section this assignment is for
    order = db.Column(db.Integer, default=0) # Order of the section in the page
    start_time = db.Column(db.DateTime, nullable=True) # Start time for the section assignment
    end_time = db.Column(db.DateTime, nullable=True) # End time for the section assignment

    section = db.relationship('Section', back_populates='section_assignments') # Relationship to Section
    page = db.relationship('Page', back_populates='section_assignments') # Relationship to Page

    # Add this to fix the error
    page_assignments = db.relationship(
        'PageAssignment',
        back_populates='page',
        cascade="all, delete-orphan"
    )

    section_assignments = db.relationship(
        'SectionAssignment',
        back_populates='page',
        cascade="all, delete-orphan"
    )
