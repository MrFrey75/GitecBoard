# app/models/page.py

from app.main import db

class Page(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    start_time = db.Column(db.DateTime, nullable=True)
    end_time = db.Column(db.DateTime, nullable=True)
    created_at = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())

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
