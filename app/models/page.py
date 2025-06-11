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

    is_published = db.Column(db.Boolean, default=False)
    is_deleted = db.Column(db.Boolean, default=False)
    is_system = db.Column(db.Boolean, default=False)

    # Relationships
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

class SectionAssignment(db.Model):
    __tablename__ = 'section_assignment'
    id = db.Column(db.Integer, primary_key=True)
    page_id = db.Column(db.Integer, db.ForeignKey('page.id'), nullable=False)
    section_id = db.Column(db.Integer, db.ForeignKey('section.id'), nullable=False)
    order = db.Column(db.Integer, default=0)
    start_time = db.Column(db.DateTime, nullable=True)
    end_time = db.Column(db.DateTime, nullable=True)

    page = db.relationship('Page', back_populates='section_assignments')
    section = db.relationship('Section', back_populates='section_assignments')
