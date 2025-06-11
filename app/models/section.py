# app/models/section.py

from app.main import db

class Section(db.Model):
    __tablename__ = 'section'
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(20))
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text)
    meta = db.Column(db.String(100), nullable=True)
    start_time = db.Column(db.DateTime, nullable=True)
    end_time = db.Column(db.DateTime, nullable=True)
    created_at = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())
    is_deleted = db.Column(db.Boolean, default=False)
    is_system = db.Column(db.Boolean, default=False)

    section_assignments = db.relationship(
        'SectionAssignment',
        back_populates='section',
        cascade='all, delete-orphan'
    )
